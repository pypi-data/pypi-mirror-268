"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1425
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_SplineToleranceClassTypes",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_SplineToleranceClassTypes")


class EnumWithSelectedValue_SplineToleranceClassTypes(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_SplineToleranceClassTypes

    A specific implementation of 'EnumWithSelectedValue' for 'SplineToleranceClassTypes' types.
    """

    __qualname__ = "SplineToleranceClassTypes"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1425.SplineToleranceClassTypes":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1425.SplineToleranceClassTypes

    @classmethod
    def implicit_type(cls) -> "_1425.SplineToleranceClassTypes.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1425.SplineToleranceClassTypes.type_()

    @property
    def selected_value(self: Self) -> "_1425.SplineToleranceClassTypes":
        """mastapy.detailed_rigid_connectors.splines.SplineToleranceClassTypes

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1425.SplineToleranceClassTypes]":
        """List[mastapy.detailed_rigid_connectors.splines.SplineToleranceClassTypes]

        Note:
            This property is readonly.
        """
        return None
