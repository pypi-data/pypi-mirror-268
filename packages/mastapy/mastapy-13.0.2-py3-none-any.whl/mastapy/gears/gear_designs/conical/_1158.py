"""ConicalFlanks"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_CONICAL_FLANKS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalFlanks"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalFlanks",)


Self = TypeVar("Self", bound="ConicalFlanks")


class ConicalFlanks(Enum):
    """ConicalFlanks

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONICAL_FLANKS

    CONCAVE = 0
    CONVEX = 1
    WORST = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ConicalFlanks.__setattr__ = __enum_setattr
ConicalFlanks.__delattr__ = __enum_delattr
