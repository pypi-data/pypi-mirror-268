"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.micro_geometry import _578
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LocationOfRootReliefEvaluation",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LocationOfRootReliefEvaluation")


class EnumWithSelectedValue_LocationOfRootReliefEvaluation(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_LocationOfRootReliefEvaluation

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfRootReliefEvaluation' types.
    """

    __qualname__ = "LocationOfRootReliefEvaluation"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_578.LocationOfRootReliefEvaluation":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _578.LocationOfRootReliefEvaluation

    @classmethod
    def implicit_type(cls) -> "_578.LocationOfRootReliefEvaluation.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _578.LocationOfRootReliefEvaluation.type_()

    @property
    def selected_value(self: Self) -> "_578.LocationOfRootReliefEvaluation":
        """mastapy.gears.micro_geometry.LocationOfRootReliefEvaluation

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_578.LocationOfRootReliefEvaluation]":
        """List[mastapy.gears.micro_geometry.LocationOfRootReliefEvaluation]

        Note:
            This property is readonly.
        """
        return None
