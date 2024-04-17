"""SingleOrDoubleLayerWindings"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SINGLE_OR_DOUBLE_LAYER_WINDINGS = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "SingleOrDoubleLayerWindings"
)


__docformat__ = "restructuredtext en"
__all__ = ("SingleOrDoubleLayerWindings",)


Self = TypeVar("Self", bound="SingleOrDoubleLayerWindings")


class SingleOrDoubleLayerWindings(Enum):
    """SingleOrDoubleLayerWindings

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SINGLE_OR_DOUBLE_LAYER_WINDINGS

    SINGLE_LAYER = 0
    DOUBLE_LAYER = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SingleOrDoubleLayerWindings.__setattr__ = __enum_setattr
SingleOrDoubleLayerWindings.__delattr__ = __enum_delattr
