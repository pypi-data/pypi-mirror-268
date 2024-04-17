"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model import _2211
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_DesignEntityId",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_DesignEntityId")


class EnumWithSelectedValue_DesignEntityId(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DesignEntityId

    A specific implementation of 'EnumWithSelectedValue' for 'DesignEntityId' types.
    """

    __qualname__ = "DesignEntityId"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_2211.DesignEntityId":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2211.DesignEntityId

    @classmethod
    def implicit_type(cls) -> "_2211.DesignEntityId.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2211.DesignEntityId.type_()

    @property
    def selected_value(self: Self) -> "_2211.DesignEntityId":
        """mastapy.system_model.DesignEntityId

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_2211.DesignEntityId]":
        """List[mastapy.system_model.DesignEntityId]

        Note:
            This property is readonly.
        """
        return None
