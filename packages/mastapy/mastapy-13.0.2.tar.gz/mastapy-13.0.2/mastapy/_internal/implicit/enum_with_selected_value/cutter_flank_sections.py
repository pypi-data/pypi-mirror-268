"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.manufacturing.cylindrical import _612
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_CutterFlankSections",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_CutterFlankSections")


class EnumWithSelectedValue_CutterFlankSections(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_CutterFlankSections

    A specific implementation of 'EnumWithSelectedValue' for 'CutterFlankSections' types.
    """

    __qualname__ = "CutterFlankSections"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_612.CutterFlankSections":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _612.CutterFlankSections

    @classmethod
    def implicit_type(cls) -> "_612.CutterFlankSections.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _612.CutterFlankSections.type_()

    @property
    def selected_value(self: Self) -> "_612.CutterFlankSections":
        """mastapy.gears.manufacturing.cylindrical.CutterFlankSections

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_612.CutterFlankSections]":
        """List[mastapy.gears.manufacturing.cylindrical.CutterFlankSections]

        Note:
            This property is readonly.
        """
        return None
