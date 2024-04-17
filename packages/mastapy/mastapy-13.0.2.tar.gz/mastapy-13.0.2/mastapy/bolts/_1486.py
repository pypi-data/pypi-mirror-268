"""HeadCapTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_HEAD_CAP_TYPES = python_net_import("SMT.MastaAPI.Bolts", "HeadCapTypes")


__docformat__ = "restructuredtext en"
__all__ = ("HeadCapTypes",)


Self = TypeVar("Self", bound="HeadCapTypes")


class HeadCapTypes(Enum):
    """HeadCapTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _HEAD_CAP_TYPES

    HEXAGONAL_HEAD = 0
    SOCKET_HEAD = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


HeadCapTypes.__setattr__ = __enum_setattr
HeadCapTypes.__delattr__ = __enum_delattr
