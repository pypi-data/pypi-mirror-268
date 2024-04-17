"""DirectionOfMeasuredModifications"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_DIRECTION_OF_MEASURED_MODIFICATIONS = python_net_import(
    "SMT.MastaAPI.Cycloidal", "DirectionOfMeasuredModifications"
)


__docformat__ = "restructuredtext en"
__all__ = ("DirectionOfMeasuredModifications",)


Self = TypeVar("Self", bound="DirectionOfMeasuredModifications")


class DirectionOfMeasuredModifications(Enum):
    """DirectionOfMeasuredModifications

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _DIRECTION_OF_MEASURED_MODIFICATIONS

    NORMAL = 0
    RADIAL = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


DirectionOfMeasuredModifications.__setattr__ = __enum_setattr
DirectionOfMeasuredModifications.__delattr__ = __enum_delattr
