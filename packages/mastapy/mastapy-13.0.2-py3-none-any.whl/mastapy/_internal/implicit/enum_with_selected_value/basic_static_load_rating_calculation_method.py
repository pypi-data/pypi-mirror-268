"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings import _1878
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod"
)


class EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BasicStaticLoadRatingCalculationMethod' types.
    """

    __qualname__ = "BasicStaticLoadRatingCalculationMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1878.BasicStaticLoadRatingCalculationMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1878.BasicStaticLoadRatingCalculationMethod

    @classmethod
    def implicit_type(cls) -> "_1878.BasicStaticLoadRatingCalculationMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1878.BasicStaticLoadRatingCalculationMethod.type_()

    @property
    def selected_value(self: Self) -> "_1878.BasicStaticLoadRatingCalculationMethod":
        """mastapy.bearings.BasicStaticLoadRatingCalculationMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_1878.BasicStaticLoadRatingCalculationMethod]":
        """List[mastapy.bearings.BasicStaticLoadRatingCalculationMethod]

        Note:
            This property is readonly.
        """
        return None
