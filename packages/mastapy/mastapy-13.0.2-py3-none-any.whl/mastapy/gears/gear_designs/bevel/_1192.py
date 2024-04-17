"""FinishingMethods"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FINISHING_METHODS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Bevel", "FinishingMethods"
)


__docformat__ = "restructuredtext en"
__all__ = ("FinishingMethods",)


Self = TypeVar("Self", bound="FinishingMethods")


class FinishingMethods(Enum):
    """FinishingMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FINISHING_METHODS

    AS_CUT = 0
    CUT_AND_LAPPED = 1
    GROUND = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FinishingMethods.__setattr__ = __enum_setattr
FinishingMethods.__delattr__ = __enum_delattr
