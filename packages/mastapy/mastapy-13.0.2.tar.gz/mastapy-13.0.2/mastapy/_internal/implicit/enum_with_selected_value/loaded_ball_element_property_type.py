"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings.bearing_results import _1969
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LoadedBallElementPropertyType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LoadedBallElementPropertyType")


class EnumWithSelectedValue_LoadedBallElementPropertyType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_LoadedBallElementPropertyType

    A specific implementation of 'EnumWithSelectedValue' for 'LoadedBallElementPropertyType' types.
    """

    __qualname__ = "LoadedBallElementPropertyType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1969.LoadedBallElementPropertyType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1969.LoadedBallElementPropertyType

    @classmethod
    def implicit_type(cls) -> "_1969.LoadedBallElementPropertyType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1969.LoadedBallElementPropertyType.type_()

    @property
    def selected_value(self: Self) -> "_1969.LoadedBallElementPropertyType":
        """mastapy.bearings.bearing_results.LoadedBallElementPropertyType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1969.LoadedBallElementPropertyType]":
        """List[mastapy.bearings.bearing_results.LoadedBallElementPropertyType]

        Note:
            This property is readonly.
        """
        return None
