"""MicroGeometryDefinitionMethod"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DEFINITION_METHOD = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving",
    "MicroGeometryDefinitionMethod",
)


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryDefinitionMethod",)


Self = TypeVar("Self", bound="MicroGeometryDefinitionMethod")


class MicroGeometryDefinitionMethod(Enum):
    """MicroGeometryDefinitionMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MICRO_GEOMETRY_DEFINITION_METHOD

    NORMAL_TO_INVOLUTE = 0
    ARC_LENGTH = 1


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


MicroGeometryDefinitionMethod.__setattr__ = __enum_setattr
MicroGeometryDefinitionMethod.__delattr__ = __enum_delattr
