"""TopremEntryType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TOPREM_ENTRY_TYPE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "TopremEntryType"
)


__docformat__ = "restructuredtext en"
__all__ = ("TopremEntryType",)


Self = TypeVar("Self", bound="TopremEntryType")


class TopremEntryType(Enum):
    """TopremEntryType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TOPREM_ENTRY_TYPE

    TOPREM_LETTER = 0
    VALUES = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TopremEntryType.__setattr__ = __enum_setattr
TopremEntryType.__delattr__ = __enum_delattr
