"""ManufactureRating"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MANUFACTURE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "ManufactureRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("ManufactureRating",)


Self = TypeVar("Self", bound="ManufactureRating")


class ManufactureRating(Enum):
    """ManufactureRating

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MANUFACTURE_RATING

    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ManufactureRating.__setattr__ = __enum_setattr
ManufactureRating.__delattr__ = __enum_delattr
