"""
Provide implementation of enums.
"""
from enum import Enum


class ServiceResourceType(Enum):
    """
    Service resource type enum implementation.
    """

    CLUSTER = 'diagrams.cluster'
    GROUP = 'diagrams.group'
