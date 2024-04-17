"""GearPositions"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GEAR_POSITIONS = python_net_import(
    "SMT.MastaAPI.Utility.ModalAnalysis.Gears", "GearPositions"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearPositions",)


Self = TypeVar("Self", bound="GearPositions")


class GearPositions(Enum):
    """GearPositions

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GEAR_POSITIONS

    UNSPECIFIED = 0
    PINION = 1
    WHEEL = 2
    SUN = 3
    PLANET = 4
    ANNULUS = 5


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GearPositions.__setattr__ = __enum_setattr
GearPositions.__delattr__ = __enum_delattr
