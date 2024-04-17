"""BearingRow"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_ROW = python_net_import("SMT.MastaAPI.Bearings", "BearingRow")


__docformat__ = "restructuredtext en"
__all__ = ("BearingRow",)


Self = TypeVar("Self", bound="BearingRow")


class BearingRow(Enum):
    """BearingRow

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_ROW

    LEFT = 0
    RIGHT = 1
    SINGLE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingRow.__setattr__ = __enum_setattr
BearingRow.__delattr__ = __enum_delattr
