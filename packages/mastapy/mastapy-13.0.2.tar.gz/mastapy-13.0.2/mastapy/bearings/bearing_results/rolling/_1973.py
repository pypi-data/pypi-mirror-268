"""BallBearingAnalysisMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BALL_BEARING_ANALYSIS_METHOD = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "BallBearingAnalysisMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("BallBearingAnalysisMethod",)


Self = TypeVar("Self", bound="BallBearingAnalysisMethod")


class BallBearingAnalysisMethod(Enum):
    """BallBearingAnalysisMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BALL_BEARING_ANALYSIS_METHOD

    TWO_DEGREES_OF_FREEDOM = 0
    TWO_DEGREES_OF_FREEDOM_IN_SIX_DOF_FRAMEWORK = 1
    SIX_DEGREES_OF_FREEDOM_COULOMB = 2
    SIX_DEGREES_OF_FREEDOM_ADVANCED = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BallBearingAnalysisMethod.__setattr__ = __enum_setattr
BallBearingAnalysisMethod.__delattr__ = __enum_delattr
