"""
Provide implementation of `diagrams` as a code using YAML.
"""
import sys
import os
import importlib

import yaml

from diagrams import (
    Cluster,
    Diagram,
    Node,
)
from diagrams_yaml.enums import ServiceResourceType
from diagrams_yaml.resources import DiagramGroup
from diagrams_yaml.schema import (
    Relationship,
    YamlDiagram,
)

resources = {}
relationships = []


def get_diagram_node_class(path) -> Node:
    """
    Get a diagram node class.
    """
    provider, resource, service = path.split('.')

    module = importlib.import_module(f'diagrams.{provider}.{resource}')
    class_ = getattr(module, service)

    return class_


def process_resource(resource, parent_id: str, group: DiagramGroup = None) -> None:
    """
    Process a resource.
    """
    if resource.type == ServiceResourceType.CLUSTER.value:
        cluster = Cluster(label=resource.name)
        cluster.__enter__()

        for resource_of in resource.of:
            process_resource(resource=resource_of, parent_id=f'{parent_id}.{resource.id}')

        cluster.__exit__(None, None, None)

    if resource.type == ServiceResourceType.GROUP.value:
        diagram_group = DiagramGroup()

        resources.update({
            f'{parent_id}.{resource.id}': diagram_group,
        })

        for relation in resource.relates:
            relationship = Relationship(
                from_=f'{parent_id}.{resource.id}',
                to=f'diagram.{relation.to}',
                type=relation.type,
            )

            relationships.append(relationship)

        for resource_of in resource.of:
            process_resource(resource=resource_of, parent_id=f'{parent_id}.{resource.id}', group=diagram_group)

    if (
        not resource.type == ServiceResourceType.CLUSTER.value and
        not resource.type == ServiceResourceType.GROUP.value
    ):
        resource_instance = get_diagram_node_class(path=resource.type)(label=resource.name)

        resources.update({
            f'{parent_id}.{resource.id}': resource_instance,
        })

        for relation in resource.relates:
            relationship = Relationship(
                from_=f'{parent_id}.{resource.id}',
                to=f'diagram.{relation.to}',
                type=relation.type,
            )

            relationships.append(relationship)

        if group is not None:
            group.add_node(node=resource_instance)


def entrypoint():
    """
    Provide the entrypoint.
    """
    _, yaml_file_path = sys.argv
    yaml_file_path = os.getcwd() + '/' + yaml_file_path

    with open(yaml_file_path, 'r') as yaml_file:
        yaml_as_dict = yaml.safe_load(yaml_file)

    diagram_as_dict = yaml_as_dict.get('diagram')
    diagram = YamlDiagram(**diagram_as_dict)

    graph_attr = {
        "layout": "osage"  # or ""
    }


    with Diagram(diagram.name, show=diagram.show, graph_attr=graph_attr):
        for resource in diagram.resources:
            process_resource(resource, 'diagram')

        for relationship in relationships:
            resource_from_instance = resources.get(relationship.from_)
            resource_to_instance = resources.get(relationship.to)

            is_resource_from_node = not isinstance(resource_from_instance, DiagramGroup)
            is_resource_from_group = isinstance(resource_from_instance, DiagramGroup)

            is_resource_to_node = not isinstance(resource_to_instance, DiagramGroup)
            is_resource_to_group = isinstance(resource_to_instance, DiagramGroup)

            if is_resource_from_node and is_resource_to_node:
                if relationship.type == 'right':
                    resource_from_instance.__rshift__(other=resource_to_instance)

                if relationship.type == 'unidirectional':
                    resource_from_instance.__sub__(other=resource_to_instance)

            if is_resource_from_group and is_resource_to_node:
                group_nodes = resource_from_instance.get_nodes()

                if relationship.type == 'right':
                    resource_to_instance.__rrshift__(other=group_nodes)

            if is_resource_from_node and is_resource_to_group:
                group_nodes = resource_to_instance.get_nodes()

                if relationship.type == 'right':
                    resource_from_instance.__rshift__(other=group_nodes)

                if relationship.type == 'unidirectional':
                    resource_from_instance.__sub__(other=group_nodes)


if __name__ == '__main__':
    entrypoint()
