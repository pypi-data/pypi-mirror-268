"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis.nodal_entities import _133
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ShearAreaFactorMethod",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ShearAreaFactorMethod")


class EnumWithSelectedValue_ShearAreaFactorMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ShearAreaFactorMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ShearAreaFactorMethod' types.
    """

    __qualname__ = "ShearAreaFactorMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_133.ShearAreaFactorMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _133.ShearAreaFactorMethod

    @classmethod
    def implicit_type(cls) -> "_133.ShearAreaFactorMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _133.ShearAreaFactorMethod.type_()

    @property
    def selected_value(self: Self) -> "_133.ShearAreaFactorMethod":
        """mastapy.nodal_analysis.nodal_entities.ShearAreaFactorMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_133.ShearAreaFactorMethod]":
        """List[mastapy.nodal_analysis.nodal_entities.ShearAreaFactorMethod]

        Note:
            This property is readonly.
        """
        return None
