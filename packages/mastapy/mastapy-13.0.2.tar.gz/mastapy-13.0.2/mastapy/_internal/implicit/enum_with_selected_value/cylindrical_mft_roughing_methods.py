"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.manufacturing.cylindrical import _627
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_CylindricalMftRoughingMethods",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_CylindricalMftRoughingMethods")


class EnumWithSelectedValue_CylindricalMftRoughingMethods(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_CylindricalMftRoughingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftRoughingMethods' types.
    """

    __qualname__ = "CylindricalMftRoughingMethods"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_627.CylindricalMftRoughingMethods":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _627.CylindricalMftRoughingMethods

    @classmethod
    def implicit_type(cls) -> "_627.CylindricalMftRoughingMethods.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _627.CylindricalMftRoughingMethods.type_()

    @property
    def selected_value(self: Self) -> "_627.CylindricalMftRoughingMethods":
        """mastapy.gears.manufacturing.cylindrical.CylindricalMftRoughingMethods

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_627.CylindricalMftRoughingMethods]":
        """List[mastapy.gears.manufacturing.cylindrical.CylindricalMftRoughingMethods]

        Note:
            This property is readonly.
        """
        return None
