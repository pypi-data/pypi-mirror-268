"""RootStressSurfaceChartOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ROOT_STRESS_SURFACE_CHART_OPTION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "RootStressSurfaceChartOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("RootStressSurfaceChartOption",)


Self = TypeVar("Self", bound="RootStressSurfaceChartOption")


class RootStressSurfaceChartOption(Enum):
    """RootStressSurfaceChartOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ROOT_STRESS_SURFACE_CHART_OPTION

    DISTANCE_ALONG_FILLET = 0
    DIAMETER = 1
    RADIUS = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RootStressSurfaceChartOption.__setattr__ = __enum_setattr
RootStressSurfaceChartOption.__delattr__ = __enum_delattr
