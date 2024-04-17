"""GearOrientations"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GEAR_ORIENTATIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "GearOrientations"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearOrientations",)


Self = TypeVar("Self", bound="GearOrientations")


class GearOrientations(Enum):
    """GearOrientations

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GEAR_ORIENTATIONS

    LEFT = 0
    RIGHT = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GearOrientations.__setattr__ = __enum_setattr
GearOrientations.__delattr__ = __enum_delattr
