"""AdditionalForcesObtainedFrom"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ADDITIONAL_FORCES_OBTAINED_FROM = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "AdditionalForcesObtainedFrom",
)


__docformat__ = "restructuredtext en"
__all__ = ("AdditionalForcesObtainedFrom",)


Self = TypeVar("Self", bound="AdditionalForcesObtainedFrom")


class AdditionalForcesObtainedFrom(Enum):
    """AdditionalForcesObtainedFrom

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ADDITIONAL_FORCES_OBTAINED_FROM

    LARGEST_MAGNITUDE = 0
    MEDIAN_VALUE = 1
    AVERAGE_VALUE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


AdditionalForcesObtainedFrom.__setattr__ = __enum_setattr
AdditionalForcesObtainedFrom.__delattr__ = __enum_delattr
