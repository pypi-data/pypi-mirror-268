"""WireSizeSpecificationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_WIRE_SIZE_SPECIFICATION_METHOD = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "WireSizeSpecificationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("WireSizeSpecificationMethod",)


Self = TypeVar("Self", bound="WireSizeSpecificationMethod")


class WireSizeSpecificationMethod(Enum):
    """WireSizeSpecificationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _WIRE_SIZE_SPECIFICATION_METHOD

    AWG = 0
    IEC_60228 = 1
    USERSPECIFIED = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


WireSizeSpecificationMethod.__setattr__ = __enum_setattr
WireSizeSpecificationMethod.__delattr__ = __enum_delattr
