"""ModeInputType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MODE_INPUT_TYPE = python_net_import("SMT.MastaAPI.NodalAnalysis", "ModeInputType")


__docformat__ = "restructuredtext en"
__all__ = ("ModeInputType",)


Self = TypeVar("Self", bound="ModeInputType")


class ModeInputType(Enum):
    """ModeInputType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MODE_INPUT_TYPE

    NO_MODES = 0
    ALL_IN_RANGE = 1
    LOWEST_IN_RANGE = 2
    NEAREST_TO_SHIFT = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ModeInputType.__setattr__ = __enum_setattr
ModeInputType.__delattr__ = __enum_delattr
