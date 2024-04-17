"""IronLossCoefficientSpecificationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_IRON_LOSS_COEFFICIENT_SPECIFICATION_METHOD = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "IronLossCoefficientSpecificationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("IronLossCoefficientSpecificationMethod",)


Self = TypeVar("Self", bound="IronLossCoefficientSpecificationMethod")


class IronLossCoefficientSpecificationMethod(Enum):
    """IronLossCoefficientSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _IRON_LOSS_COEFFICIENT_SPECIFICATION_METHOD

    SPECIFIED = 0
    OBTAINED_FROM_LOSS_CURVES = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


IronLossCoefficientSpecificationMethod.__setattr__ = __enum_setattr
IronLossCoefficientSpecificationMethod.__delattr__ = __enum_delattr
