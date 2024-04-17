"""BallBearingContactCalculation"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BALL_BEARING_CONTACT_CALCULATION = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "BallBearingContactCalculation"
)


__docformat__ = "restructuredtext en"
__all__ = ("BallBearingContactCalculation",)


Self = TypeVar("Self", bound="BallBearingContactCalculation")


class BallBearingContactCalculation(Enum):
    """BallBearingContactCalculation

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BALL_BEARING_CONTACT_CALCULATION

    FULL = 0
    BREWE_AND_HAMROCK_1977 = 1
    HAMROCK_AND_BREWE_1983 = 2
    HOUPERT_2016 = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BallBearingContactCalculation.__setattr__ = __enum_setattr
BallBearingContactCalculation.__delattr__ = __enum_delattr
