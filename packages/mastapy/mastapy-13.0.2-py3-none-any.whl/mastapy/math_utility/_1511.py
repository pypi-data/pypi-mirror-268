"""DegreeOfFreedom"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_DEGREE_OF_FREEDOM = python_net_import("SMT.MastaAPI.MathUtility", "DegreeOfFreedom")


__docformat__ = "restructuredtext en"
__all__ = ("DegreeOfFreedom",)


Self = TypeVar("Self", bound="DegreeOfFreedom")


class DegreeOfFreedom(Enum):
    """DegreeOfFreedom

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _DEGREE_OF_FREEDOM

    X = 0
    Y = 1
    Z = 2
    ΘX = 3
    ΘY = 4
    ΘZ = 5


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


DegreeOfFreedom.__setattr__ = __enum_setattr
DegreeOfFreedom.__delattr__ = __enum_delattr
