"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.gear_designs.conical import _1175
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_LoadDistributionFactorMethods",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_LoadDistributionFactorMethods")


class EnumWithSelectedValue_LoadDistributionFactorMethods(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_LoadDistributionFactorMethods

    A specific implementation of 'EnumWithSelectedValue' for 'LoadDistributionFactorMethods' types.
    """

    __qualname__ = "LoadDistributionFactorMethods"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1175.LoadDistributionFactorMethods":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1175.LoadDistributionFactorMethods

    @classmethod
    def implicit_type(cls) -> "_1175.LoadDistributionFactorMethods.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1175.LoadDistributionFactorMethods.type_()

    @property
    def selected_value(self: Self) -> "_1175.LoadDistributionFactorMethods":
        """mastapy.gears.gear_designs.conical.LoadDistributionFactorMethods

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1175.LoadDistributionFactorMethods]":
        """List[mastapy.gears.gear_designs.conical.LoadDistributionFactorMethods]

        Note:
            This property is readonly.
        """
        return None
