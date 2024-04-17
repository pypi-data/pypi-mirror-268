"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.gear_designs.conical import _1163
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ConicalMachineSettingCalculationMethods",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_ConicalMachineSettingCalculationMethods"
)


class EnumWithSelectedValue_ConicalMachineSettingCalculationMethods(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ConicalMachineSettingCalculationMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ConicalMachineSettingCalculationMethods' types.
    """

    __qualname__ = "ConicalMachineSettingCalculationMethods"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1163.ConicalMachineSettingCalculationMethods":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1163.ConicalMachineSettingCalculationMethods

    @classmethod
    def implicit_type(cls) -> "_1163.ConicalMachineSettingCalculationMethods.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1163.ConicalMachineSettingCalculationMethods.type_()

    @property
    def selected_value(self: Self) -> "_1163.ConicalMachineSettingCalculationMethods":
        """mastapy.gears.gear_designs.conical.ConicalMachineSettingCalculationMethods

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_1163.ConicalMachineSettingCalculationMethods]":
        """List[mastapy.gears.gear_designs.conical.ConicalMachineSettingCalculationMethods]

        Note:
            This property is readonly.
        """
        return None
