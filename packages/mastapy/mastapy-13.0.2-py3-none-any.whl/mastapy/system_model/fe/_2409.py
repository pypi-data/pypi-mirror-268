"""NodeSelectionDepthOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_NODE_SELECTION_DEPTH_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "NodeSelectionDepthOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("NodeSelectionDepthOption",)


Self = TypeVar("Self", bound="NodeSelectionDepthOption")


class NodeSelectionDepthOption(Enum):
    """NodeSelectionDepthOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _NODE_SELECTION_DEPTH_OPTION

    SURFACE_NODES = 0
    SOLID_NODES = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


NodeSelectionDepthOption.__setattr__ = __enum_setattr
NodeSelectionDepthOption.__delattr__ = __enum_delattr
