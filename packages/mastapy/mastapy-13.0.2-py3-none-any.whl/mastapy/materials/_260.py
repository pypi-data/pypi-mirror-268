"""GreaseContaminationOptions"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GREASE_CONTAMINATION_OPTIONS = python_net_import(
    "SMT.MastaAPI.Materials", "GreaseContaminationOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("GreaseContaminationOptions",)


Self = TypeVar("Self", bound="GreaseContaminationOptions")


class GreaseContaminationOptions(Enum):
    """GreaseContaminationOptions

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GREASE_CONTAMINATION_OPTIONS

    HIGH_CLEANLINESS = 0
    NORMAL_CLEANLINESS = 1
    SLIGHTTYPICAL_CONTAMINATION = 2
    SEVERE_CONTAMINATION = 3
    VERY_SEVERE_CONTAMINATION = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GreaseContaminationOptions.__setattr__ = __enum_setattr
GreaseContaminationOptions.__delattr__ = __enum_delattr
