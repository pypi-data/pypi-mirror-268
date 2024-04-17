"""AnalysisMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ANALYSIS_METHOD = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "AnalysisMethod",
)


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisMethod",)


Self = TypeVar("Self", bound="AnalysisMethod")


class AnalysisMethod(Enum):
    """AnalysisMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ANALYSIS_METHOD

    NEWTON_RAPHSON = 0
    HEURISTIC_SEARCH = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AnalysisMethod.__setattr__ = __enum_setattr
AnalysisMethod.__delattr__ = __enum_delattr
