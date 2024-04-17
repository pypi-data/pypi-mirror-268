"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.manufacturing.cylindrical import _626
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_CylindricalMftFinishingMethods",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_CylindricalMftFinishingMethods")


class EnumWithSelectedValue_CylindricalMftFinishingMethods(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_CylindricalMftFinishingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftFinishingMethods' types.
    """

    __qualname__ = "CylindricalMftFinishingMethods"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_626.CylindricalMftFinishingMethods":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _626.CylindricalMftFinishingMethods

    @classmethod
    def implicit_type(cls) -> "_626.CylindricalMftFinishingMethods.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _626.CylindricalMftFinishingMethods.type_()

    @property
    def selected_value(self: Self) -> "_626.CylindricalMftFinishingMethods":
        """mastapy.gears.manufacturing.cylindrical.CylindricalMftFinishingMethods

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_626.CylindricalMftFinishingMethods]":
        """List[mastapy.gears.manufacturing.cylindrical.CylindricalMftFinishingMethods]

        Note:
            This property is readonly.
        """
        return None
