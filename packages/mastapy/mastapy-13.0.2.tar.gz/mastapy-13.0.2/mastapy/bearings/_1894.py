"""JournalOilFeedType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_JOURNAL_OIL_FEED_TYPE = python_net_import(
    "SMT.MastaAPI.Bearings", "JournalOilFeedType"
)


__docformat__ = "restructuredtext en"
__all__ = ("JournalOilFeedType",)


Self = TypeVar("Self", bound="JournalOilFeedType")


class JournalOilFeedType(Enum):
    """JournalOilFeedType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _JOURNAL_OIL_FEED_TYPE

    AXIAL_GROOVE = 0
    AXIAL_HOLE = 1
    CIRCUMFERENTIAL_GROOVE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


JournalOilFeedType.__setattr__ = __enum_setattr
JournalOilFeedType.__delattr__ = __enum_delattr
