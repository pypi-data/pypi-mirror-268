"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.manufacturing.cylindrical import _630
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_Flank",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_Flank")


class EnumWithSelectedValue_Flank(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Flank

    A specific implementation of 'EnumWithSelectedValue' for 'Flank' types.
    """

    __qualname__ = "Flank"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_630.Flank":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _630.Flank

    @classmethod
    def implicit_type(cls) -> "_630.Flank.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _630.Flank.type_()

    @property
    def selected_value(self: Self) -> "_630.Flank":
        """mastapy.gears.manufacturing.cylindrical.Flank

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_630.Flank]":
        """List[mastapy.gears.manufacturing.cylindrical.Flank]

        Note:
            This property is readonly.
        """
        return None
