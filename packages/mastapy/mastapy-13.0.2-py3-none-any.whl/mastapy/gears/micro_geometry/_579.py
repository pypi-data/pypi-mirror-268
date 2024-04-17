"""LocationOfTipReliefEvaluation"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_LOCATION_OF_TIP_RELIEF_EVALUATION = python_net_import(
    "SMT.MastaAPI.Gears.MicroGeometry", "LocationOfTipReliefEvaluation"
)


__docformat__ = "restructuredtext en"
__all__ = ("LocationOfTipReliefEvaluation",)


Self = TypeVar("Self", bound="LocationOfTipReliefEvaluation")


class LocationOfTipReliefEvaluation(Enum):
    """LocationOfTipReliefEvaluation

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _LOCATION_OF_TIP_RELIEF_EVALUATION

    TIP_FORM = 0
    UPPER_EVALUATION_LIMIT = 1
    USERSPECIFIED = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


LocationOfTipReliefEvaluation.__setattr__ = __enum_setattr
LocationOfTipReliefEvaluation.__delattr__ = __enum_delattr
