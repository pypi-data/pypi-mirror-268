"""CylindricalGearRatingGeometryDataSource"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_RATING_GEOMETRY_DATA_SOURCE = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearRatingGeometryDataSource"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearRatingGeometryDataSource",)


Self = TypeVar("Self", bound="CylindricalGearRatingGeometryDataSource")


class CylindricalGearRatingGeometryDataSource(Enum):
    """CylindricalGearRatingGeometryDataSource

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CYLINDRICAL_GEAR_RATING_GEOMETRY_DATA_SOURCE

    BASIC_RACK = 0
    PINION_TYPE_CUTTER = 1
    MANUFACTURING_CONFIGURATION = 2
    ROUGH_MANUFACTURING_CONFIGURATION = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CylindricalGearRatingGeometryDataSource.__setattr__ = __enum_setattr
CylindricalGearRatingGeometryDataSource.__delattr__ = __enum_delattr
