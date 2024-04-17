"""PowerRatingF1EstimationMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_POWER_RATING_F1_ESTIMATION_METHOD = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "PowerRatingF1EstimationMethod"
)


__docformat__ = "restructuredtext en"
__all__ = ("PowerRatingF1EstimationMethod",)


Self = TypeVar("Self", bound="PowerRatingF1EstimationMethod")


class PowerRatingF1EstimationMethod(Enum):
    """PowerRatingF1EstimationMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _POWER_RATING_F1_ESTIMATION_METHOD

    ISOTR_141792001 = 0
    USERSPECIFIED = 1
    ONEDIMENSIONAL_LOOKUP_TABLE = 2
    TWODIMENSIONAL_LOOKUP_TABLE = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


PowerRatingF1EstimationMethod.__setattr__ = __enum_setattr
PowerRatingF1EstimationMethod.__delattr__ = __enum_delattr
