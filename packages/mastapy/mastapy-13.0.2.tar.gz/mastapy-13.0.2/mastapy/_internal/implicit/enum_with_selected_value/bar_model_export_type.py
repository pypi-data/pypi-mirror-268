"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis import _53
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_BarModelExportType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_BarModelExportType")


class EnumWithSelectedValue_BarModelExportType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BarModelExportType

    A specific implementation of 'EnumWithSelectedValue' for 'BarModelExportType' types.
    """

    __qualname__ = "BarModelExportType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_53.BarModelExportType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _53.BarModelExportType

    @classmethod
    def implicit_type(cls) -> "_53.BarModelExportType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _53.BarModelExportType.type_()

    @property
    def selected_value(self: Self) -> "_53.BarModelExportType":
        """mastapy.nodal_analysis.BarModelExportType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_53.BarModelExportType]":
        """List[mastapy.nodal_analysis.BarModelExportType]

        Note:
            This property is readonly.
        """
        return None
