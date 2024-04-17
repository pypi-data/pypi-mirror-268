"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears import _341
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod",)


Self = TypeVar(
    "Self",
    bound="EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod",
)


class EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'MicropittingCoefficientOfFrictionCalculationMethod' types.
    """

    __qualname__ = "MicropittingCoefficientOfFrictionCalculationMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_341.MicropittingCoefficientOfFrictionCalculationMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _341.MicropittingCoefficientOfFrictionCalculationMethod

    @classmethod
    def implicit_type(
        cls,
    ) -> "_341.MicropittingCoefficientOfFrictionCalculationMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _341.MicropittingCoefficientOfFrictionCalculationMethod.type_()

    @property
    def selected_value(
        self: Self,
    ) -> "_341.MicropittingCoefficientOfFrictionCalculationMethod":
        """mastapy.gears.MicropittingCoefficientOfFrictionCalculationMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_341.MicropittingCoefficientOfFrictionCalculationMethod]":
        """List[mastapy.gears.MicropittingCoefficientOfFrictionCalculationMethod]

        Note:
            This property is readonly.
        """
        return None
