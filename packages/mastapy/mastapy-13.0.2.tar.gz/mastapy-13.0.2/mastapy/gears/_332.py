"""GearSetModes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GEAR_SET_MODES = python_net_import("SMT.MastaAPI.Gears", "GearSetModes")


__docformat__ = "restructuredtext en"
__all__ = ("GearSetModes",)


Self = TypeVar("Self", bound="GearSetModes")


class GearSetModes(Enum):
    """GearSetModes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GEAR_SET_MODES

    DESIGN = 0
    MICRO_GEOMETRY = 1
    MICRO_GEOMETRY_ADVANCED_LTCA = 2
    CYLINDRICAL_MANUFACTURING_POWER_FLOW = 3
    CYLINDRICAL_MANUFACTURING_SYSTEM_DEFLECTION = 4
    BEVEL_MANUFACTURING = 5
    BEVEL_LTCA = 6


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GearSetModes.__setattr__ = __enum_setattr
GearSetModes.__delattr__ = __enum_delattr
