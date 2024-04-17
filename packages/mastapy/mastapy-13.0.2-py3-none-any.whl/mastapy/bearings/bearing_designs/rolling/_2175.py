"""SleeveType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SLEEVE_TYPE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "SleeveType"
)


__docformat__ = "restructuredtext en"
__all__ = ("SleeveType",)


Self = TypeVar("Self", bound="SleeveType")


class SleeveType(Enum):
    """SleeveType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SLEEVE_TYPE

    NONE = 0
    WITHDRAWAL = 1
    ADAPTER = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


SleeveType.__setattr__ = __enum_setattr
SleeveType.__delattr__ = __enum_delattr
