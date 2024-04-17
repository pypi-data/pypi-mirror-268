"""AGMAHardeningType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_AGMA_HARDENING_TYPE = python_net_import("SMT.MastaAPI.Shafts", "AGMAHardeningType")


__docformat__ = "restructuredtext en"
__all__ = ("AGMAHardeningType",)


Self = TypeVar("Self", bound="AGMAHardeningType")


class AGMAHardeningType(Enum):
    """AGMAHardeningType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _AGMA_HARDENING_TYPE

    DUCTILE_THROUGH_HARDENED_STEEL = 0
    SURFACE_HARDENED_STEEL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AGMAHardeningType.__setattr__ = __enum_setattr
AGMAHardeningType.__delattr__ = __enum_delattr
