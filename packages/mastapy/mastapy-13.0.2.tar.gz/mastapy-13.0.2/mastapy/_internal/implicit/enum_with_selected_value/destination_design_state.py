"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
    _7000,
)
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_DestinationDesignState",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_DestinationDesignState")


class EnumWithSelectedValue_DestinationDesignState(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_DestinationDesignState

    A specific implementation of 'EnumWithSelectedValue' for 'DestinationDesignState' types.
    """

    __qualname__ = "DestinationDesignState"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_7000.DestinationDesignState":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _7000.DestinationDesignState

    @classmethod
    def implicit_type(cls) -> "_7000.DestinationDesignState.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _7000.DestinationDesignState.type_()

    @property
    def selected_value(self: Self) -> "_7000.DestinationDesignState":
        """mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.DestinationDesignState

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_7000.DestinationDesignState]":
        """List[mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.DestinationDesignState]

        Note:
            This property is readonly.
        """
        return None
