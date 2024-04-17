"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.math_utility import _1498
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_AlignmentAxis",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_AlignmentAxis")


class EnumWithSelectedValue_AlignmentAxis(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AlignmentAxis

    A specific implementation of 'EnumWithSelectedValue' for 'AlignmentAxis' types.
    """

    __qualname__ = "AlignmentAxis"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1498.AlignmentAxis":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1498.AlignmentAxis

    @classmethod
    def implicit_type(cls) -> "_1498.AlignmentAxis.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1498.AlignmentAxis.type_()

    @property
    def selected_value(self: Self) -> "_1498.AlignmentAxis":
        """mastapy.math_utility.AlignmentAxis

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1498.AlignmentAxis]":
        """List[mastapy.math_utility.AlignmentAxis]

        Note:
            This property is readonly.
        """
        return None
