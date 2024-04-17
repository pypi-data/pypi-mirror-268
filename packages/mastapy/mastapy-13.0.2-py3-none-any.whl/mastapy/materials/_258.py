"""GearingTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_GEARING_TYPES = python_net_import("SMT.MastaAPI.Materials", "GearingTypes")


__docformat__ = "restructuredtext en"
__all__ = ("GearingTypes",)


Self = TypeVar("Self", bound="GearingTypes")


class GearingTypes(Enum):
    """GearingTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GEARING_TYPES

    OPEN_GEARING = 0
    COMMERCIAL_ENCLOSED_GEAR_UNITS = 1
    PRECISION_ENCLOSED_GEAR_UNITS = 2
    EXTRA_PRECISION_ENCLOSED_GEAR_UNITS = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


GearingTypes.__setattr__ = __enum_setattr
GearingTypes.__delattr__ = __enum_delattr
