"""TolerancedMetalMeasurements"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_TOLERANCED_METAL_MEASUREMENTS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "TolerancedMetalMeasurements"
)


__docformat__ = "restructuredtext en"
__all__ = ("TolerancedMetalMeasurements",)


Self = TypeVar("Self", bound="TolerancedMetalMeasurements")


class TolerancedMetalMeasurements(Enum):
    """TolerancedMetalMeasurements

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _TOLERANCED_METAL_MEASUREMENTS

    MINIMUM_THICKNESS = 0
    AVERAGE_THICKNESS = 1
    MAXIMUM_THICKNESS = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


TolerancedMetalMeasurements.__setattr__ = __enum_setattr
TolerancedMetalMeasurements.__delattr__ = __enum_delattr
