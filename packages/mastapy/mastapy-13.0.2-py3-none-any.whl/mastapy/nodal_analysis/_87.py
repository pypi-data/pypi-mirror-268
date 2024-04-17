"""SectionEnd"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SECTION_END = python_net_import("SMT.MastaAPI.NodalAnalysis", "SectionEnd")


__docformat__ = "restructuredtext en"
__all__ = ("SectionEnd",)


Self = TypeVar("Self", bound="SectionEnd")


class SectionEnd(Enum):
    """SectionEnd

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SECTION_END

    LEFT = 0
    RIGHT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SectionEnd.__setattr__ = __enum_setattr
SectionEnd.__delattr__ = __enum_delattr
