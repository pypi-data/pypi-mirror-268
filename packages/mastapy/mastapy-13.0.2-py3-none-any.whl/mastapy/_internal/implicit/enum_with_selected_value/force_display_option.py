"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.electric_machines.harmonic_load_data import _1386
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ForceDisplayOption",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ForceDisplayOption")


class EnumWithSelectedValue_ForceDisplayOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ForceDisplayOption

    A specific implementation of 'EnumWithSelectedValue' for 'ForceDisplayOption' types.
    """

    __qualname__ = "ForceDisplayOption"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1386.ForceDisplayOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1386.ForceDisplayOption

    @classmethod
    def implicit_type(cls) -> "_1386.ForceDisplayOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1386.ForceDisplayOption.type_()

    @property
    def selected_value(self: Self) -> "_1386.ForceDisplayOption":
        """mastapy.electric_machines.harmonic_load_data.ForceDisplayOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1386.ForceDisplayOption]":
        """List[mastapy.electric_machines.harmonic_load_data.ForceDisplayOption]

        Note:
            This property is readonly.
        """
        return None
