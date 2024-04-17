"""FatigueLoadLimitCalculationMethodEnum"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FATIGUE_LOAD_LIMIT_CALCULATION_METHOD_ENUM = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling",
    "FatigueLoadLimitCalculationMethodEnum",
)


__docformat__ = "restructuredtext en"
__all__ = ("FatigueLoadLimitCalculationMethodEnum",)


Self = TypeVar("Self", bound="FatigueLoadLimitCalculationMethodEnum")


class FatigueLoadLimitCalculationMethodEnum(Enum):
    """FatigueLoadLimitCalculationMethodEnum

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FATIGUE_LOAD_LIMIT_CALCULATION_METHOD_ENUM

    BASIC = 0
    ADVANCED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FatigueLoadLimitCalculationMethodEnum.__setattr__ = __enum_setattr
FatigueLoadLimitCalculationMethodEnum.__delattr__ = __enum_delattr
