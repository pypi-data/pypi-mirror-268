"""RelativeOffsetOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_RELATIVE_OFFSET_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel", "RelativeOffsetOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("RelativeOffsetOption",)


Self = TypeVar("Self", bound="RelativeOffsetOption")


class RelativeOffsetOption(Enum):
    """RelativeOffsetOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _RELATIVE_OFFSET_OPTION

    LEFT = 0
    CENTRE = 1
    RIGHT = 2
    SPECIFIED = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RelativeOffsetOption.__setattr__ = __enum_setattr
RelativeOffsetOption.__delattr__ = __enum_delattr
