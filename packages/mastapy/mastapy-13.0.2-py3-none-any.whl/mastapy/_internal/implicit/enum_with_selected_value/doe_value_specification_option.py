"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4357
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_DoeValueSpecificationOption",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_DoeValueSpecificationOption")


class EnumWithSelectedValue_DoeValueSpecificationOption(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_DoeValueSpecificationOption

    A specific implementation of 'EnumWithSelectedValue' for 'DoeValueSpecificationOption' types.
    """

    __qualname__ = "DoeValueSpecificationOption"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_4357.DoeValueSpecificationOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _4357.DoeValueSpecificationOption

    @classmethod
    def implicit_type(cls) -> "_4357.DoeValueSpecificationOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _4357.DoeValueSpecificationOption.type_()

    @property
    def selected_value(self: Self) -> "_4357.DoeValueSpecificationOption":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.DoeValueSpecificationOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_4357.DoeValueSpecificationOption]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.DoeValueSpecificationOption]

        Note:
            This property is readonly.
        """
        return None
