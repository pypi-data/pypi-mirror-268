"""DrawDefiningGearOrBoth"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_DRAW_DEFINING_GEAR_OR_BOTH = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry", "DrawDefiningGearOrBoth"
)


__docformat__ = "restructuredtext en"
__all__ = ("DrawDefiningGearOrBoth",)


Self = TypeVar("Self", bound="DrawDefiningGearOrBoth")


class DrawDefiningGearOrBoth(Enum):
    """DrawDefiningGearOrBoth

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _DRAW_DEFINING_GEAR_OR_BOTH

    DEFINING_GEAR = 0
    BOTH = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


DrawDefiningGearOrBoth.__setattr__ = __enum_setattr
DrawDefiningGearOrBoth.__delattr__ = __enum_delattr
