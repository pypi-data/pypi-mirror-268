"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.modal_analyses import _4635
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_DynamicsResponseType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_DynamicsResponseType")


class EnumWithSelectedValue_DynamicsResponseType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_DynamicsResponseType

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponseType' types.
    """

    __qualname__ = "DynamicsResponseType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_4635.DynamicsResponseType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _4635.DynamicsResponseType

    @classmethod
    def implicit_type(cls) -> "_4635.DynamicsResponseType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _4635.DynamicsResponseType.type_()

    @property
    def selected_value(self: Self) -> "_4635.DynamicsResponseType":
        """mastapy.system_model.analyses_and_results.modal_analyses.DynamicsResponseType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_4635.DynamicsResponseType]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.DynamicsResponseType]

        Note:
            This property is readonly.
        """
        return None
