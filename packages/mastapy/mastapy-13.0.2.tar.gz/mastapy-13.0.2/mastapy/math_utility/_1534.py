"""ResultOptionsFor3DVector"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_RESULT_OPTIONS_FOR_3D_VECTOR = python_net_import(
    "SMT.MastaAPI.MathUtility", "ResultOptionsFor3DVector"
)


__docformat__ = "restructuredtext en"
__all__ = ("ResultOptionsFor3DVector",)


Self = TypeVar("Self", bound="ResultOptionsFor3DVector")


class ResultOptionsFor3DVector(Enum):
    """ResultOptionsFor3DVector

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _RESULT_OPTIONS_FOR_3D_VECTOR

    X = 0
    Y = 1
    Z = 2
    MAGNITUDE_XY = 3
    MAGNITUDE = 4
    RADIAL_XY = 5
    TANGENTIAL_XY = 6


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ResultOptionsFor3DVector.__setattr__ = __enum_setattr
ResultOptionsFor3DVector.__delattr__ = __enum_delattr
