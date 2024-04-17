"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.math_utility import _1517
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ExtrapolationOptions",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ExtrapolationOptions")


class EnumWithSelectedValue_ExtrapolationOptions(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ExtrapolationOptions

    A specific implementation of 'EnumWithSelectedValue' for 'ExtrapolationOptions' types.
    """

    __qualname__ = "ExtrapolationOptions"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1517.ExtrapolationOptions":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1517.ExtrapolationOptions

    @classmethod
    def implicit_type(cls) -> "_1517.ExtrapolationOptions.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1517.ExtrapolationOptions.type_()

    @property
    def selected_value(self: Self) -> "_1517.ExtrapolationOptions":
        """mastapy.math_utility.ExtrapolationOptions

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1517.ExtrapolationOptions]":
        """List[mastapy.math_utility.ExtrapolationOptions]

        Note:
            This property is readonly.
        """
        return None
