"""CoolingDuctShape"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_COOLING_DUCT_SHAPE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "CoolingDuctShape"
)


__docformat__ = "restructuredtext en"
__all__ = ("CoolingDuctShape",)


Self = TypeVar("Self", bound="CoolingDuctShape")


class CoolingDuctShape(Enum):
    """CoolingDuctShape

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _COOLING_DUCT_SHAPE

    CIRCULAR = 0
    ELLIPSE = 1
    RECTANGULAR = 2
    TYPE_1 = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


CoolingDuctShape.__setattr__ = __enum_setattr
CoolingDuctShape.__delattr__ = __enum_delattr
