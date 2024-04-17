"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings.bearing_results import _1970
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_RaceAxialMountingType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_RaceAxialMountingType")


class EnumWithSelectedValue_RaceAxialMountingType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_RaceAxialMountingType

    A specific implementation of 'EnumWithSelectedValue' for 'RaceAxialMountingType' types.
    """

    __qualname__ = "RaceAxialMountingType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1970.RaceAxialMountingType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1970.RaceAxialMountingType

    @classmethod
    def implicit_type(cls) -> "_1970.RaceAxialMountingType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1970.RaceAxialMountingType.type_()

    @property
    def selected_value(self: Self) -> "_1970.RaceAxialMountingType":
        """mastapy.bearings.bearing_results.RaceAxialMountingType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1970.RaceAxialMountingType]":
        """List[mastapy.bearings.bearing_results.RaceAxialMountingType]

        Note:
            This property is readonly.
        """
        return None
