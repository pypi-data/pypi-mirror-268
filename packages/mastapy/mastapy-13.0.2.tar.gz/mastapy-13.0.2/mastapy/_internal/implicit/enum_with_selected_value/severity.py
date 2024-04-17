"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.utility.model_validation import _1799
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_Severity",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_Severity")


class EnumWithSelectedValue_Severity(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Severity

    A specific implementation of 'EnumWithSelectedValue' for 'Severity' types.
    """

    __qualname__ = "Severity"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1799.Severity":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1799.Severity

    @classmethod
    def implicit_type(cls) -> "_1799.Severity.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1799.Severity.type_()

    @property
    def selected_value(self: Self) -> "_1799.Severity":
        """mastapy.utility.model_validation.Severity

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1799.Severity]":
        """List[mastapy.utility.model_validation.Severity]

        Note:
            This property is readonly.
        """
        return None
