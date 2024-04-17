"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings import _1884
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_BearingModel",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_BearingModel")


class EnumWithSelectedValue_BearingModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingModel

    A specific implementation of 'EnumWithSelectedValue' for 'BearingModel' types.
    """

    __qualname__ = "BearingModel"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1884.BearingModel":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1884.BearingModel

    @classmethod
    def implicit_type(cls) -> "_1884.BearingModel.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1884.BearingModel.type_()

    @property
    def selected_value(self: Self) -> "_1884.BearingModel":
        """mastapy.bearings.BearingModel

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1884.BearingModel]":
        """List[mastapy.bearings.BearingModel]

        Note:
            This property is readonly.
        """
        return None
