"""ThreadTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_THREAD_TYPES = python_net_import("SMT.MastaAPI.Bolts", "ThreadTypes")


__docformat__ = "restructuredtext en"
__all__ = ("ThreadTypes",)


Self = TypeVar("Self", bound="ThreadTypes")


class ThreadTypes(Enum):
    """ThreadTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _THREAD_TYPES

    METRIC_STANDARD_THREAD = 0
    METRIC_FINE_THREAD = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ThreadTypes.__setattr__ = __enum_setattr
ThreadTypes.__delattr__ = __enum_delattr
