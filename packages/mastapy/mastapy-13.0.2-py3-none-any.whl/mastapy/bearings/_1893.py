"""JournalBearingType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_JOURNAL_BEARING_TYPE = python_net_import("SMT.MastaAPI.Bearings", "JournalBearingType")


__docformat__ = "restructuredtext en"
__all__ = ("JournalBearingType",)


Self = TypeVar("Self", bound="JournalBearingType")


class JournalBearingType(Enum):
    """JournalBearingType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _JOURNAL_BEARING_TYPE

    PLAIN_OIL_FED = 0
    PLAIN_GREASE_FILLED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


JournalBearingType.__setattr__ = __enum_setattr
JournalBearingType.__delattr__ = __enum_delattr
