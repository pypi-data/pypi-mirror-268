"""BoltTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BOLT_TYPES = python_net_import("SMT.MastaAPI.Bolts", "BoltTypes")


__docformat__ = "restructuredtext en"
__all__ = ("BoltTypes",)


Self = TypeVar("Self", bound="BoltTypes")


class BoltTypes(Enum):
    """BoltTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BOLT_TYPES

    THROUGH_BOLTED_JOINT = 0
    TAPPED_THREAD_JOINT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BoltTypes.__setattr__ = __enum_setattr
BoltTypes.__delattr__ = __enum_delattr
