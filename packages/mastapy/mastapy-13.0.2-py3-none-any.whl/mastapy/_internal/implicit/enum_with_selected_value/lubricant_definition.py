"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.materials import _264
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LubricantDefinition",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LubricantDefinition")


class EnumWithSelectedValue_LubricantDefinition(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_LubricantDefinition

    A specific implementation of 'EnumWithSelectedValue' for 'LubricantDefinition' types.
    """

    __qualname__ = "LubricantDefinition"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_264.LubricantDefinition":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _264.LubricantDefinition

    @classmethod
    def implicit_type(cls) -> "_264.LubricantDefinition.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _264.LubricantDefinition.type_()

    @property
    def selected_value(self: Self) -> "_264.LubricantDefinition":
        """mastapy.materials.LubricantDefinition

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_264.LubricantDefinition]":
        """List[mastapy.materials.LubricantDefinition]

        Note:
            This property is readonly.
        """
        return None
