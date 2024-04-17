"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings import _1891
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_FluidFilmTemperatureOptions",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_FluidFilmTemperatureOptions")


class EnumWithSelectedValue_FluidFilmTemperatureOptions(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_FluidFilmTemperatureOptions

    A specific implementation of 'EnumWithSelectedValue' for 'FluidFilmTemperatureOptions' types.
    """

    __qualname__ = "FluidFilmTemperatureOptions"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1891.FluidFilmTemperatureOptions":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1891.FluidFilmTemperatureOptions

    @classmethod
    def implicit_type(cls) -> "_1891.FluidFilmTemperatureOptions.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1891.FluidFilmTemperatureOptions.type_()

    @property
    def selected_value(self: Self) -> "_1891.FluidFilmTemperatureOptions":
        """mastapy.bearings.FluidFilmTemperatureOptions

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1891.FluidFilmTemperatureOptions]":
        """List[mastapy.bearings.FluidFilmTemperatureOptions]

        Note:
            This property is readonly.
        """
        return None
