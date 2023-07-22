"""
Provide implementation of schemas.
"""
from __future__ import annotations

from pydantic import BaseModel

from diagrams_yaml.enums import RelationType


class YamlDiagram(BaseModel):
    """
    YAML diagram schema implementation.
    """

    name: str
    show: bool
    resources: list[YamlDiagramResource]


class YamlDiagramResource(BaseModel):
    """
    YAML diagram resource schema implementation.
    """

    id: str | int
    name: str
    type: str
    of: list[YamlDiagramResource] | None = []
    relates: list[YamlDiagramResourceRelationship] | None = []


class YamlDiagramResourceRelationship(BaseModel):
    """
    Yaml diagram resource relationship schema implementation.
    """

    to: str
    type: RelationType


class Relationship(BaseModel):
    """
    Relationship schema implementation.

    Is used internally between layers and functions.
    """

    from_: str
    to: str
    type: str
