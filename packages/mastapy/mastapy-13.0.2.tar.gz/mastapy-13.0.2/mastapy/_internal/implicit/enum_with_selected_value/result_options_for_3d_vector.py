"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.math_utility import _1534
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ResultOptionsFor3DVector",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ResultOptionsFor3DVector")


class EnumWithSelectedValue_ResultOptionsFor3DVector(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ResultOptionsFor3DVector

    A specific implementation of 'EnumWithSelectedValue' for 'ResultOptionsFor3DVector' types.
    """

    __qualname__ = "ResultOptionsFor3DVector"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1534.ResultOptionsFor3DVector":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1534.ResultOptionsFor3DVector

    @classmethod
    def implicit_type(cls) -> "_1534.ResultOptionsFor3DVector.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1534.ResultOptionsFor3DVector.type_()

    @property
    def selected_value(self: Self) -> "_1534.ResultOptionsFor3DVector":
        """mastapy.math_utility.ResultOptionsFor3DVector

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1534.ResultOptionsFor3DVector]":
        """List[mastapy.math_utility.ResultOptionsFor3DVector]

        Note:
            This property is readonly.
        """
        return None
