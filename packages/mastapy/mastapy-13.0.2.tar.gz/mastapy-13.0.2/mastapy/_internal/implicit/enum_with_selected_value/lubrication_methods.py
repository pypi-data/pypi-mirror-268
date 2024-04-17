"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears import _338
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LubricationMethods",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LubricationMethods")


class EnumWithSelectedValue_LubricationMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LubricationMethods

    A specific implementation of 'EnumWithSelectedValue' for 'LubricationMethods' types.
    """

    __qualname__ = "LubricationMethods"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_338.LubricationMethods":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _338.LubricationMethods

    @classmethod
    def implicit_type(cls) -> "_338.LubricationMethods.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _338.LubricationMethods.type_()

    @property
    def selected_value(self: Self) -> "_338.LubricationMethods":
        """mastapy.gears.LubricationMethods

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_338.LubricationMethods]":
        """List[mastapy.gears.LubricationMethods]

        Note:
            This property is readonly.
        """
        return None
