"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""

from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5826
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation",)


Self = TypeVar(
    "Self",
    bound="EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation",
)


class EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation

    A specific implementation of 'EnumWithSelectedValue' for 'StiffnessOptionsForHarmonicAnalysis.StepCreation' types.
    """

    __qualname__ = "StiffnessOptionsForHarmonicAnalysis.StepCreation"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_5826.StiffnessOptionsForHarmonicAnalysis.StepCreation":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5826.StiffnessOptionsForHarmonicAnalysis.StepCreation

    @classmethod
    def implicit_type(
        cls,
    ) -> "_5826.StiffnessOptionsForHarmonicAnalysis.StepCreation.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5826.StiffnessOptionsForHarmonicAnalysis.StepCreation.type_()

    @property
    def selected_value(
        self: Self,
    ) -> "_5826.StiffnessOptionsForHarmonicAnalysis.StepCreation":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StiffnessOptionsForHarmonicAnalysis.StepCreation

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_5826.StiffnessOptionsForHarmonicAnalysis.StepCreation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StiffnessOptionsForHarmonicAnalysis.StepCreation]

        Note:
            This property is readonly.
        """
        return None
