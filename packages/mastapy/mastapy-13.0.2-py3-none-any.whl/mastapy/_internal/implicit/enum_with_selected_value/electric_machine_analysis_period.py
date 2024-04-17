"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis.elmer import _172
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ElectricMachineAnalysisPeriod",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ElectricMachineAnalysisPeriod")


class EnumWithSelectedValue_ElectricMachineAnalysisPeriod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ElectricMachineAnalysisPeriod

    A specific implementation of 'EnumWithSelectedValue' for 'ElectricMachineAnalysisPeriod' types.
    """

    __qualname__ = "ElectricMachineAnalysisPeriod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_172.ElectricMachineAnalysisPeriod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _172.ElectricMachineAnalysisPeriod

    @classmethod
    def implicit_type(cls) -> "_172.ElectricMachineAnalysisPeriod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _172.ElectricMachineAnalysisPeriod.type_()

    @property
    def selected_value(self: Self) -> "_172.ElectricMachineAnalysisPeriod":
        """mastapy.nodal_analysis.elmer.ElectricMachineAnalysisPeriod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_172.ElectricMachineAnalysisPeriod]":
        """List[mastapy.nodal_analysis.elmer.ElectricMachineAnalysisPeriod]

        Note:
            This property is readonly.
        """
        return None
