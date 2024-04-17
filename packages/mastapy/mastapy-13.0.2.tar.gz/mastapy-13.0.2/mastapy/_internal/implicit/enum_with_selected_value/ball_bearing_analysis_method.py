"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings.bearing_results.rolling import _1973
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_BallBearingAnalysisMethod",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_BallBearingAnalysisMethod")


class EnumWithSelectedValue_BallBearingAnalysisMethod(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_BallBearingAnalysisMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BallBearingAnalysisMethod' types.
    """

    __qualname__ = "BallBearingAnalysisMethod"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1973.BallBearingAnalysisMethod":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1973.BallBearingAnalysisMethod

    @classmethod
    def implicit_type(cls) -> "_1973.BallBearingAnalysisMethod.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1973.BallBearingAnalysisMethod.type_()

    @property
    def selected_value(self: Self) -> "_1973.BallBearingAnalysisMethod":
        """mastapy.bearings.bearing_results.rolling.BallBearingAnalysisMethod

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1973.BallBearingAnalysisMethod]":
        """List[mastapy.bearings.bearing_results.rolling.BallBearingAnalysisMethod]

        Note:
            This property is readonly.
        """
        return None
