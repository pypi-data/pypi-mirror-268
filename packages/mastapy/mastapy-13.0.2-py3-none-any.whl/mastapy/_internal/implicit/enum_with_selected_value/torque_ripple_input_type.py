"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6985
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_TorqueRippleInputType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_TorqueRippleInputType")


class EnumWithSelectedValue_TorqueRippleInputType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_TorqueRippleInputType

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueRippleInputType' types.
    """

    __qualname__ = "TorqueRippleInputType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_6985.TorqueRippleInputType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6985.TorqueRippleInputType

    @classmethod
    def implicit_type(cls) -> "_6985.TorqueRippleInputType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6985.TorqueRippleInputType.type_()

    @property
    def selected_value(self: Self) -> "_6985.TorqueRippleInputType":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueRippleInputType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_6985.TorqueRippleInputType]":
        """List[mastapy.system_model.analyses_and_results.static_loads.TorqueRippleInputType]

        Note:
            This property is readonly.
        """
        return None
