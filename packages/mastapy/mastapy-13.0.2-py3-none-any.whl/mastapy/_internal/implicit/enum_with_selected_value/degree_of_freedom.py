"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.math_utility import _1511
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_DegreeOfFreedom",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_DegreeOfFreedom")


class EnumWithSelectedValue_DegreeOfFreedom(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DegreeOfFreedom

    A specific implementation of 'EnumWithSelectedValue' for 'DegreeOfFreedom' types.
    """

    __qualname__ = "DegreeOfFreedom"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1511.DegreeOfFreedom":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1511.DegreeOfFreedom

    @classmethod
    def implicit_type(cls) -> "_1511.DegreeOfFreedom.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1511.DegreeOfFreedom.type_()

    @property
    def selected_value(self: Self) -> "_1511.DegreeOfFreedom":
        """mastapy.math_utility.DegreeOfFreedom

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1511.DegreeOfFreedom]":
        """List[mastapy.math_utility.DegreeOfFreedom]

        Note:
            This property is readonly.
        """
        return None
