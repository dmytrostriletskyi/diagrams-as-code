"""
Provide implementation of schemas.
"""
from __future__ import annotations

from pydantic import BaseModel

from diagrams_yaml.enums import (
    RelationType,
    DiagramDirection,
    DiagramFormat,
)


class YamlDiagramStyle(BaseModel):
    """
    YAML diagram style schema implementation.
    """

    graph: dict = {}
    node: dict = {}
    edge: dict = {}


class YamlDiagram(BaseModel):
    """
    YAML diagram schema implementation.

    References:
        - https://github.com/mingrammer/diagrams/blob/b19b09761db6f0037fd76e527b9ce6918fbdfcfc/diagrams/__init__.py#L79
    """

    name: str
    file_name: str | None = None
    format: DiagramFormat = DiagramFormat.PNG
    direction: DiagramDirection = DiagramDirection.LEFT_TO_RIGHT
    style: YamlDiagramStyle | None = {}
    label_resources: bool = False
    open: bool = False
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
    label: str | None = None
    color: str | None = None
    style: str | None = None


class Relationship(BaseModel):
    """
    Relationship schema implementation.

    Is used internally between layers and functions.
    """

    from_: str
    to: str
    type: str
    label: str | None = None
    color: str | None = None
    style: str | None = None
