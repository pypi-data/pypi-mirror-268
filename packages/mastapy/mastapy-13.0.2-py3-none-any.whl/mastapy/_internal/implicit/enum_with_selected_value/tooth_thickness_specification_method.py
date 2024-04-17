"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.gear_designs.bevel import _1196
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ToothThicknessSpecificationMethod",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ToothThicknessSpecificationMethod")


class EnumWithSelectedValue_ToothThicknessSpecificationMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ToothThicknessSpecificationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ToothThicknessSpecificationMethod' types.
    """

    __qualname__ = "ToothThicknessSpecificationMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1196.ToothThicknessSpecificationMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1196.ToothThicknessSpecificationMethod

    @classmethod
    def implicit_type(cls) -> "_1196.ToothThicknessSpecificationMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1196.ToothThicknessSpecificationMethod.type_()

    @property
    def selected_value(self: Self) -> "_1196.ToothThicknessSpecificationMethod":
        """mastapy.gears.gear_designs.bevel.ToothThicknessSpecificationMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1196.ToothThicknessSpecificationMethod]":
        """List[mastapy.gears.gear_designs.bevel.ToothThicknessSpecificationMethod]

        Note:
            This property is readonly.
        """
        return None
