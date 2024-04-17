"""RaceRadialMountingType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_RACE_RADIAL_MOUNTING_TYPE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "RaceRadialMountingType"
)


__docformat__ = "restructuredtext en"
__all__ = ("RaceRadialMountingType",)


Self = TypeVar("Self", bound="RaceRadialMountingType")


class RaceRadialMountingType(Enum):
    """RaceRadialMountingType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _RACE_RADIAL_MOUNTING_TYPE

    INTERFERENCE = 0
    CLEARANCE = 1
    SLIDING = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RaceRadialMountingType.__setattr__ = __enum_setattr
RaceRadialMountingType.__delattr__ = __enum_delattr
