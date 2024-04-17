"""ScuffingMethods"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_SCUFFING_METHODS = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "ScuffingMethods"
)


__docformat__ = "restructuredtext en"
__all__ = ("ScuffingMethods",)


Self = TypeVar("Self", bound="ScuffingMethods")


class ScuffingMethods(Enum):
    """ScuffingMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SCUFFING_METHODS

    AGMA_2001B88 = 0
    AGMA_925A03 = 1
    AGMA_925B22 = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ScuffingMethods.__setattr__ = __enum_setattr
ScuffingMethods.__delattr__ = __enum_delattr
