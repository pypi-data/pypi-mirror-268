"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.fe import _2370
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_BearingNodeOption",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_BearingNodeOption")


class EnumWithSelectedValue_BearingNodeOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingNodeOption

    A specific implementation of 'EnumWithSelectedValue' for 'BearingNodeOption' types.
    """

    __qualname__ = "BearingNodeOption"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_2370.BearingNodeOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2370.BearingNodeOption

    @classmethod
    def implicit_type(cls) -> "_2370.BearingNodeOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2370.BearingNodeOption.type_()

    @property
    def selected_value(self: Self) -> "_2370.BearingNodeOption":
        """mastapy.system_model.fe.BearingNodeOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_2370.BearingNodeOption]":
        """List[mastapy.system_model.fe.BearingNodeOption]

        Note:
            This property is readonly.
        """
        return None
