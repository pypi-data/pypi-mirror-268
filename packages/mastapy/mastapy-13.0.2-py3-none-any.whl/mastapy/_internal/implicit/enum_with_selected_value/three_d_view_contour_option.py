"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.utility.enums import _1828
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ThreeDViewContourOption",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ThreeDViewContourOption")


class EnumWithSelectedValue_ThreeDViewContourOption(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ThreeDViewContourOption

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOption' types.
    """

    __qualname__ = "ThreeDViewContourOption"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1828.ThreeDViewContourOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1828.ThreeDViewContourOption

    @classmethod
    def implicit_type(cls) -> "_1828.ThreeDViewContourOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1828.ThreeDViewContourOption.type_()

    @property
    def selected_value(self: Self) -> "_1828.ThreeDViewContourOption":
        """mastapy.utility.enums.ThreeDViewContourOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1828.ThreeDViewContourOption]":
        """List[mastapy.utility.enums.ThreeDViewContourOption]

        Note:
            This property is readonly.
        """
        return None
