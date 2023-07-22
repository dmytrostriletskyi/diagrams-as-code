"""
Provide implementation of `diagrams` as a code using YAML.
"""
import importlib
import os
import sys

import yaml
from diagrams import (
    Cluster,
    Diagram,
    Node,
)

from diagrams_yaml.enums import (
    ServiceResourceType,
    RelationType,
)
from diagrams_yaml.resources import DiagramGroup
from diagrams_yaml.schema import (
    Relationship,
    YamlDiagram,
    YamlDiagramResource,
)

resources = {}
relationships = []


def get_diagram_node_class(path: str) -> Node:
    """
    Get a `diagrams` node class.

    The common example of a path is `aws.analytics.Analytics` which strongly correlates to `diagrams` real defined
    classes. In the example, `Analytics` is a class, the rest `aws.analytics` is a few modules. Basically, there
    are the modules are loaded and then the class is got on fly.

    It helps to reuse the same «path» in both YAML files and execution of classes without a need of redeclaration.

    Arguments:
        path (str): a path to class.

    References:
        - https://diagrams.mingrammer.com/docs/nodes/aws

    Returns:
        The node's class as a `Node`.
    """
    provider, resource, service = path.split('.')

    module = importlib.import_module(f'diagrams.{provider}.{resource}')
    class_ = getattr(module, service)

    return class_


def process_resource(resource: YamlDiagramResource, parent_id: str, group: DiagramGroup = None) -> None:
    """
    Process a resource.

    Basically, this function is recursive because `YAML` file can contain infinite number of configurations. There might
    be a single node (such as EC2 or RDS), a group of nodes and a cluster of nodes and groups further.

    All nodes are stored by unique identifiers in a global storage (`resources`) and then easily fetched from there
    to build relationships. For this, there is a need to always pass parent's resource identifier to have unique
    identifier for each node.

    There is also the resource called `group` which is literary a list of nodes to which other things relate to.

    Arguments:
        resource (YamlDiagramResource): a resource.
        parent_id (str): a parent's identifier.
        group (DiagramGroup): a group.
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
        resource.type != ServiceResourceType.CLUSTER.value and
        resource.type != ServiceResourceType.GROUP.value
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


def entrypoint() -> None:
    """
    Provide the entrypoint.
    """
    _, yaml_file_path = sys.argv
    yaml_file_path = os.getcwd() + '/' + yaml_file_path

    with open(yaml_file_path) as yaml_file:
        yaml_as_dict = yaml.safe_load(yaml_file)

    diagram_as_dict = yaml_as_dict.get('diagram')
    diagram = YamlDiagram(**diagram_as_dict)

    with Diagram(diagram.name, show=diagram.show):
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
                if relationship.type == RelationType.LEFT:
                    resource_from_instance.__lshift__(other=resource_to_instance)

                if relationship.type == RelationType.RIGHT:
                    resource_from_instance.__rshift__(other=resource_to_instance)

                if relationship.type == RelationType.UNIDIRECTIONAL:
                    resource_from_instance.__sub__(other=resource_to_instance)

            if is_resource_from_group and is_resource_to_node:
                group_nodes = resource_from_instance.get_nodes()

                if relationship.type == RelationType.LEFT:
                    resource_to_instance.__rlshift__(other=group_nodes)

                if relationship.type == RelationType.RIGHT:
                    resource_to_instance.__rrshift__(other=group_nodes)

                if relationship.type == RelationType.UNIDIRECTIONAL:
                    resource_to_instance.__sub__(other=group_nodes)

            if is_resource_from_node and is_resource_to_group:
                group_nodes = resource_to_instance.get_nodes()

                if relationship.type == RelationType.LEFT:
                    resource_from_instance.__lshift__(other=group_nodes)

                if relationship.type == RelationType.RIGHT:
                    resource_from_instance.__rshift__(other=group_nodes)

                if relationship.type == RelationType.UNIDIRECTIONAL:
                    resource_from_instance.__sub__(other=group_nodes)


if __name__ == '__main__':
    entrypoint()
