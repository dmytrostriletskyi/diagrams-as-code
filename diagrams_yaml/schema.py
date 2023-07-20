"""
Provide implementation of schemas.
"""
from pydantic import BaseModel


class YamlDiagram(BaseModel):
    """
    YAML diagram schema implementation.
    """

    name: str
    show: bool
    resources: list['YamlDiagramResource']


class YamlDiagramResource(BaseModel):
    """
    YAML diagram resource schema implementation.
    """

    id: str | int
    name: str
    type: str
    of: list['YamlDiagramResource'] | None = []
    relates: list['YamlDiagramResourceRelationship'] | None = []


class YamlDiagramResourceRelationship(BaseModel):
    """
    Yaml diagram resource relationship schema implementation.
    """

    to: str
    type: str


class Relationship(BaseModel):
    """
    Relationship schema implementation.

    Is used internally between layers and functions.
    """

    from_: str
    to: str
    type: str
