"""BearingStiffnessMatrixOption"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_BEARING_STIFFNESS_MATRIX_OPTION = python_net_import(
    "SMT.MastaAPI.Bearings", "BearingStiffnessMatrixOption"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingStiffnessMatrixOption",)


Self = TypeVar("Self", bound="BearingStiffnessMatrixOption")


class BearingStiffnessMatrixOption(Enum):
    """BearingStiffnessMatrixOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_STIFFNESS_MATRIX_OPTION

    BASIC = 0
    SPECIFY_MATRIX = 1
    SPEED_DEPENDENT = 2


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


BearingStiffnessMatrixOption.__setattr__ = __enum_setattr
BearingStiffnessMatrixOption.__delattr__ = __enum_delattr
