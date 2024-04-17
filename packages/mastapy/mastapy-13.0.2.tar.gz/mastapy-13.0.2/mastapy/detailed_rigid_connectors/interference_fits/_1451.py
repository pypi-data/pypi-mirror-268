"""CalculationMethods"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CALCULATION_METHODS = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits", "CalculationMethods"
)


__docformat__ = "restructuredtext en"
__all__ = ("CalculationMethods",)


Self = TypeVar("Self", bound="CalculationMethods")


class CalculationMethods(Enum):
    """CalculationMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CALCULATION_METHODS

    SPECIFY_PRESSURE = 0
    SPECIFY_INTERFERENCE = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CalculationMethods.__setattr__ = __enum_setattr
CalculationMethods.__delattr__ = __enum_delattr
