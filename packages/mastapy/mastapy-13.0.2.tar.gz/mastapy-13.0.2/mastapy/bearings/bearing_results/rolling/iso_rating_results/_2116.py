"""StressConcentrationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_STRESS_CONCENTRATION_METHOD = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults",
    "StressConcentrationMethod",
)


__docformat__ = "restructuredtext en"
__all__ = ("StressConcentrationMethod",)


Self = TypeVar("Self", bound="StressConcentrationMethod")


class StressConcentrationMethod(Enum):
    """StressConcentrationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _STRESS_CONCENTRATION_METHOD

    BASIC_STRESS_RISER_FUNCTION = 0
    CALCULATED_STRESSES = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


StressConcentrationMethod.__setattr__ = __enum_setattr
StressConcentrationMethod.__delattr__ = __enum_delattr
