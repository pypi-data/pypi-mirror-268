"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _649
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_MicroGeometryDefinitionType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_MicroGeometryDefinitionType")


class EnumWithSelectedValue_MicroGeometryDefinitionType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_MicroGeometryDefinitionType

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryDefinitionType' types.
    """

    __qualname__ = "MicroGeometryDefinitionType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_649.MicroGeometryDefinitionType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _649.MicroGeometryDefinitionType

    @classmethod
    def implicit_type(cls) -> "_649.MicroGeometryDefinitionType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _649.MicroGeometryDefinitionType.type_()

    @property
    def selected_value(self: Self) -> "_649.MicroGeometryDefinitionType":
        """mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_649.MicroGeometryDefinitionType]":
        """List[mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionType]

        Note:
            This property is readonly.
        """
        return None
