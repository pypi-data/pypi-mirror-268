"""MagnetisationDirection"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MAGNETISATION_DIRECTION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "MagnetisationDirection"
)


__docformat__ = "restructuredtext en"
__all__ = ("MagnetisationDirection",)


Self = TypeVar("Self", bound="MagnetisationDirection")


class MagnetisationDirection(Enum):
    """MagnetisationDirection

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MAGNETISATION_DIRECTION

    AS_CALCULATED = 0
    PLUS_90_FROM_CALCULATED = 1
    MINUS_90_FROM_CALCULATED = 2
    PLUS_180_FROM_CALCULATED = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MagnetisationDirection.__setattr__ = __enum_setattr
MagnetisationDirection.__delattr__ = __enum_delattr
