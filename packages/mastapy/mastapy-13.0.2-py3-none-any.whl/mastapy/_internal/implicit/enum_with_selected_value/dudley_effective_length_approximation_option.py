"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1401
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption"
)


class EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption

    A specific implementation of 'EnumWithSelectedValue' for 'DudleyEffectiveLengthApproximationOption' types.
    """

    __qualname__ = "DudleyEffectiveLengthApproximationOption"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1401.DudleyEffectiveLengthApproximationOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1401.DudleyEffectiveLengthApproximationOption

    @classmethod
    def implicit_type(cls) -> "_1401.DudleyEffectiveLengthApproximationOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1401.DudleyEffectiveLengthApproximationOption.type_()

    @property
    def selected_value(self: Self) -> "_1401.DudleyEffectiveLengthApproximationOption":
        """mastapy.detailed_rigid_connectors.splines.DudleyEffectiveLengthApproximationOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_1401.DudleyEffectiveLengthApproximationOption]":
        """List[mastapy.detailed_rigid_connectors.splines.DudleyEffectiveLengthApproximationOption]

        Note:
            This property is readonly.
        """
        return None
