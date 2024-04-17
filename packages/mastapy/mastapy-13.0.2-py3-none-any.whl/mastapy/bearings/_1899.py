"""RollingBearingArrangement"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_ARRANGEMENT = python_net_import(
    "SMT.MastaAPI.Bearings", "RollingBearingArrangement"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollingBearingArrangement",)


Self = TypeVar("Self", bound="RollingBearingArrangement")


class RollingBearingArrangement(Enum):
    """RollingBearingArrangement

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ROLLING_BEARING_ARRANGEMENT

    SINGLE = 0
    TANDEM = 1
    PAIR_X = 2
    PAIR_O = 3
    DOUBLE = 4


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


RollingBearingArrangement.__setattr__ = __enum_setattr
RollingBearingArrangement.__delattr__ = __enum_delattr
