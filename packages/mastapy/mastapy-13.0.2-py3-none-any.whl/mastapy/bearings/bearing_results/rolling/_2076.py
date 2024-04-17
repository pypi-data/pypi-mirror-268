"""RollerAnalysisMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ROLLER_ANALYSIS_METHOD = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "RollerAnalysisMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollerAnalysisMethod",)


Self = TypeVar("Self", bound="RollerAnalysisMethod")


class RollerAnalysisMethod(Enum):
    """RollerAnalysisMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ROLLER_ANALYSIS_METHOD

    THREE_DEGREE_OF_FREEDOM_ROLLERS = 0
    LEGACY_METHOD = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RollerAnalysisMethod.__setattr__ = __enum_setattr
RollerAnalysisMethod.__delattr__ = __enum_delattr
