"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _646
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ChartType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ChartType")


class EnumWithSelectedValue_ChartType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ChartType

    A specific implementation of 'EnumWithSelectedValue' for 'ChartType' types.
    """

    __qualname__ = "ChartType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_646.ChartType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _646.ChartType

    @classmethod
    def implicit_type(cls) -> "_646.ChartType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _646.ChartType.type_()

    @property
    def selected_value(self: Self) -> "_646.ChartType":
        """mastapy.gears.manufacturing.cylindrical.plunge_shaving.ChartType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_646.ChartType]":
        """List[mastapy.gears.manufacturing.cylindrical.plunge_shaving.ChartType]

        Note:
            This property is readonly.
        """
        return None
