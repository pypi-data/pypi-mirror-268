"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _661
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ActiveProcessMethod",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ActiveProcessMethod")


class EnumWithSelectedValue_ActiveProcessMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ActiveProcessMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ActiveProcessMethod' types.
    """

    __qualname__ = "ActiveProcessMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_661.ActiveProcessMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _661.ActiveProcessMethod

    @classmethod
    def implicit_type(cls) -> "_661.ActiveProcessMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _661.ActiveProcessMethod.type_()

    @property
    def selected_value(self: Self) -> "_661.ActiveProcessMethod":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ActiveProcessMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_661.ActiveProcessMethod]":
        """List[mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ActiveProcessMethod]

        Note:
            This property is readonly.
        """
        return None
