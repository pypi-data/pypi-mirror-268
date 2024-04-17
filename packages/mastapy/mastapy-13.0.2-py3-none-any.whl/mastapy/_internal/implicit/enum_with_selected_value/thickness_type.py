"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.gear_designs.cylindrical import _1085
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ThicknessType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ThicknessType")


class EnumWithSelectedValue_ThicknessType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThicknessType

    A specific implementation of 'EnumWithSelectedValue' for 'ThicknessType' types.
    """

    __qualname__ = "ThicknessType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1085.ThicknessType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1085.ThicknessType

    @classmethod
    def implicit_type(cls) -> "_1085.ThicknessType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1085.ThicknessType.type_()

    @property
    def selected_value(self: Self) -> "_1085.ThicknessType":
        """mastapy.gears.gear_designs.cylindrical.ThicknessType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1085.ThicknessType]":
        """List[mastapy.gears.gear_designs.cylindrical.ThicknessType]

        Note:
            This property is readonly.
        """
        return None
