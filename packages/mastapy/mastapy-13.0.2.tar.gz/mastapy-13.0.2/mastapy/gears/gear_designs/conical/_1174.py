"""KlingelnbergFinishingMethods"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_FINISHING_METHODS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "KlingelnbergFinishingMethods"
)


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergFinishingMethods",)


Self = TypeVar("Self", bound="KlingelnbergFinishingMethods")


class KlingelnbergFinishingMethods(Enum):
    """KlingelnbergFinishingMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _KLINGELNBERG_FINISHING_METHODS

    LAPPED = 0
    SOFTCUT = 1
    HPG = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


KlingelnbergFinishingMethods.__setattr__ = __enum_setattr
KlingelnbergFinishingMethods.__delattr__ = __enum_delattr
