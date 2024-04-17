"""ExtrapolationOptions"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_EXTRAPOLATION_OPTIONS = python_net_import(
    "SMT.MastaAPI.MathUtility", "ExtrapolationOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("ExtrapolationOptions",)


Self = TypeVar("Self", bound="ExtrapolationOptions")


class ExtrapolationOptions(Enum):
    """ExtrapolationOptions

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _EXTRAPOLATION_OPTIONS

    FLAT = 0
    LINEAR = 1
    THROW_EXCEPTION = 2
    WRAP = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ExtrapolationOptions.__setattr__ = __enum_setattr
ExtrapolationOptions.__delattr__ = __enum_delattr
