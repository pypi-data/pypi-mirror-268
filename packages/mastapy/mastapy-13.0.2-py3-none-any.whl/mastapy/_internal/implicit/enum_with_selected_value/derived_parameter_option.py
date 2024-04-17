"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.gear_designs.creation_options import _1152
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = (
    "EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption",
)


Self = TypeVar(
    "Self",
    bound="EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption",
)


class EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalGearPairCreationOptions.DerivedParameterOption' types.
    """

    __qualname__ = "CylindricalGearPairCreationOptions.DerivedParameterOption"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(
        cls,
    ) -> "_1152.CylindricalGearPairCreationOptions.DerivedParameterOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1152.CylindricalGearPairCreationOptions.DerivedParameterOption

    @classmethod
    def implicit_type(
        cls,
    ) -> "_1152.CylindricalGearPairCreationOptions.DerivedParameterOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1152.CylindricalGearPairCreationOptions.DerivedParameterOption.type_()

    @property
    def selected_value(
        self: Self,
    ) -> "_1152.CylindricalGearPairCreationOptions.DerivedParameterOption":
        """mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions.DerivedParameterOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_1152.CylindricalGearPairCreationOptions.DerivedParameterOption]":
        """List[mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions.DerivedParameterOption]

        Note:
            This property is readonly.
        """
        return None
