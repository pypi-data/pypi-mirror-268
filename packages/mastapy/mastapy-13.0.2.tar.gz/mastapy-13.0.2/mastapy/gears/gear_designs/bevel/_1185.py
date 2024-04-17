"""AGMAGleasonConicalGearGeometryMethods"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_GEOMETRY_METHODS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Bevel", "AGMAGleasonConicalGearGeometryMethods"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearGeometryMethods",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearGeometryMethods")


class AGMAGleasonConicalGearGeometryMethods(Enum):
    """AGMAGleasonConicalGearGeometryMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _AGMA_GLEASON_CONICAL_GEAR_GEOMETRY_METHODS

    GLEASON = 0
    AGMA_2005D03 = 1
    GLEASON_CAGE = 2
    GLEASON_GEMS = 3
    KIMOS = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AGMAGleasonConicalGearGeometryMethods.__setattr__ = __enum_setattr
AGMAGleasonConicalGearGeometryMethods.__delattr__ = __enum_delattr
