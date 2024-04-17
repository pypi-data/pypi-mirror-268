"""HeightSeries"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_HEIGHT_SERIES = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "HeightSeries"
)


__docformat__ = "restructuredtext en"
__all__ = ("HeightSeries",)


Self = TypeVar("Self", bound="HeightSeries")


class HeightSeries(Enum):
    """HeightSeries

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _HEIGHT_SERIES

    _1 = 1
    _7 = 7
    _9 = 9


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


HeightSeries.__setattr__ = __enum_setattr
HeightSeries.__delattr__ = __enum_delattr
