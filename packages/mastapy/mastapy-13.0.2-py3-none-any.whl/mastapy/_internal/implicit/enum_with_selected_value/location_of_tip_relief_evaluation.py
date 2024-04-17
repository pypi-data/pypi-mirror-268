"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.micro_geometry import _579
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LocationOfTipReliefEvaluation",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LocationOfTipReliefEvaluation")


class EnumWithSelectedValue_LocationOfTipReliefEvaluation(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_LocationOfTipReliefEvaluation

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfTipReliefEvaluation' types.
    """

    __qualname__ = "LocationOfTipReliefEvaluation"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_579.LocationOfTipReliefEvaluation":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _579.LocationOfTipReliefEvaluation

    @classmethod
    def implicit_type(cls) -> "_579.LocationOfTipReliefEvaluation.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _579.LocationOfTipReliefEvaluation.type_()

    @property
    def selected_value(self: Self) -> "_579.LocationOfTipReliefEvaluation":
        """mastapy.gears.micro_geometry.LocationOfTipReliefEvaluation

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_579.LocationOfTipReliefEvaluation]":
        """List[mastapy.gears.micro_geometry.LocationOfTipReliefEvaluation]

        Note:
            This property is readonly.
        """
        return None
