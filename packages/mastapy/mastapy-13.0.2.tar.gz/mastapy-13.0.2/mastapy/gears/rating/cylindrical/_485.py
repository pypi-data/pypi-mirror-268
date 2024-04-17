"""ScuffingIntegralTemperatureRatingMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SCUFFING_INTEGRAL_TEMPERATURE_RATING_METHOD = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "ScuffingIntegralTemperatureRatingMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("ScuffingIntegralTemperatureRatingMethod",)


Self = TypeVar("Self", bound="ScuffingIntegralTemperatureRatingMethod")


class ScuffingIntegralTemperatureRatingMethod(Enum):
    """ScuffingIntegralTemperatureRatingMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SCUFFING_INTEGRAL_TEMPERATURE_RATING_METHOD

    ISOTR_1398922000 = 0
    ISOTS_6336212017 = 1
    ISOTS_6336212022 = 2
    DIN_399041987 = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ScuffingIntegralTemperatureRatingMethod.__setattr__ = __enum_setattr
ScuffingIntegralTemperatureRatingMethod.__delattr__ = __enum_delattr
