"""
Provide implementation of resources.
"""


class DiagramGroup:
    """
    Diagram group resource implementation.

    Is used to collect a list of `diagrams` resources to pack them as a list for further relationships.
    """

    def __init__(self):
        """
        Construct the object.
        """
        self.nodes = []

    def add_node(self, node):
        """
        Add a node.
        """
        self.nodes.append(node)

    def get_nodes(self):
        """
        Get nodes.
        """
        return self.nodes

    def __repr__(self):
        """
        Get object representation.
        """
        representation = ''

        for node in self.nodes:
            representation += f' {node},'

        return '<Group: [' + representation[1:-1] + ']>'
