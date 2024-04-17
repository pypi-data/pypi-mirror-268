"""AnalysisTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ANALYSIS_TYPES = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "AnalysisTypes"
)


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisTypes",)


Self = TypeVar("Self", bound="AnalysisTypes")


class AnalysisTypes(Enum):
    """AnalysisTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ANALYSIS_TYPES

    NORMAL = 0
    RUNUPDOWN = 1
    SIMULINK = 2
    DRIVE_CYCLE = 3
    DRIVE_CYCLE_WITH_SIMULINK = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AnalysisTypes.__setattr__ = __enum_setattr
AnalysisTypes.__delattr__ = __enum_delattr
