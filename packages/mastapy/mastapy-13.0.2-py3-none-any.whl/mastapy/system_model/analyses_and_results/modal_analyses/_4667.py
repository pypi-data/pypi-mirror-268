"""MultipleExcitationsSpeedRangeOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MULTIPLE_EXCITATIONS_SPEED_RANGE_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "MultipleExcitationsSpeedRangeOption",
)


__docformat__ = "restructuredtext en"
__all__ = ("MultipleExcitationsSpeedRangeOption",)


Self = TypeVar("Self", bound="MultipleExcitationsSpeedRangeOption")


class MultipleExcitationsSpeedRangeOption(Enum):
    """MultipleExcitationsSpeedRangeOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MULTIPLE_EXCITATIONS_SPEED_RANGE_OPTION

    INTERSECTION_OF_SPEED_RANGES = 0
    UNION_OF_SPEED_RANGES = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MultipleExcitationsSpeedRangeOption.__setattr__ = __enum_setattr
MultipleExcitationsSpeedRangeOption.__delattr__ = __enum_delattr
