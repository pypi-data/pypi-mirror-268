"""FontStyle"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FONT_STYLE = python_net_import("SMT.MastaAPI.Utility.Report", "FontStyle")


__docformat__ = "restructuredtext en"
__all__ = ("FontStyle",)


Self = TypeVar("Self", bound="FontStyle")


class FontStyle(Enum):
    """FontStyle

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FONT_STYLE

    NORMAL = 0
    ITALIC = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FontStyle.__setattr__ = __enum_setattr
FontStyle.__delattr__ = __enum_delattr
