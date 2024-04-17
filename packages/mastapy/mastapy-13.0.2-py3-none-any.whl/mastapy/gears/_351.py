"""SpiralBevelToothTaper"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_TOOTH_TAPER = python_net_import(
    "SMT.MastaAPI.Gears", "SpiralBevelToothTaper"
)


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelToothTaper",)


Self = TypeVar("Self", bound="SpiralBevelToothTaper")


class SpiralBevelToothTaper(Enum):
    """SpiralBevelToothTaper

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SPIRAL_BEVEL_TOOTH_TAPER

    DUPLEX_DPLX = 0
    STANDARD_STD = 1
    TILTED_ROOT_LINE_TRL = 2
    USERSPECIFIED = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SpiralBevelToothTaper.__setattr__ = __enum_setattr
SpiralBevelToothTaper.__delattr__ = __enum_delattr
