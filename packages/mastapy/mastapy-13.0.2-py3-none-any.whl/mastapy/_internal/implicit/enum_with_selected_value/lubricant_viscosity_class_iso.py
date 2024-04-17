"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.materials import _268
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LubricantViscosityClassISO",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LubricantViscosityClassISO")


class EnumWithSelectedValue_LubricantViscosityClassISO(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_LubricantViscosityClassISO

    A specific implementation of 'EnumWithSelectedValue' for 'LubricantViscosityClassISO' types.
    """

    __qualname__ = "LubricantViscosityClassISO"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_268.LubricantViscosityClassISO":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _268.LubricantViscosityClassISO

    @classmethod
    def implicit_type(cls) -> "_268.LubricantViscosityClassISO.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _268.LubricantViscosityClassISO.type_()

    @property
    def selected_value(self: Self) -> "_268.LubricantViscosityClassISO":
        """mastapy.materials.LubricantViscosityClassISO

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_268.LubricantViscosityClassISO]":
        """List[mastapy.materials.LubricantViscosityClassISO]

        Note:
            This property is readonly.
        """
        return None
