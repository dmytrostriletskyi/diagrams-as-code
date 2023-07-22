"""
Provide implementation of enums.
"""
from enum import Enum


class ServiceResourceType(Enum):
    """
    Service resource type enum implementation.
    """

    CLUSTER = 'cluster'
    GROUP = 'group'


class RelationType(str, Enum):
    """
    Relation type enum implementation.
    """

    LEFT = 'left'
    RIGHT = 'right'
    UNIDIRECTIONAL = 'unidirectional'
    BOTH = 'both'
