"""LubricantViscosityClassAGMA"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_LUBRICANT_VISCOSITY_CLASS_AGMA = python_net_import(
    "SMT.MastaAPI.Materials", "LubricantViscosityClassAGMA"
)


__docformat__ = "restructuredtext en"
__all__ = ("LubricantViscosityClassAGMA",)


Self = TypeVar("Self", bound="LubricantViscosityClassAGMA")


class LubricantViscosityClassAGMA(Enum):
    """LubricantViscosityClassAGMA

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _LUBRICANT_VISCOSITY_CLASS_AGMA

    AGMA_1 = 46
    AGMA_2 = 68
    AGMA_3 = 100
    AGMA_4 = 150
    AGMA_5 = 220
    AGMA_6 = 320
    AGMA_7 = 460
    AGMA_8 = 680
    AGMA_8A = 1000


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


LubricantViscosityClassAGMA.__setattr__ = __enum_setattr
LubricantViscosityClassAGMA.__delattr__ = __enum_delattr
