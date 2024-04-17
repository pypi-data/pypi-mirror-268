"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.utility.model_validation import _1802
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_StatusItemSeverity",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_StatusItemSeverity")


class EnumWithSelectedValue_StatusItemSeverity(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StatusItemSeverity

    A specific implementation of 'EnumWithSelectedValue' for 'StatusItemSeverity' types.
    """

    __qualname__ = "StatusItemSeverity"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1802.StatusItemSeverity":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1802.StatusItemSeverity

    @classmethod
    def implicit_type(cls) -> "_1802.StatusItemSeverity.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1802.StatusItemSeverity.type_()

    @property
    def selected_value(self: Self) -> "_1802.StatusItemSeverity":
        """mastapy.utility.model_validation.StatusItemSeverity

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1802.StatusItemSeverity]":
        """List[mastapy.utility.model_validation.StatusItemSeverity]

        Note:
            This property is readonly.
        """
        return None
