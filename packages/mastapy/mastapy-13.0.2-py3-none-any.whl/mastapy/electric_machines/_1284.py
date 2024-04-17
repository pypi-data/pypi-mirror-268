"""MagnetClearance"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MAGNET_CLEARANCE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "MagnetClearance"
)


__docformat__ = "restructuredtext en"
__all__ = ("MagnetClearance",)


Self = TypeVar("Self", bound="MagnetClearance")


class MagnetClearance(Enum):
    """MagnetClearance

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MAGNET_CLEARANCE

    INSIDE = 0
    OUTSIDE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MagnetClearance.__setattr__ = __enum_setattr
MagnetClearance.__delattr__ = __enum_delattr
