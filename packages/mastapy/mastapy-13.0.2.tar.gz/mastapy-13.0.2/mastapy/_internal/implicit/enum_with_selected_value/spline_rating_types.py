"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1424
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_SplineRatingTypes",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_SplineRatingTypes")


class EnumWithSelectedValue_SplineRatingTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineRatingTypes

    A specific implementation of 'EnumWithSelectedValue' for 'SplineRatingTypes' types.
    """

    __qualname__ = "SplineRatingTypes"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1424.SplineRatingTypes":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1424.SplineRatingTypes

    @classmethod
    def implicit_type(cls) -> "_1424.SplineRatingTypes.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1424.SplineRatingTypes.type_()

    @property
    def selected_value(self: Self) -> "_1424.SplineRatingTypes":
        """mastapy.detailed_rigid_connectors.splines.SplineRatingTypes

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1424.SplineRatingTypes]":
        """List[mastapy.detailed_rigid_connectors.splines.SplineRatingTypes]

        Note:
            This property is readonly.
        """
        return None
