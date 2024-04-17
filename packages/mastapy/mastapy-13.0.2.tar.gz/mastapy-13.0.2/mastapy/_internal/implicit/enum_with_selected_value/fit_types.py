"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1402
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_FitTypes",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_FitTypes")


class EnumWithSelectedValue_FitTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FitTypes

    A specific implementation of 'EnumWithSelectedValue' for 'FitTypes' types.
    """

    __qualname__ = "FitTypes"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1402.FitTypes":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1402.FitTypes

    @classmethod
    def implicit_type(cls) -> "_1402.FitTypes.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1402.FitTypes.type_()

    @property
    def selected_value(self: Self) -> "_1402.FitTypes":
        """mastapy.detailed_rigid_connectors.splines.FitTypes

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1402.FitTypes]":
        """List[mastapy.detailed_rigid_connectors.splines.FitTypes]

        Note:
            This property is readonly.
        """
        return None
