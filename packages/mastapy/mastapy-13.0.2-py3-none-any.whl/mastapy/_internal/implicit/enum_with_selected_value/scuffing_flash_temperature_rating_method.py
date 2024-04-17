"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.rating.cylindrical import _484
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod"
)


class EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingFlashTemperatureRatingMethod' types.
    """

    __qualname__ = "ScuffingFlashTemperatureRatingMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_484.ScuffingFlashTemperatureRatingMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _484.ScuffingFlashTemperatureRatingMethod

    @classmethod
    def implicit_type(cls) -> "_484.ScuffingFlashTemperatureRatingMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _484.ScuffingFlashTemperatureRatingMethod.type_()

    @property
    def selected_value(self: Self) -> "_484.ScuffingFlashTemperatureRatingMethod":
        """mastapy.gears.rating.cylindrical.ScuffingFlashTemperatureRatingMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_484.ScuffingFlashTemperatureRatingMethod]":
        """List[mastapy.gears.rating.cylindrical.ScuffingFlashTemperatureRatingMethod]

        Note:
            This property is readonly.
        """
        return None
