"""BearingNodeOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_NODE_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "BearingNodeOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingNodeOption",)


Self = TypeVar("Self", bound="BearingNodeOption")


class BearingNodeOption(Enum):
    """BearingNodeOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_NODE_OPTION

    SINGLE_NODE_FOR_BEARING = 0
    NODE_PER_BEARING_ROW = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingNodeOption.__setattr__ = __enum_setattr
BearingNodeOption.__delattr__ = __enum_delattr
