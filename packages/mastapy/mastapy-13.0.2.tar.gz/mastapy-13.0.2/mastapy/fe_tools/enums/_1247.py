"""ElementPropertyClass"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTY_CLASS = python_net_import(
    "SMT.MastaAPI.FETools.Enums", "ElementPropertyClass"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElementPropertyClass",)


Self = TypeVar("Self", bound="ElementPropertyClass")


class ElementPropertyClass(Enum):
    """ElementPropertyClass

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ELEMENT_PROPERTY_CLASS

    UNDEFINED = 0
    SOLID = 1
    SHELL = 2
    MEMBRANE = 3
    BEAM = 4
    TRUSS = 5
    INFINITE = 6
    GAP = 7
    JOINT = 8
    SPRING_DASHPOT = 9
    RIGID = 10
    CONSTRAINT = 11
    PLOT = 12
    MASS = 13
    INTERFACE = 14
    SUPERELEMENT = 15


def __enum_setattr(self: Self, attr: str, value: Any):
    raise AttributeError("Cannot set the attributes of an Enum.") from None


def __enum_delattr(self: Self, attr: str):
    raise AttributeError("Cannot delete the attributes of an Enum.") from None


ElementPropertyClass.__setattr__ = __enum_setattr
ElementPropertyClass.__delattr__ = __enum_delattr
