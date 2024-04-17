"""PlanetPinManufacturingErrorsCoordinateSystem"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_PLANET_PIN_MANUFACTURING_ERRORS_COORDINATE_SYSTEM = python_net_import(
    "SMT.MastaAPI.SystemModel", "PlanetPinManufacturingErrorsCoordinateSystem"
)


__docformat__ = "restructuredtext en"
__all__ = ("PlanetPinManufacturingErrorsCoordinateSystem",)


Self = TypeVar("Self", bound="PlanetPinManufacturingErrorsCoordinateSystem")


class PlanetPinManufacturingErrorsCoordinateSystem(Enum):
    """PlanetPinManufacturingErrorsCoordinateSystem

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _PLANET_PIN_MANUFACTURING_ERRORS_COORDINATE_SYSTEM

    RADIAL_AND_ANGULAR_IN_PLANET_CARRIER_SYSTEM = 0
    X_AND_Y_IN_PLANET_CARRIER_SYSTEM = 1
    RADIAL_AND_TANGENTIAL_IN_PIN_SYSTEM = 2
    RADIAL_AND_ANGULAR_IN_PIN_SYSTEM = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


PlanetPinManufacturingErrorsCoordinateSystem.__setattr__ = __enum_setattr
PlanetPinManufacturingErrorsCoordinateSystem.__delattr__ = __enum_delattr
