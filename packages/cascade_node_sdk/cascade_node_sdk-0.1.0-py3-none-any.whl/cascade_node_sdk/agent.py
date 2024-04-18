import asyncio
import json
import logging
from os import environ
import signal
import time

from dotenv import load_dotenv
from langchain.tools import Tool
from langchain.tools.render import render_text_description
from langchain_core.utils.function_calling import convert_to_openai_tool
import nats
import nest_asyncio
from opentelemetry import trace
from opentelemetry.propagate import extract
from traceloop.sdk import Traceloop

from cascade_node_sdk.protobuffs import cascade_pb2

from .validation import CatalogInfo, load_catalog_info

nest_asyncio.apply()

load_dotenv()

logging.basicConfig(level=logging.INFO)


class AgentWrapper:
    """
    A wrapper class for the Langchain agentExecutor object.
    """

    _agent_executor = None

    def __init__(
        self,
        hub_broker,
        config_path="catalog-info.yaml",
        config: CatalogInfo | None = None,
    ):
        self.hub_broker = hub_broker + ":4222"

        if config is not None:
            self.config = config
        else:
            self.config = load_catalog_info(config_path)

        # create id from base64 encoded namespace and name
        self.id = self.config.metadata.namespace + "." + self.config.metadata.name

    def run_agent(
        self,
        agentExecutor,
        input_formatter=None,
        response_formatter=None,
        on_env_change=lambda: logging.info("environment changed"),
    ):
        self._agent_executor = agentExecutor
        self.input_formatter = input_formatter
        self.response_formatter = response_formatter
        self.on_env_change = on_env_change
        self.tool_calling_method = cascade_pb2.ToolCallingMethod.Value("AGENT")

        # configure tracing
        self._configure_tracing(self.config.metadata.name)

        self.loop = asyncio.get_event_loop()

        self.loop.run_until_complete(self._launch_tasks())

        self.loop.run_forever()

    def refresh_agent_executor(self, _agent_executor):
        self._agent_executor = _agent_executor

    def agent_tools(self):
        if self._agent_executor is None:
            return []

        # assume that the agent executor has a tools attribute but handle the case where it does not
        try:
            return self._agent_executor.tools
        except AttributeError:
            return []

    def _configure_tracing(self, name):
        disable_tracing = environ.get("DISABLE_TRACING")
        if environ.get("OTEL_COLLECTOR_URL"):
            environ["TRACELOOP_BASE_URL"] = environ.get("OTEL_COLLECTOR_URL")

        if disable_tracing:
            logging.warning("tracing is disabled")
            # create a no-op trace provider
            self.tracer = trace.NoOpTracer()
            return

        # initialize tracing, disable batch mode to see traces in real time
        Traceloop.init(app_name=name, disable_batch=True)
        self.tracer = trace.get_tracer(name)

    async def error_cb(self, e):
        logging.error(f"There was an error connecting: {e}") # noqa: G004

    async def _launch_tasks(self):
        self._nc = await nats.connect(
            self.hub_broker, name=self.id, error_cb=self.error_cb
        )

        logging.info(
            f"[{self.config.metadata.name}] connected to broker [{self.hub_broker}]"  # noqa: G004
        )  # noqa: G004

        for sig in ("SIGINT", "SIGTERM"):
            try:
                asyncio.get_running_loop().add_signal_handler(
                    getattr(signal, sig), self._signal_handler
                )
            except RuntimeError:
                logging.error(f"Could not add signal handler for {sig}")  # noqa: G004
                continue

        # subscribe to the tools and knowledge topics
        await self._nc.subscribe(self._format_topic("tools"), cb=self._dynamic_tool_cb)
        await self._nc.subscribe(
            self._format_topic("tool-calling-method"), cb=self._retrieval_method_cb
        )
        await self._nc.subscribe(self._format_topic("knowledge"), cb=self._knowledge_cb)
        await self._nc.subscribe(self._format_topic("set-env"), cb=self._set_env_cb)

        for topic in self._nc._subs.values():
            logging.info(
                f"[{self.config.metadata.name}] subscribed -> [{topic._subject}]" # noqa: G004
            )

    def _format_topic(self, topic: str):
        return f"{self.id}.{topic}"

    async def _retrieval_method_cb(self, msg):
        payload = msg.data

        try:
            tool_calling_method = cascade_pb2.SetToolCallingMethod()
            tool_calling_method.ParseFromString(payload)

            logging.info(
                f"received tool calling method request: {tool_calling_method.method}"  # noqa: G004
            )
            self.tool_calling_method = tool_calling_method.method
        except Exception as e:
            logging.error(f"Error in setting tool calling method: {e}")  # noqa: G004
            pass

    # @aworkflow(name="tool_callback")
    async def _tool_callback(self, topic: str, prompt):
        if "input" in prompt:
            prompt = prompt["input"]

        payload = cascade_pb2.KnowledgeRequest(prompt=prompt).SerializeToString()

        # get the span context from the workflow
        span_context = trace.get_current_span().get_span_context()

        trace_id = format(span_context.trace_id, "x")
        span_id = format(span_context.span_id, "x")

        # set traceparent header
        headers = {}
        headers["traceparent"] = f"00-{trace_id}-{span_id}-01"

        future = self._nc.request(
            subject=topic, payload=payload, headers=headers, timeout=45
        )

        msg = await future
        return msg.data.decode()

    async def _dynamic_tool_cb(self, msg):
        payload = msg.data

        tool = cascade_pb2.AgentAsTool()
        tool.ParseFromString(payload)

        if tool.add is False:
            logging.info(f"removing tool {tool.agent_name} from agent executor")  # noqa: G004
            for t in self._agent_executor.tools:
                # check if t hassttr id
                if hasattr(t, "id") and t.id == tool.agent_id:
                    self._agent_executor.tools.remove(t)

            return

        # check if the tool is already in the agent executor
        for t in self._agent_executor.tools:
            if hasattr(t, "id") and t.name == tool.agent_name:
                return

        logging.info(
            f"adding tool {tool.agent_name}, len(tools): {len(self._agent_executor.tools) + 1}"  # noqa: G004
        )

        topic = f"knowledge.{tool.agent_id}"

        def tool_callback(prompt):
            return asyncio.run(self._tool_callback(topic, prompt))

        # create a langchain tool from the agent tool
        agentTool = Tool.from_function(
            func=tool_callback,
            name=tool.agent_name,
            description=tool.agent_description,
            return_direct=tool.return_direct,
            id=tool.agent_id,
        )

        # add the tool to the agent executor
        self._update_agent(agentTool)

    def _update_agent(self, tool: Tool):
        if self._agent_executor is None:
            return

        self._agent_executor.tools.append(tool)

        if "agent" not in self._agent_executor.__dict__:
            return

        # for langchain agents we must update the prompt partial variables
        # which are used to select the correct tool

        for _, chain_sequence in self._agent_executor.__dict__["agent"].runnable:
            if chain_sequence is None:
                continue

            for component in chain_sequence:
                if hasattr(component, "kwargs"):
                    component.kwargs = {
                        "tools": [
                            convert_to_openai_tool(t)
                            for t in self._agent_executor.tools
                        ],
                    }

                # check if component has partial variables
                if hasattr(component, "partial_variables"):
                    component.partial_variables = {
                        "tools": render_text_description(
                            list(self._agent_executor.tools)
                        ),
                        "tool_names": ", ".join(
                            [t.name for t in self._agent_executor.tools]
                        ),
                    }

    async def _knowledge_cb(self, msg):
        request = cascade_pb2.KnowledgeRequest()
        request.ParseFromString(msg.data)

        ctx = extract(carrier=msg.headers)

        with self.tracer.start_as_current_span(
            "_knowledge_handler", context=ctx
        ) as span:
            span.set_attribute("prompt", request.prompt)

            logging.info(f"received knowledge event: {request.prompt}")  # noqa: G004

            if self.input_formatter is not None:
                request.prompt = self.input_formatter(request.prompt)

            match self.tool_calling_method:
                case cascade_pb2.ToolCallingMethod.MULTIPLEX:
                    result = await self._multiplex_prompt_to_single_input_tools(
                        request.prompt
                    )
                    await msg.respond(result.encode())
                case cascade_pb2.ToolCallingMethod.AGENT:
                    result = await self._run(request)
                    # encode the result, if it is a dict or list encode it as json
                    if isinstance(result, dict | list):
                        result = json.dumps(result, indent=4, sort_keys=True)
                    await msg.respond(result.encode())
                case _:
                    logging.error(
                        f"unknown tool calling method {self.tool_calling_method}"  # noqa: G004
                    )
                    return

    async def _run(self, request: cascade_pb2.KnowledgeRequest):
        Traceloop.set_association_properties({"prompt": request.prompt})
        input = {"input": request.prompt}

        try:
            result = self._agent_executor.invoke(input)
        except Exception as e:
            logging.error(f"Error in agent executor: {e}")  # noqa: G004
            logging.error(f"prompt: {request.prompt}")  # noqa: G004
            return {"error": str(e)}

        if self.response_formatter is not None:
            logging.info("invoking response formatter")
            result = self.response_formatter(result)

        logging.info(f"knowledge result: {result}")  # noqa: G004

        return result

    async def _multiplex_prompt_to_single_input_tools(self, prompt):
        tools = self.agent_tools()

        results = await asyncio.gather(
            *[self._run_tool(tool, prompt) for tool in tools]
        )

        logging.info(f"multiplexed prompt to single input tools: {results}")  # noqa: G004

        # decode first
        tool_responses = [
            {"tool": tool.name, "response": response}
            for tool, response in zip(tools, results)
        ]

        return json.dumps(tool_responses, indent=4, sort_keys=True)

    async def _run_tool(self, tool, prompt):
        if tool.coroutine is not None:
            return await tool.coroutine(prompt)
        else:
            return tool.func(prompt)

    async def _set_env_cb(self, msg):
        payload = msg.data
        env = cascade_pb2.NodeEnv()
        env.ParseFromString(payload)

        for key, value in env.env_vars.items():
            if key in environ:
                logging.info(f"overwriting environment variable {key}")  # noqa: G004
            else:
                logging.info(f"setting environment variable {key}")  # noqa: G004
            environ[key] = value

        self.on_env_change()

    def _signal_handler(self):
        logging.info("Shutting down agent...")

        if not self._nc.is_closed:
            task = asyncio.create_task(self._nc.drain())

        time.sleep(0.25)
        self.loop.stop()
        self.loop.stop()

        if not self._nc.is_closed:
            task.cancel()
