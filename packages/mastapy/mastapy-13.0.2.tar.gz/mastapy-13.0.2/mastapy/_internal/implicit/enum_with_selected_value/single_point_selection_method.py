"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis.varying_input_components import _101
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_SinglePointSelectionMethod",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_SinglePointSelectionMethod")


class EnumWithSelectedValue_SinglePointSelectionMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_SinglePointSelectionMethod

    A specific implementation of 'EnumWithSelectedValue' for 'SinglePointSelectionMethod' types.
    """

    __qualname__ = "SinglePointSelectionMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_101.SinglePointSelectionMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _101.SinglePointSelectionMethod

    @classmethod
    def implicit_type(cls) -> "_101.SinglePointSelectionMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _101.SinglePointSelectionMethod.type_()

    @property
    def selected_value(self: Self) -> "_101.SinglePointSelectionMethod":
        """mastapy.nodal_analysis.varying_input_components.SinglePointSelectionMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_101.SinglePointSelectionMethod]":
        """List[mastapy.nodal_analysis.varying_input_components.SinglePointSelectionMethod]

        Note:
            This property is readonly.
        """
        return None
