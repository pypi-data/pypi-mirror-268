"""GleasonSafetyRequirements"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GLEASON_SAFETY_REQUIREMENTS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "GleasonSafetyRequirements"
)


__docformat__ = "restructuredtext en"
__all__ = ("GleasonSafetyRequirements",)


Self = TypeVar("Self", bound="GleasonSafetyRequirements")


class GleasonSafetyRequirements(Enum):
    """GleasonSafetyRequirements

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GLEASON_SAFETY_REQUIREMENTS

    MAXIMUM_SAFETY = 0
    FEWER_THAN_1_FAILURE_IN_100 = 1
    FEWER_THAN_1_FAILURE_IN_3 = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GleasonSafetyRequirements.__setattr__ = __enum_setattr
GleasonSafetyRequirements.__delattr__ = __enum_delattr
