"""MeasurementSystem"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MEASUREMENT_SYSTEM = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements", "MeasurementSystem"
)


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementSystem",)


Self = TypeVar("Self", bound="MeasurementSystem")


class MeasurementSystem(Enum):
    """MeasurementSystem

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MEASUREMENT_SYSTEM

    METRIC = 0
    IMPERIAL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MeasurementSystem.__setattr__ = __enum_setattr
MeasurementSystem.__delattr__ = __enum_delattr
