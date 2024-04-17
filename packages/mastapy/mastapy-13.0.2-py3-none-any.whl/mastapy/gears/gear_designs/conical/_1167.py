"""CutterBladeType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CUTTER_BLADE_TYPE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "CutterBladeType"
)


__docformat__ = "restructuredtext en"
__all__ = ("CutterBladeType",)


Self = TypeVar("Self", bound="CutterBladeType")


class CutterBladeType(Enum):
    """CutterBladeType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CUTTER_BLADE_TYPE

    STRAIGHT = 0
    CIRCULAR_ARC = 1
    PARABOLIC = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CutterBladeType.__setattr__ = __enum_setattr
CutterBladeType.__delattr__ = __enum_delattr
