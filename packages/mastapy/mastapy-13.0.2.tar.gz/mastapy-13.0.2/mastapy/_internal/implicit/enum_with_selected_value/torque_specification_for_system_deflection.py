"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6986
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_TorqueSpecificationForSystemDeflection",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_TorqueSpecificationForSystemDeflection"
)


class EnumWithSelectedValue_TorqueSpecificationForSystemDeflection(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_TorqueSpecificationForSystemDeflection

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueSpecificationForSystemDeflection' types.
    """

    __qualname__ = "TorqueSpecificationForSystemDeflection"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_6986.TorqueSpecificationForSystemDeflection":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6986.TorqueSpecificationForSystemDeflection

    @classmethod
    def implicit_type(cls) -> "_6986.TorqueSpecificationForSystemDeflection.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6986.TorqueSpecificationForSystemDeflection.type_()

    @property
    def selected_value(self: Self) -> "_6986.TorqueSpecificationForSystemDeflection":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueSpecificationForSystemDeflection

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_6986.TorqueSpecificationForSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.static_loads.TorqueSpecificationForSystemDeflection]

        Note:
            This property is readonly.
        """
        return None
