"""StrengthGrades"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_STRENGTH_GRADES = python_net_import("SMT.MastaAPI.Bolts", "StrengthGrades")


__docformat__ = "restructuredtext en"
__all__ = ("StrengthGrades",)


Self = TypeVar("Self", bound="StrengthGrades")


class StrengthGrades(Enum):
    """StrengthGrades

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _STRENGTH_GRADES

    _129 = 0
    _109 = 1
    _88 = 2
    OTHER = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


StrengthGrades.__setattr__ = __enum_setattr
StrengthGrades.__delattr__ = __enum_delattr
