import click
import requests

from .agent import AgentWrapper


class ProxyAgentExecutor:
    def __init__(self, proxy_to_url):
        self.proxy_to_url = proxy_to_url
        self.tools = []  # dummy tools, this is a leaf node so it doesn't have any downstream tools

    async def ainvoke(self, prompt, callbacks=[]):
        if "input" in prompt:
            prompt = prompt["input"]

        body = {
            "prompt": prompt,
            "use_context": True,
        }

        completions = self.completions(body)
        if completions is None:
            body["use_context"] = False
            completions = self.completions(body)

        return completions

    def completions(self, body):
        # TODO: how to implement generic parsing? add option for user to provide jsonpath?
        try:
            response = requests.post(self.proxy_to_url, json=body)
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(e)
            return None


@click.group()
def cli():
    pass


@cli.command()
@click.option("--host", "-h", default="localhost", help="Controller host")
@click.option("--proxy_to_url", "-u", default="http://example.com", help="Proxy to URL")
def proxy(host, proxy_to_url):
    click.echo(f"Controller host: {host}")
    click.echo(f"Proxy to URL: {proxy_to_url}")

    node = AgentWrapper(hub_broker=host)
    node.run_agent(ProxyAgentExecutor(proxy_to_url))

if __name__ == "__main__":
    cli()
