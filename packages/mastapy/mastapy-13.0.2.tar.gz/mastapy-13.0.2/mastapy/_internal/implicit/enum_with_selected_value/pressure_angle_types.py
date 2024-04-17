"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1411
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_PressureAngleTypes",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_PressureAngleTypes")


class EnumWithSelectedValue_PressureAngleTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PressureAngleTypes

    A specific implementation of 'EnumWithSelectedValue' for 'PressureAngleTypes' types.
    """

    __qualname__ = "PressureAngleTypes"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1411.PressureAngleTypes":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1411.PressureAngleTypes

    @classmethod
    def implicit_type(cls) -> "_1411.PressureAngleTypes.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1411.PressureAngleTypes.type_()

    @property
    def selected_value(self: Self) -> "_1411.PressureAngleTypes":
        """mastapy.detailed_rigid_connectors.splines.PressureAngleTypes

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1411.PressureAngleTypes]":
        """List[mastapy.detailed_rigid_connectors.splines.PressureAngleTypes]

        Note:
            This property is readonly.
        """
        return None
