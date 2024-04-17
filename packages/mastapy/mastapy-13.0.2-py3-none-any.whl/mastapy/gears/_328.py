"""DeflectionFromBendingOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_DEFLECTION_FROM_BENDING_OPTION = python_net_import(
    "SMT.MastaAPI.Gears", "DeflectionFromBendingOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("DeflectionFromBendingOption",)


Self = TypeVar("Self", bound="DeflectionFromBendingOption")


class DeflectionFromBendingOption(Enum):
    """DeflectionFromBendingOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _DEFLECTION_FROM_BENDING_OPTION

    ACCURATE_CALCULATION = 0
    BASIC_TOTAL_SINGLE_TOOTH_STIFFNESS_IS_14_NUM_MM_AS_SUGGESTED_BY_ISO = 1
    ESTIMATED_FROM_FE_MODEL = 2
    NONE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


DeflectionFromBendingOption.__setattr__ = __enum_setattr
DeflectionFromBendingOption.__delattr__ = __enum_delattr
