"""GearBlankFactorCalculationOptions"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GEAR_BLANK_FACTOR_CALCULATION_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "GearBlankFactorCalculationOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearBlankFactorCalculationOptions",)


Self = TypeVar("Self", bound="GearBlankFactorCalculationOptions")


class GearBlankFactorCalculationOptions(Enum):
    """GearBlankFactorCalculationOptions

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GEAR_BLANK_FACTOR_CALCULATION_OPTIONS

    AVERAGE_VALUE = 0
    MINIMUM_VALUE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GearBlankFactorCalculationOptions.__setattr__ = __enum_setattr
GearBlankFactorCalculationOptions.__delattr__ = __enum_delattr
