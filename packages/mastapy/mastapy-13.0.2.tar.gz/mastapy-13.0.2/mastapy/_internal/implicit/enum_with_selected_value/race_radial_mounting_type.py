"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings.bearing_results import _1971
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_RaceRadialMountingType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_RaceRadialMountingType")


class EnumWithSelectedValue_RaceRadialMountingType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_RaceRadialMountingType

    A specific implementation of 'EnumWithSelectedValue' for 'RaceRadialMountingType' types.
    """

    __qualname__ = "RaceRadialMountingType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1971.RaceRadialMountingType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1971.RaceRadialMountingType

    @classmethod
    def implicit_type(cls) -> "_1971.RaceRadialMountingType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1971.RaceRadialMountingType.type_()

    @property
    def selected_value(self: Self) -> "_1971.RaceRadialMountingType":
        """mastapy.bearings.bearing_results.RaceRadialMountingType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1971.RaceRadialMountingType]":
        """List[mastapy.bearings.bearing_results.RaceRadialMountingType]

        Note:
            This property is readonly.
        """
        return None
