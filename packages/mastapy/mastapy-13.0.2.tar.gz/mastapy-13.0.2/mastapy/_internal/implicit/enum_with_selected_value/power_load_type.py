"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model import _2226
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_PowerLoadType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_PowerLoadType")


class EnumWithSelectedValue_PowerLoadType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PowerLoadType

    A specific implementation of 'EnumWithSelectedValue' for 'PowerLoadType' types.
    """

    __qualname__ = "PowerLoadType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_2226.PowerLoadType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2226.PowerLoadType

    @classmethod
    def implicit_type(cls) -> "_2226.PowerLoadType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2226.PowerLoadType.type_()

    @property
    def selected_value(self: Self) -> "_2226.PowerLoadType":
        """mastapy.system_model.PowerLoadType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_2226.PowerLoadType]":
        """List[mastapy.system_model.PowerLoadType]

        Note:
            This property is readonly.
        """
        return None
