"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.electric_machines.load_cases_and_analyses import _1371
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LoadCaseType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LoadCaseType")


class EnumWithSelectedValue_LoadCaseType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LoadCaseType

    A specific implementation of 'EnumWithSelectedValue' for 'LoadCaseType' types.
    """

    __qualname__ = "LoadCaseType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1371.LoadCaseType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1371.LoadCaseType

    @classmethod
    def implicit_type(cls) -> "_1371.LoadCaseType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1371.LoadCaseType.type_()

    @property
    def selected_value(self: Self) -> "_1371.LoadCaseType":
        """mastapy.electric_machines.load_cases_and_analyses.LoadCaseType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1371.LoadCaseType]":
        """List[mastapy.electric_machines.load_cases_and_analyses.LoadCaseType]

        Note:
            This property is readonly.
        """
        return None
