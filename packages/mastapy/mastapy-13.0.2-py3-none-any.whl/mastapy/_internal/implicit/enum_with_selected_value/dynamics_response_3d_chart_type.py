"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.modal_analyses import _4634
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_DynamicsResponse3DChartType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_DynamicsResponse3DChartType")


class EnumWithSelectedValue_DynamicsResponse3DChartType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_DynamicsResponse3DChartType

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponse3DChartType' types.
    """

    __qualname__ = "DynamicsResponse3DChartType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_4634.DynamicsResponse3DChartType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _4634.DynamicsResponse3DChartType

    @classmethod
    def implicit_type(cls) -> "_4634.DynamicsResponse3DChartType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _4634.DynamicsResponse3DChartType.type_()

    @property
    def selected_value(self: Self) -> "_4634.DynamicsResponse3DChartType":
        """mastapy.system_model.analyses_and_results.modal_analyses.DynamicsResponse3DChartType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_4634.DynamicsResponse3DChartType]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.DynamicsResponse3DChartType]

        Note:
            This property is readonly.
        """
        return None
