"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6826
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_AnalysisType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_AnalysisType")


class EnumWithSelectedValue_AnalysisType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AnalysisType

    A specific implementation of 'EnumWithSelectedValue' for 'AnalysisType' types.
    """

    __qualname__ = "AnalysisType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_6826.AnalysisType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6826.AnalysisType

    @classmethod
    def implicit_type(cls) -> "_6826.AnalysisType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6826.AnalysisType.type_()

    @property
    def selected_value(self: Self) -> "_6826.AnalysisType":
        """mastapy.system_model.analyses_and_results.static_loads.AnalysisType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_6826.AnalysisType]":
        """List[mastapy.system_model.analyses_and_results.static_loads.AnalysisType]

        Note:
            This property is readonly.
        """
        return None
