"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings.tolerances import _1911
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_BearingToleranceDefinitionOptions",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_BearingToleranceDefinitionOptions")


class EnumWithSelectedValue_BearingToleranceDefinitionOptions(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_BearingToleranceDefinitionOptions

    A specific implementation of 'EnumWithSelectedValue' for 'BearingToleranceDefinitionOptions' types.
    """

    __qualname__ = "BearingToleranceDefinitionOptions"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1911.BearingToleranceDefinitionOptions":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1911.BearingToleranceDefinitionOptions

    @classmethod
    def implicit_type(cls) -> "_1911.BearingToleranceDefinitionOptions.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1911.BearingToleranceDefinitionOptions.type_()

    @property
    def selected_value(self: Self) -> "_1911.BearingToleranceDefinitionOptions":
        """mastapy.bearings.tolerances.BearingToleranceDefinitionOptions

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1911.BearingToleranceDefinitionOptions]":
        """List[mastapy.bearings.tolerances.BearingToleranceDefinitionOptions]

        Note:
            This property is readonly.
        """
        return None
