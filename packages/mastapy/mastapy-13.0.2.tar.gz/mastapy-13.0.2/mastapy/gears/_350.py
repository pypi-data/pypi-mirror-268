"""SpiralBevelRootLineTilt"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_ROOT_LINE_TILT = python_net_import(
    "SMT.MastaAPI.Gears", "SpiralBevelRootLineTilt"
)


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelRootLineTilt",)


Self = TypeVar("Self", bound="SpiralBevelRootLineTilt")


class SpiralBevelRootLineTilt(Enum):
    """SpiralBevelRootLineTilt

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SPIRAL_BEVEL_ROOT_LINE_TILT

    ABOUT_MEAN_POINT = 0
    ABOUT_LARGE_END = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SpiralBevelRootLineTilt.__setattr__ = __enum_setattr
SpiralBevelRootLineTilt.__delattr__ = __enum_delattr
