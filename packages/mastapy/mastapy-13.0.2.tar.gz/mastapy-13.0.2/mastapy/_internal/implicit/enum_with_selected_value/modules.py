"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1410
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_Modules",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_Modules")


class EnumWithSelectedValue_Modules(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Modules

    A specific implementation of 'EnumWithSelectedValue' for 'Modules' types.
    """

    __qualname__ = "Modules"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1410.Modules":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1410.Modules

    @classmethod
    def implicit_type(cls) -> "_1410.Modules.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1410.Modules.type_()

    @property
    def selected_value(self: Self) -> "_1410.Modules":
        """mastapy.detailed_rigid_connectors.splines.Modules

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1410.Modules]":
        """List[mastapy.detailed_rigid_connectors.splines.Modules]

        Note:
            This property is readonly.
        """
        return None
