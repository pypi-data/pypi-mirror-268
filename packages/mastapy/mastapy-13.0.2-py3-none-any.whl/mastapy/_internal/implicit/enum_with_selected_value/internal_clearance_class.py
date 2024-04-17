"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings.tolerances import _1909
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_InternalClearanceClass",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_InternalClearanceClass")


class EnumWithSelectedValue_InternalClearanceClass(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_InternalClearanceClass

    A specific implementation of 'EnumWithSelectedValue' for 'InternalClearanceClass' types.
    """

    __qualname__ = "InternalClearanceClass"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1909.InternalClearanceClass":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1909.InternalClearanceClass

    @classmethod
    def implicit_type(cls) -> "_1909.InternalClearanceClass.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1909.InternalClearanceClass.type_()

    @property
    def selected_value(self: Self) -> "_1909.InternalClearanceClass":
        """mastapy.bearings.tolerances.InternalClearanceClass

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1909.InternalClearanceClass]":
        """List[mastapy.bearings.tolerances.InternalClearanceClass]

        Note:
            This property is readonly.
        """
        return None
