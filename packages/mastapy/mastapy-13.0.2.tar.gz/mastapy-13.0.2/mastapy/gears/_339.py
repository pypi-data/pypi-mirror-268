"""MicroGeometryInputTypes"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_INPUT_TYPES = python_net_import(
    "SMT.MastaAPI.Gears", "MicroGeometryInputTypes"
)


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryInputTypes",)


Self = TypeVar("Self", bound="MicroGeometryInputTypes")


class MicroGeometryInputTypes(Enum):
    """MicroGeometryInputTypes

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MICRO_GEOMETRY_INPUT_TYPES

    FACTORS = 0
    MEASUREMENTS = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MicroGeometryInputTypes.__setattr__ = __enum_setattr
MicroGeometryInputTypes.__delattr__ = __enum_delattr
