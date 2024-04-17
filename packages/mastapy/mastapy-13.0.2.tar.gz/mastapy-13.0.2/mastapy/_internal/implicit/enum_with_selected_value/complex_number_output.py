"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5772
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput",)


Self = TypeVar(
    "Self",
    bound="EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput",
)


class EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicAnalysisFEExportOptions.ComplexNumberOutput' types.
    """

    __qualname__ = "HarmonicAnalysisFEExportOptions.ComplexNumberOutput"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(
        cls,
    ) -> "_5772.HarmonicAnalysisFEExportOptions.ComplexNumberOutput":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5772.HarmonicAnalysisFEExportOptions.ComplexNumberOutput

    @classmethod
    def implicit_type(
        cls,
    ) -> "_5772.HarmonicAnalysisFEExportOptions.ComplexNumberOutput.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5772.HarmonicAnalysisFEExportOptions.ComplexNumberOutput.type_()

    @property
    def selected_value(
        self: Self,
    ) -> "_5772.HarmonicAnalysisFEExportOptions.ComplexNumberOutput":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisFEExportOptions.ComplexNumberOutput

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_5772.HarmonicAnalysisFEExportOptions.ComplexNumberOutput]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisFEExportOptions.ComplexNumberOutput]

        Note:
            This property is readonly.
        """
        return None
