"""RoundnessSpecificationType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ROUNDNESS_SPECIFICATION_TYPE = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "RoundnessSpecificationType"
)


__docformat__ = "restructuredtext en"
__all__ = ("RoundnessSpecificationType",)


Self = TypeVar("Self", bound="RoundnessSpecificationType")


class RoundnessSpecificationType(Enum):
    """RoundnessSpecificationType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ROUNDNESS_SPECIFICATION_TYPE

    SINUSOIDAL = 0
    USERSPECIFIED = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RoundnessSpecificationType.__setattr__ = __enum_setattr
RoundnessSpecificationType.__delattr__ = __enum_delattr
