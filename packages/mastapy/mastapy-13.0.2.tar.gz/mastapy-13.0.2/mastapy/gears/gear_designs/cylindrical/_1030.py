"""CylindricalGearProfileMeasurementType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PROFILE_MEASUREMENT_TYPE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CylindricalGearProfileMeasurementType",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearProfileMeasurementType",)


Self = TypeVar("Self", bound="CylindricalGearProfileMeasurementType")


class CylindricalGearProfileMeasurementType(Enum):
    """CylindricalGearProfileMeasurementType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CYLINDRICAL_GEAR_PROFILE_MEASUREMENT_TYPE

    DIAMETER = 0
    RADIUS = 1
    ROLL_ANGLE = 2
    ROLL_DISTANCE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CylindricalGearProfileMeasurementType.__setattr__ = __enum_setattr
CylindricalGearProfileMeasurementType.__delattr__ = __enum_delattr
