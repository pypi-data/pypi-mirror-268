"""GeneralLoadFactorCalculationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GENERAL_LOAD_FACTOR_CALCULATION_METHOD = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "GeneralLoadFactorCalculationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("GeneralLoadFactorCalculationMethod",)


Self = TypeVar("Self", bound="GeneralLoadFactorCalculationMethod")


class GeneralLoadFactorCalculationMethod(Enum):
    """GeneralLoadFactorCalculationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GENERAL_LOAD_FACTOR_CALCULATION_METHOD

    METHOD_B = 0
    METHOD_C = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GeneralLoadFactorCalculationMethod.__setattr__ = __enum_setattr
GeneralLoadFactorCalculationMethod.__delattr__ = __enum_delattr
