"""MicropittingCoefficientOfFrictionCalculationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MICROPITTING_COEFFICIENT_OF_FRICTION_CALCULATION_METHOD = python_net_import(
    "SMT.MastaAPI.Gears", "MicropittingCoefficientOfFrictionCalculationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("MicropittingCoefficientOfFrictionCalculationMethod",)


Self = TypeVar("Self", bound="MicropittingCoefficientOfFrictionCalculationMethod")


class MicropittingCoefficientOfFrictionCalculationMethod(Enum):
    """MicropittingCoefficientOfFrictionCalculationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MICROPITTING_COEFFICIENT_OF_FRICTION_CALCULATION_METHOD

    CALCULATED_CONSTANT = 0
    VARIABLE_BENEDICT_AND_KELLEY = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MicropittingCoefficientOfFrictionCalculationMethod.__setattr__ = __enum_setattr
MicropittingCoefficientOfFrictionCalculationMethod.__delattr__ = __enum_delattr
