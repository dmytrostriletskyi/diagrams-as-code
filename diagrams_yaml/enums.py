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


class DiagramDirection(str, Enum):
    """
    Diagram direction enum implementation.
    """

    LEFT_TO_RIGHT = 'left-to-right'
    RIGHT_TO_LEFT = 'right-to-left'
    TOP_TO_BOTTOM = 'top-to-bottom'
    BOTTOM_TO_TOP = 'bottom-to-top'

    @property
    def mapped(self):
        """
        References:
            - https://github.com/mingrammer/diagrams/blob/b19b09761db6f0037fd76e527b9ce6918fbdfcfc/diagrams/__init__.py#L41
        :return:
        """
        match self.value:
            case self.LEFT_TO_RIGHT:
                return 'LR'
            case self.RIGHT_TO_LEFT:
                return 'RL'
            case self.TOP_TO_BOTTOM:
                return 'TB'
            case self.BOTTOM_TO_TOP:
                return 'BT'


class DiagramFormat(str, Enum):
    """
    Diagram format enum implementation.
    """

    PNG = 'png'
    JPG = 'jpg'
    SVG = 'svg'
    PDF = 'pdf'
    DOT = 'dot'
