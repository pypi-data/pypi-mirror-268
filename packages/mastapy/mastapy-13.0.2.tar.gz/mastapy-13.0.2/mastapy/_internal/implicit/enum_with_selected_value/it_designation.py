"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings.tolerances import _1917
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ITDesignation",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ITDesignation")


class EnumWithSelectedValue_ITDesignation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ITDesignation

    A specific implementation of 'EnumWithSelectedValue' for 'ITDesignation' types.
    """

    __qualname__ = "ITDesignation"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1917.ITDesignation":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1917.ITDesignation

    @classmethod
    def implicit_type(cls) -> "_1917.ITDesignation.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1917.ITDesignation.type_()

    @property
    def selected_value(self: Self) -> "_1917.ITDesignation":
        """mastapy.bearings.tolerances.ITDesignation

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1917.ITDesignation]":
        """List[mastapy.bearings.tolerances.ITDesignation]

        Note:
            This property is readonly.
        """
        return None
