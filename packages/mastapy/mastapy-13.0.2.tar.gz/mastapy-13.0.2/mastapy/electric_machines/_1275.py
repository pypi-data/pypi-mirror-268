"""FillFactorSpecificationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FILL_FACTOR_SPECIFICATION_METHOD = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "FillFactorSpecificationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("FillFactorSpecificationMethod",)


Self = TypeVar("Self", bound="FillFactorSpecificationMethod")


class FillFactorSpecificationMethod(Enum):
    """FillFactorSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FILL_FACTOR_SPECIFICATION_METHOD

    CALCULATED_FROM_WIRE_DIMENSIONS = 0
    SPECIFIED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FillFactorSpecificationMethod.__setattr__ = __enum_setattr
FillFactorSpecificationMethod.__delattr__ = __enum_delattr
