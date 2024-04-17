"""UseAdvancedLTCAOptions"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_USE_ADVANCED_LTCA_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "UseAdvancedLTCAOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("UseAdvancedLTCAOptions",)


Self = TypeVar("Self", bound="UseAdvancedLTCAOptions")


class UseAdvancedLTCAOptions(Enum):
    """UseAdvancedLTCAOptions

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _USE_ADVANCED_LTCA_OPTIONS

    YES = 0
    NO = 1
    SPECIFY_FOR_EACH_MESH = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


UseAdvancedLTCAOptions.__setattr__ = __enum_setattr
UseAdvancedLTCAOptions.__delattr__ = __enum_delattr
