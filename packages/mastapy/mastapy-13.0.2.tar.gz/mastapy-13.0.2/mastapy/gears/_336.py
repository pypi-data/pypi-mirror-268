"""Hand"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_HAND = python_net_import("SMT.MastaAPI.Gears", "Hand")


__docformat__ = "restructuredtext en"
__all__ = ("Hand",)


Self = TypeVar("Self", bound="Hand")


class Hand(Enum):
    """Hand

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _HAND

    LEFT = 0
    RIGHT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


Hand.__setattr__ = __enum_setattr
Hand.__delattr__ = __enum_delattr
