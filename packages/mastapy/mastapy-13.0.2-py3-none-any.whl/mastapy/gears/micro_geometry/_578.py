"""LocationOfRootReliefEvaluation"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_LOCATION_OF_ROOT_RELIEF_EVALUATION = python_net_import(
    "SMT.MastaAPI.Gears.MicroGeometry", "LocationOfRootReliefEvaluation"
)


__docformat__ = "restructuredtext en"
__all__ = ("LocationOfRootReliefEvaluation",)


Self = TypeVar("Self", bound="LocationOfRootReliefEvaluation")


class LocationOfRootReliefEvaluation(Enum):
    """LocationOfRootReliefEvaluation

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _LOCATION_OF_ROOT_RELIEF_EVALUATION

    ROOT_FORM = 0
    LOWER_EVALUATION_LIMIT = 1
    USERSPECIFIED = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


LocationOfRootReliefEvaluation.__setattr__ = __enum_setattr
LocationOfRootReliefEvaluation.__delattr__ = __enum_delattr
