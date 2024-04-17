"""Axis"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_AXIS = python_net_import("SMT.MastaAPI.MathUtility", "Axis")


__docformat__ = "restructuredtext en"
__all__ = ("Axis",)


Self = TypeVar("Self", bound="Axis")


class Axis(Enum):
    """Axis

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _AXIS

    X = 0
    Y = 1
    Z = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


Axis.__setattr__ = __enum_setattr
Axis.__delattr__ = __enum_delattr
