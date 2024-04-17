"""TipAlterationCoefficientMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TIP_ALTERATION_COEFFICIENT_METHOD = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "TipAlterationCoefficientMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("TipAlterationCoefficientMethod",)


Self = TypeVar("Self", bound="TipAlterationCoefficientMethod")


class TipAlterationCoefficientMethod(Enum):
    """TipAlterationCoefficientMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TIP_ALTERATION_COEFFICIENT_METHOD

    USERSPECIFIED = 0
    B = 1
    C = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TipAlterationCoefficientMethod.__setattr__ = __enum_setattr
TipAlterationCoefficientMethod.__delattr__ = __enum_delattr
