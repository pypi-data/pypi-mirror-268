"""HeadingSize"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_HEADING_SIZE = python_net_import("SMT.MastaAPI.Utility.Report", "HeadingSize")


__docformat__ = "restructuredtext en"
__all__ = ("HeadingSize",)


Self = TypeVar("Self", bound="HeadingSize")


class HeadingSize(Enum):
    """HeadingSize

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _HEADING_SIZE

    REGULAR = 0
    MEDIUM = 1
    LARGE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


HeadingSize.__setattr__ = __enum_setattr
HeadingSize.__delattr__ = __enum_delattr
