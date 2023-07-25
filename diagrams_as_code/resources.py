"""
Provide implementation of resources.
"""
from diagrams import Node


class DiagramGroup:
    """
    Diagram group resource implementation.

    Is used to collect a list of `diagrams` resources to pack them as a list for further relationships.
    """

    def __init__(self: 'DiagramGroup') -> None:
        """
        Construct the object.
        """
        self.nodes = []

    def add_node(self: 'DiagramGroup', node: Node) -> None:
        """
        Add a node.

        Arguments:
            node (Node): a node.
        """
        self.nodes.append(node)

    def get_nodes(self: 'DiagramGroup') -> list[Node]:
        """
        Get nodes.

        Returns:
            A list of nodes as a list of `Node`.
        """
        return self.nodes

    def __repr__(self: 'DiagramGroup') -> str:
        """
        Get the group's representation.

        Returns:
            The group's representation as a string.
        """
        representation = ''

        for node in self.nodes:
            representation += f' {node},'

        return '<Group: [' + representation[1:-1] + ']>'
