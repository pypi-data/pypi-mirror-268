"""FlankLoadingState"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FLANK_LOADING_STATE = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "FlankLoadingState"
)


__docformat__ = "restructuredtext en"
__all__ = ("FlankLoadingState",)


Self = TypeVar("Self", bound="FlankLoadingState")


class FlankLoadingState(Enum):
    """FlankLoadingState

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FLANK_LOADING_STATE

    UNLOADED = 0
    DRIVING = 1
    DRIVEN = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FlankLoadingState.__setattr__ = __enum_setattr
FlankLoadingState.__delattr__ = __enum_delattr
