"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis import _78
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ModeInputType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ModeInputType")


class EnumWithSelectedValue_ModeInputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ModeInputType

    A specific implementation of 'EnumWithSelectedValue' for 'ModeInputType' types.
    """

    __qualname__ = "ModeInputType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_78.ModeInputType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _78.ModeInputType

    @classmethod
    def implicit_type(cls) -> "_78.ModeInputType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _78.ModeInputType.type_()

    @property
    def selected_value(self: Self) -> "_78.ModeInputType":
        """mastapy.nodal_analysis.ModeInputType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_78.ModeInputType]":
        """List[mastapy.nodal_analysis.ModeInputType]

        Note:
            This property is readonly.
        """
        return None
