"""RegionID"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_REGION_ID = python_net_import("SMT.MastaAPI.ElectricMachines", "RegionID")


__docformat__ = "restructuredtext en"
__all__ = ("RegionID",)


Self = TypeVar("Self", bound="RegionID")


class RegionID(Enum):
    """RegionID

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _REGION_ID

    STATOR_CORE = 0
    STATOR_SLOT = 1
    STATOR_WEDGE = 2
    REGION_BETWEEN_WEDGE_AND_AIR_GAP = 3
    AIR_GAP_STATOR_SIDE = 4
    STATOR_CUTOUTS = 5
    ROTOR_CORE = 6
    ROTOR_AIR_REGION = 7
    MAGNET = 8
    AIR_GAP_ROTOR_SIDE = 9
    SHAFT = 10
    CONDUCTOR = 11


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RegionID.__setattr__ = __enum_setattr
RegionID.__delattr__ = __enum_delattr
