"""BearingNodeAlignmentOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_NODE_ALIGNMENT_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "BearingNodeAlignmentOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingNodeAlignmentOption",)


Self = TypeVar("Self", bound="BearingNodeAlignmentOption")


class BearingNodeAlignmentOption(Enum):
    """BearingNodeAlignmentOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_NODE_ALIGNMENT_OPTION

    CENTRE_OF_BEARING = 0
    CENTRE_OF_RACE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingNodeAlignmentOption.__setattr__ = __enum_setattr
BearingNodeAlignmentOption.__delattr__ = __enum_delattr
