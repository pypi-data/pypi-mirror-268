"""DoubleAxisScaleAndRange"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_DOUBLE_AXIS_SCALE_AND_RANGE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "DoubleAxisScaleAndRange"
)


__docformat__ = "restructuredtext en"
__all__ = ("DoubleAxisScaleAndRange",)


Self = TypeVar("Self", bound="DoubleAxisScaleAndRange")


class DoubleAxisScaleAndRange(Enum):
    """DoubleAxisScaleAndRange

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _DOUBLE_AXIS_SCALE_AND_RANGE

    MASTA_DEFAULT = 0
    EQUAL_SCALE = 1
    EQUAL_RANGE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


DoubleAxisScaleAndRange.__setattr__ = __enum_setattr
DoubleAxisScaleAndRange.__delattr__ = __enum_delattr
