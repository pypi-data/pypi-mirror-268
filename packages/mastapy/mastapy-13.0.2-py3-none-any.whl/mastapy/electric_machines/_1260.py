"""CoilPositionInSlot"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_COIL_POSITION_IN_SLOT = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "CoilPositionInSlot"
)


__docformat__ = "restructuredtext en"
__all__ = ("CoilPositionInSlot",)


Self = TypeVar("Self", bound="CoilPositionInSlot")


class CoilPositionInSlot(Enum):
    """CoilPositionInSlot

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _COIL_POSITION_IN_SLOT

    CENTRE = 0
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CoilPositionInSlot.__setattr__ = __enum_setattr
CoilPositionInSlot.__delattr__ = __enum_delattr
