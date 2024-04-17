"""OuterRingMounting"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_OUTER_RING_MOUNTING = python_net_import("SMT.MastaAPI.Bearings", "OuterRingMounting")


__docformat__ = "restructuredtext en"
__all__ = ("OuterRingMounting",)


Self = TypeVar("Self", bound="OuterRingMounting")


class OuterRingMounting(Enum):
    """OuterRingMounting

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _OUTER_RING_MOUNTING

    STANDARD = 0
    SPHERICAL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


OuterRingMounting.__setattr__ = __enum_setattr
OuterRingMounting.__delattr__ = __enum_delattr
