"""WindingConnection"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_WINDING_CONNECTION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "WindingConnection"
)


__docformat__ = "restructuredtext en"
__all__ = ("WindingConnection",)


Self = TypeVar("Self", bound="WindingConnection")


class WindingConnection(Enum):
    """WindingConnection

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _WINDING_CONNECTION

    STAR_CONNECTION = 0
    DELTA_CONNECTION = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


WindingConnection.__setattr__ = __enum_setattr
WindingConnection.__delattr__ = __enum_delattr
