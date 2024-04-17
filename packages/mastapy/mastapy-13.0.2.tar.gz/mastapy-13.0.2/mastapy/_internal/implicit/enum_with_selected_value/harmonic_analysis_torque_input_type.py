"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5777
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_HarmonicAnalysisTorqueInputType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_HarmonicAnalysisTorqueInputType")


class EnumWithSelectedValue_HarmonicAnalysisTorqueInputType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_HarmonicAnalysisTorqueInputType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicAnalysisTorqueInputType' types.
    """

    __qualname__ = "HarmonicAnalysisTorqueInputType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_5777.HarmonicAnalysisTorqueInputType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5777.HarmonicAnalysisTorqueInputType

    @classmethod
    def implicit_type(cls) -> "_5777.HarmonicAnalysisTorqueInputType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5777.HarmonicAnalysisTorqueInputType.type_()

    @property
    def selected_value(self: Self) -> "_5777.HarmonicAnalysisTorqueInputType":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisTorqueInputType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_5777.HarmonicAnalysisTorqueInputType]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisTorqueInputType]

        Note:
            This property is readonly.
        """
        return None
