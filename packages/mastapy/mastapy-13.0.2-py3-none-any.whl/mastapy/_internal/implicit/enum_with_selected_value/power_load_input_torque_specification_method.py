"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model import _2224
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod"
)


class EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'PowerLoadInputTorqueSpecificationMethod' types.
    """

    __qualname__ = "PowerLoadInputTorqueSpecificationMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_2224.PowerLoadInputTorqueSpecificationMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2224.PowerLoadInputTorqueSpecificationMethod

    @classmethod
    def implicit_type(cls) -> "_2224.PowerLoadInputTorqueSpecificationMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2224.PowerLoadInputTorqueSpecificationMethod.type_()

    @property
    def selected_value(self: Self) -> "_2224.PowerLoadInputTorqueSpecificationMethod":
        """mastapy.system_model.PowerLoadInputTorqueSpecificationMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_2224.PowerLoadInputTorqueSpecificationMethod]":
        """List[mastapy.system_model.PowerLoadInputTorqueSpecificationMethod]

        Note:
            This property is readonly.
        """
        return None
