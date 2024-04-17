"""LubricationMethods"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_LUBRICATION_METHODS = python_net_import("SMT.MastaAPI.Gears", "LubricationMethods")


__docformat__ = "restructuredtext en"
__all__ = ("LubricationMethods",)


Self = TypeVar("Self", bound="LubricationMethods")


class LubricationMethods(Enum):
    """LubricationMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _LUBRICATION_METHODS

    SPRAYINJECTION_LUBRICATION = 0
    DIP_LUBRICATION = 1
    SUBMERGED = 2
    ADDITIONAL_SPRAY_LUBRICATION = 3


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


LubricationMethods.__setattr__ = __enum_setattr
LubricationMethods.__delattr__ = __enum_delattr
