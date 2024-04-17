"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _648
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_MicroGeometryDefinitionMethod",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_MicroGeometryDefinitionMethod")


class EnumWithSelectedValue_MicroGeometryDefinitionMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_MicroGeometryDefinitionMethod

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryDefinitionMethod' types.
    """

    __qualname__ = "MicroGeometryDefinitionMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_648.MicroGeometryDefinitionMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _648.MicroGeometryDefinitionMethod

    @classmethod
    def implicit_type(cls) -> "_648.MicroGeometryDefinitionMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _648.MicroGeometryDefinitionMethod.type_()

    @property
    def selected_value(self: Self) -> "_648.MicroGeometryDefinitionMethod":
        """mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_648.MicroGeometryDefinitionMethod]":
        """List[mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionMethod]

        Note:
            This property is readonly.
        """
        return None
