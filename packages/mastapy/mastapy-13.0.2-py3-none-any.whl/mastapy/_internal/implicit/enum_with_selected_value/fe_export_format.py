"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis.fe_export_utility import _169
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_FEExportFormat",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_FEExportFormat")


class EnumWithSelectedValue_FEExportFormat(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FEExportFormat

    A specific implementation of 'EnumWithSelectedValue' for 'FEExportFormat' types.
    """

    __qualname__ = "FEExportFormat"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_169.FEExportFormat":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _169.FEExportFormat

    @classmethod
    def implicit_type(cls) -> "_169.FEExportFormat.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _169.FEExportFormat.type_()

    @property
    def selected_value(self: Self) -> "_169.FEExportFormat":
        """mastapy.nodal_analysis.fe_export_utility.FEExportFormat

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_169.FEExportFormat]":
        """List[mastapy.nodal_analysis.fe_export_utility.FEExportFormat]

        Note:
            This property is readonly.
        """
        return None
