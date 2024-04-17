"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.fe import _2405
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LinkNodeSource",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LinkNodeSource")


class EnumWithSelectedValue_LinkNodeSource(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LinkNodeSource

    A specific implementation of 'EnumWithSelectedValue' for 'LinkNodeSource' types.
    """

    __qualname__ = "LinkNodeSource"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_2405.LinkNodeSource":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2405.LinkNodeSource

    @classmethod
    def implicit_type(cls) -> "_2405.LinkNodeSource.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2405.LinkNodeSource.type_()

    @property
    def selected_value(self: Self) -> "_2405.LinkNodeSource":
        """mastapy.system_model.fe.LinkNodeSource

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_2405.LinkNodeSource]":
        """List[mastapy.system_model.fe.LinkNodeSource]

        Note:
            This property is readonly.
        """
        return None
