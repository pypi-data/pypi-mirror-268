"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6947
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification"
)


class EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification

    A specific implementation of 'EnumWithSelectedValue' for 'PointLoadLoadCase.ForceSpecification' types.
    """

    __qualname__ = "PointLoadLoadCase.ForceSpecification"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_6947.PointLoadLoadCase.ForceSpecification":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6947.PointLoadLoadCase.ForceSpecification

    @classmethod
    def implicit_type(cls) -> "_6947.PointLoadLoadCase.ForceSpecification.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6947.PointLoadLoadCase.ForceSpecification.type_()

    @property
    def selected_value(self: Self) -> "_6947.PointLoadLoadCase.ForceSpecification":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase.ForceSpecification

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_6947.PointLoadLoadCase.ForceSpecification]":
        """List[mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase.ForceSpecification]

        Note:
            This property is readonly.
        """
        return None
