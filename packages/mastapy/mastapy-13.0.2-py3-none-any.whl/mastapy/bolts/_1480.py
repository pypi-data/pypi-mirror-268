"""BoltShankType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BOLT_SHANK_TYPE = python_net_import("SMT.MastaAPI.Bolts", "BoltShankType")


__docformat__ = "restructuredtext en"
__all__ = ("BoltShankType",)


Self = TypeVar("Self", bound="BoltShankType")


class BoltShankType(Enum):
    """BoltShankType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BOLT_SHANK_TYPE

    SHANKED = 0
    NECKED_DOWN = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BoltShankType.__setattr__ = __enum_setattr
BoltShankType.__delattr__ = __enum_delattr
