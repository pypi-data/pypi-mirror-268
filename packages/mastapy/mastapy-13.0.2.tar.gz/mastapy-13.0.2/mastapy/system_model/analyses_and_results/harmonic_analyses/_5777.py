"""HarmonicAnalysisTorqueInputType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_TORQUE_INPUT_TYPE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HarmonicAnalysisTorqueInputType",
)


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisTorqueInputType",)


Self = TypeVar("Self", bound="HarmonicAnalysisTorqueInputType")


class HarmonicAnalysisTorqueInputType(Enum):
    """HarmonicAnalysisTorqueInputType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _HARMONIC_ANALYSIS_TORQUE_INPUT_TYPE

    LOAD_CASE = 0
    SPECIFIED_TORQUE_SPEED_CURVE = 1
    TORQUE_SPEED_CURVE_FROM_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


HarmonicAnalysisTorqueInputType.__setattr__ = __enum_setattr
HarmonicAnalysisTorqueInputType.__delattr__ = __enum_delattr
