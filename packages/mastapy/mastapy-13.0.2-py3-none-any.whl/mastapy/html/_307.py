"""HeadingType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_HEADING_TYPE = python_net_import("SMT.MastaAPI.HTML", "HeadingType")


__docformat__ = "restructuredtext en"
__all__ = ("HeadingType",)


Self = TypeVar("Self", bound="HeadingType")


class HeadingType(Enum):
    """HeadingType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _HEADING_TYPE

    VERY_SMALL = 0
    REGULAR = 1
    MEDIUM = 2
    LARGE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


HeadingType.__setattr__ = __enum_setattr
HeadingType.__delattr__ = __enum_delattr
