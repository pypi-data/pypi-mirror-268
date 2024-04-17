"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.fe_tools.enums import _1248
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_MaterialPropertyClass",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_MaterialPropertyClass")


class EnumWithSelectedValue_MaterialPropertyClass(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_MaterialPropertyClass

    A specific implementation of 'EnumWithSelectedValue' for 'MaterialPropertyClass' types.
    """

    __qualname__ = "MaterialPropertyClass"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1248.MaterialPropertyClass":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1248.MaterialPropertyClass

    @classmethod
    def implicit_type(cls) -> "_1248.MaterialPropertyClass.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1248.MaterialPropertyClass.type_()

    @property
    def selected_value(self: Self) -> "_1248.MaterialPropertyClass":
        """mastapy.fe_tools.enums.MaterialPropertyClass

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1248.MaterialPropertyClass]":
        """List[mastapy.fe_tools.enums.MaterialPropertyClass]

        Note:
            This property is readonly.
        """
        return None
