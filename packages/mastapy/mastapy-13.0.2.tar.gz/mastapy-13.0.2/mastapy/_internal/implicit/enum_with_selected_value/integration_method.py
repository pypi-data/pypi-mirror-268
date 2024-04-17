"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis import _71
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_IntegrationMethod",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_IntegrationMethod")


class EnumWithSelectedValue_IntegrationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_IntegrationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'IntegrationMethod' types.
    """

    __qualname__ = "IntegrationMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_71.IntegrationMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _71.IntegrationMethod

    @classmethod
    def implicit_type(cls) -> "_71.IntegrationMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _71.IntegrationMethod.type_()

    @property
    def selected_value(self: Self) -> "_71.IntegrationMethod":
        """mastapy.nodal_analysis.IntegrationMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_71.IntegrationMethod]":
        """List[mastapy.nodal_analysis.IntegrationMethod]

        Note:
            This property is readonly.
        """
        return None
