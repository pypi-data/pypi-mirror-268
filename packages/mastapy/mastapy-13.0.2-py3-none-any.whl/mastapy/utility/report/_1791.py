"""FontWeight"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FONT_WEIGHT = python_net_import("SMT.MastaAPI.Utility.Report", "FontWeight")


__docformat__ = "restructuredtext en"
__all__ = ("FontWeight",)


Self = TypeVar("Self", bound="FontWeight")


class FontWeight(Enum):
    """FontWeight

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FONT_WEIGHT

    NORMAL = 0
    BOLD = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FontWeight.__setattr__ = __enum_setattr
FontWeight.__delattr__ = __enum_delattr
