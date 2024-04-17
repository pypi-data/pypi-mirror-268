"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.materials.efficiency import _303
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_OilSealLossCalculationMethod",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_OilSealLossCalculationMethod")


class EnumWithSelectedValue_OilSealLossCalculationMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_OilSealLossCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'OilSealLossCalculationMethod' types.
    """

    __qualname__ = "OilSealLossCalculationMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_303.OilSealLossCalculationMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _303.OilSealLossCalculationMethod

    @classmethod
    def implicit_type(cls) -> "_303.OilSealLossCalculationMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _303.OilSealLossCalculationMethod.type_()

    @property
    def selected_value(self: Self) -> "_303.OilSealLossCalculationMethod":
        """mastapy.materials.efficiency.OilSealLossCalculationMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_303.OilSealLossCalculationMethod]":
        """List[mastapy.materials.efficiency.OilSealLossCalculationMethod]

        Note:
            This property is readonly.
        """
        return None
