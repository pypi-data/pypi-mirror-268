"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.fe_tools.vfx_tools.vfx_enums import _1246
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ProSolveSolverType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ProSolveSolverType")


class EnumWithSelectedValue_ProSolveSolverType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ProSolveSolverType

    A specific implementation of 'EnumWithSelectedValue' for 'ProSolveSolverType' types.
    """

    __qualname__ = "ProSolveSolverType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1246.ProSolveSolverType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1246.ProSolveSolverType

    @classmethod
    def implicit_type(cls) -> "_1246.ProSolveSolverType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1246.ProSolveSolverType.type_()

    @property
    def selected_value(self: Self) -> "_1246.ProSolveSolverType":
        """mastapy.fe_tools.vfx_tools.vfx_enums.ProSolveSolverType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1246.ProSolveSolverType]":
        """List[mastapy.fe_tools.vfx_tools.vfx_enums.ProSolveSolverType]

        Note:
            This property is readonly.
        """
        return None
