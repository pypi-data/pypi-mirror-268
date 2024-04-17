"""StatusItemSeverity"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_STATUS_ITEM_SEVERITY = python_net_import(
    "SMT.MastaAPI.Utility.ModelValidation", "StatusItemSeverity"
)


__docformat__ = "restructuredtext en"
__all__ = ("StatusItemSeverity",)


Self = TypeVar("Self", bound="StatusItemSeverity")


class StatusItemSeverity(Enum):
    """StatusItemSeverity

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _STATUS_ITEM_SEVERITY

    HEADER = 1
    INFORMATION = 16
    WARNING = 256
    ERROR = 4096


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


StatusItemSeverity.__setattr__ = __enum_setattr
StatusItemSeverity.__delattr__ = __enum_delattr
