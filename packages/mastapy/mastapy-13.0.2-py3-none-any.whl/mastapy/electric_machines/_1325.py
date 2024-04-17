"""WindingType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_WINDING_TYPE = python_net_import("SMT.MastaAPI.ElectricMachines", "WindingType")


__docformat__ = "restructuredtext en"
__all__ = ("WindingType",)


Self = TypeVar("Self", bound="WindingType")


class WindingType(Enum):
    """WindingType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _WINDING_TYPE

    ROUND_CONDUCTORS = 0
    HAIRPIN = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


WindingType.__setattr__ = __enum_setattr
WindingType.__delattr__ = __enum_delattr
