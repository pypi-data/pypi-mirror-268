"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.micro_geometry import _577
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LocationOfEvaluationUpperLimit",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LocationOfEvaluationUpperLimit")


class EnumWithSelectedValue_LocationOfEvaluationUpperLimit(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_LocationOfEvaluationUpperLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationUpperLimit' types.
    """

    __qualname__ = "LocationOfEvaluationUpperLimit"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_577.LocationOfEvaluationUpperLimit":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _577.LocationOfEvaluationUpperLimit

    @classmethod
    def implicit_type(cls) -> "_577.LocationOfEvaluationUpperLimit.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _577.LocationOfEvaluationUpperLimit.type_()

    @property
    def selected_value(self: Self) -> "_577.LocationOfEvaluationUpperLimit":
        """mastapy.gears.micro_geometry.LocationOfEvaluationUpperLimit

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_577.LocationOfEvaluationUpperLimit]":
        """List[mastapy.gears.micro_geometry.LocationOfEvaluationUpperLimit]

        Note:
            This property is readonly.
        """
        return None
