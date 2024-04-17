"""MeasuredMapDataTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MEASURED_MAP_DATA_TYPES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry", "MeasuredMapDataTypes"
)


__docformat__ = "restructuredtext en"
__all__ = ("MeasuredMapDataTypes",)


Self = TypeVar("Self", bound="MeasuredMapDataTypes")


class MeasuredMapDataTypes(Enum):
    """MeasuredMapDataTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MEASURED_MAP_DATA_TYPES

    MULTIPLE_PROFILES = 0
    MULTIPLE_PROFILES_ONE_LEAD = 1
    MULTIPLE_LEADS = 2
    MULTIPLE_LEADS_ONE_PROFILE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MeasuredMapDataTypes.__setattr__ = __enum_setattr
MeasuredMapDataTypes.__delattr__ = __enum_delattr
