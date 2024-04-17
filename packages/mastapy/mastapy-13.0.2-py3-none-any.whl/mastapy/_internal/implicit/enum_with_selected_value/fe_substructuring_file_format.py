"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis.fe_export_utility import _170
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_FESubstructuringFileFormat",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_FESubstructuringFileFormat")


class EnumWithSelectedValue_FESubstructuringFileFormat(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_FESubstructuringFileFormat

    A specific implementation of 'EnumWithSelectedValue' for 'FESubstructuringFileFormat' types.
    """

    __qualname__ = "FESubstructuringFileFormat"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_170.FESubstructuringFileFormat":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _170.FESubstructuringFileFormat

    @classmethod
    def implicit_type(cls) -> "_170.FESubstructuringFileFormat.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _170.FESubstructuringFileFormat.type_()

    @property
    def selected_value(self: Self) -> "_170.FESubstructuringFileFormat":
        """mastapy.nodal_analysis.fe_export_utility.FESubstructuringFileFormat

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_170.FESubstructuringFileFormat]":
        """List[mastapy.nodal_analysis.fe_export_utility.FESubstructuringFileFormat]

        Note:
            This property is readonly.
        """
        return None
