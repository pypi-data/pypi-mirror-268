"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.gear_designs.bevel import _1185
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods"
)


class EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods

    A specific implementation of 'EnumWithSelectedValue' for 'AGMAGleasonConicalGearGeometryMethods' types.
    """

    __qualname__ = "AGMAGleasonConicalGearGeometryMethods"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1185.AGMAGleasonConicalGearGeometryMethods":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1185.AGMAGleasonConicalGearGeometryMethods

    @classmethod
    def implicit_type(cls) -> "_1185.AGMAGleasonConicalGearGeometryMethods.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1185.AGMAGleasonConicalGearGeometryMethods.type_()

    @property
    def selected_value(self: Self) -> "_1185.AGMAGleasonConicalGearGeometryMethods":
        """mastapy.gears.gear_designs.bevel.AGMAGleasonConicalGearGeometryMethods

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_1185.AGMAGleasonConicalGearGeometryMethods]":
        """List[mastapy.gears.gear_designs.bevel.AGMAGleasonConicalGearGeometryMethods]

        Note:
            This property is readonly.
        """
        return None
