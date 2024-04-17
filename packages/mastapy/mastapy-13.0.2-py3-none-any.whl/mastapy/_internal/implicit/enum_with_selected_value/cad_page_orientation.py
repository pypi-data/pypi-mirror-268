"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.utility.report import _1752
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_CadPageOrientation",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_CadPageOrientation")


class EnumWithSelectedValue_CadPageOrientation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CadPageOrientation

    A specific implementation of 'EnumWithSelectedValue' for 'CadPageOrientation' types.
    """

    __qualname__ = "CadPageOrientation"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1752.CadPageOrientation":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1752.CadPageOrientation

    @classmethod
    def implicit_type(cls) -> "_1752.CadPageOrientation.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1752.CadPageOrientation.type_()

    @property
    def selected_value(self: Self) -> "_1752.CadPageOrientation":
        """mastapy.utility.report.CadPageOrientation

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1752.CadPageOrientation]":
        """List[mastapy.utility.report.CadPageOrientation]

        Note:
            This property is readonly.
        """
        return None
