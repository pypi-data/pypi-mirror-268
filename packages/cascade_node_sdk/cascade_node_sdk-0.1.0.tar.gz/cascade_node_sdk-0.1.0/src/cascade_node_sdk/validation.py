from enum import Enum

from pydantic import BaseModel
import yaml

CATALOG_CONFIG_PATH = "catalog-info.yaml"


class AgentCategory(str, Enum):
    Multimodal = "Multimodal"
    ComputerVision = "Computer Vision"
    NaturalLanguage = "Natural Language"
    Audio = "Audio"
    Tabular = "Tabular"


class AgentAccessLevel(str, Enum):
    Public = "PUBLIC"
    Private = "PRIVATE"


class AgentType(str, Enum):
    Type = "agent"


class Metadata(BaseModel):
    name: str
    namespace: str
    description: str


class Spec(BaseModel):
    category: AgentCategory
    access_level: AgentAccessLevel
    type: AgentType


class CatalogInfo(BaseModel):
    metadata: Metadata
    spec: Spec

    class Config:
        validate_assignment = True


def load_catalog_info(catalog_path: str = CATALOG_CONFIG_PATH):
    try:
        with open(catalog_path) as file:
            catalog_info = yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Catalog info file not found at {catalog_path}")

    try:
        catalog_info = CatalogInfo(**catalog_info)
    except Exception as e:
        raise ValueError(f"Catalog info file is not valid: {e}")

    # strip trailing newline from description
    catalog_info.metadata.description = catalog_info.metadata.description.rstrip("\n")

    return catalog_info
