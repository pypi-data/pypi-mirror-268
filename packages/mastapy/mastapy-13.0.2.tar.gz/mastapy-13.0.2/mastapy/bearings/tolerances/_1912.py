"""FitType"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_FIT_TYPE = python_net_import("SMT.MastaAPI.Bearings.Tolerances", "FitType")


__docformat__ = "restructuredtext en"
__all__ = ("FitType",)


Self = TypeVar("Self", bound="FitType")


class FitType(Enum):
    """FitType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _FIT_TYPE

    INTERFERENCE = 0
    TRANSITION = 1
    CLEARANCE = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


FitType.__setattr__ = __enum_setattr
FitType.__delattr__ = __enum_delattr
