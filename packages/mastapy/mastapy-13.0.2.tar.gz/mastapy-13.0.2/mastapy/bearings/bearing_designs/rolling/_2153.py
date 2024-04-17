"""BearingTypeExtraInformation"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_TYPE_EXTRA_INFORMATION = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "BearingTypeExtraInformation"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingTypeExtraInformation",)


Self = TypeVar("Self", bound="BearingTypeExtraInformation")


class BearingTypeExtraInformation(Enum):
    """BearingTypeExtraInformation

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_TYPE_EXTRA_INFORMATION

    NONE = 0
    SKF_EXPLORER = 1
    XLIFE_PERFORMANCE = 2
    GENERATION_C = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingTypeExtraInformation.__setattr__ = __enum_setattr
BearingTypeExtraInformation.__delattr__ = __enum_delattr
