"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.electric_machines.load_cases_and_analyses import _1379
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_SpecifyTorqueOrCurrent",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_SpecifyTorqueOrCurrent")


class EnumWithSelectedValue_SpecifyTorqueOrCurrent(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_SpecifyTorqueOrCurrent

    A specific implementation of 'EnumWithSelectedValue' for 'SpecifyTorqueOrCurrent' types.
    """

    __qualname__ = "SpecifyTorqueOrCurrent"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1379.SpecifyTorqueOrCurrent":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1379.SpecifyTorqueOrCurrent

    @classmethod
    def implicit_type(cls) -> "_1379.SpecifyTorqueOrCurrent.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1379.SpecifyTorqueOrCurrent.type_()

    @property
    def selected_value(self: Self) -> "_1379.SpecifyTorqueOrCurrent":
        """mastapy.electric_machines.load_cases_and_analyses.SpecifyTorqueOrCurrent

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1379.SpecifyTorqueOrCurrent]":
        """List[mastapy.electric_machines.load_cases_and_analyses.SpecifyTorqueOrCurrent]

        Note:
            This property is readonly.
        """
        return None
