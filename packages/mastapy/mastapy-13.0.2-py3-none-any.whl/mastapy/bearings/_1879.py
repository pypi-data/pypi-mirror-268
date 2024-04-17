"""BearingCageMaterial"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_CAGE_MATERIAL = python_net_import(
    "SMT.MastaAPI.Bearings", "BearingCageMaterial"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingCageMaterial",)


Self = TypeVar("Self", bound="BearingCageMaterial")


class BearingCageMaterial(Enum):
    """BearingCageMaterial

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_CAGE_MATERIAL

    STEEL = 0
    BRASS = 1
    PLASTIC = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingCageMaterial.__setattr__ = __enum_setattr
BearingCageMaterial.__delattr__ = __enum_delattr
