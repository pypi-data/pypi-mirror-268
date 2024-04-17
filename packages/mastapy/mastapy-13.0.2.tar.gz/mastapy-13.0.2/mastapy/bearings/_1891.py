"""FluidFilmTemperatureOptions"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FLUID_FILM_TEMPERATURE_OPTIONS = python_net_import(
    "SMT.MastaAPI.Bearings", "FluidFilmTemperatureOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("FluidFilmTemperatureOptions",)


Self = TypeVar("Self", bound="FluidFilmTemperatureOptions")


class FluidFilmTemperatureOptions(Enum):
    """FluidFilmTemperatureOptions

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FLUID_FILM_TEMPERATURE_OPTIONS

    CALCULATE_USING_DIN_7322010_WHERE_AVAILABLE = 0
    CALCULATE_FROM_SPECIFIED_ELEMENT_AND_RING_TEMPERATURES = 1
    USE_SPECIFIED_ELEMENT_TEMPERATURE = 2
    USE_SPECIFIED_SUMP_TEMPERATURE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FluidFilmTemperatureOptions.__setattr__ = __enum_setattr
FluidFilmTemperatureOptions.__delattr__ = __enum_delattr
