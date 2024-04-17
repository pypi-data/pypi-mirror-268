"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.electric_machines.harmonic_load_data import _1389
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_HarmonicLoadDataType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_HarmonicLoadDataType")


class EnumWithSelectedValue_HarmonicLoadDataType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_HarmonicLoadDataType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicLoadDataType' types.
    """

    __qualname__ = "HarmonicLoadDataType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1389.HarmonicLoadDataType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1389.HarmonicLoadDataType

    @classmethod
    def implicit_type(cls) -> "_1389.HarmonicLoadDataType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1389.HarmonicLoadDataType.type_()

    @property
    def selected_value(self: Self) -> "_1389.HarmonicLoadDataType":
        """mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1389.HarmonicLoadDataType]":
        """List[mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType]

        Note:
            This property is readonly.
        """
        return None
