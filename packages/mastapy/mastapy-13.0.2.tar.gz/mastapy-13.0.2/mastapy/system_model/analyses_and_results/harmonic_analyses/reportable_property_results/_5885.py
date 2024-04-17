"""RootAssemblySingleWhineAnalysisResultsPropertyAccessor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5862,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5878,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblySingleWhineAnalysisResultsPropertyAccessor",)


Self = TypeVar("Self", bound="RootAssemblySingleWhineAnalysisResultsPropertyAccessor")


class RootAssemblySingleWhineAnalysisResultsPropertyAccessor(
    _5862.AbstractSingleWhineAnalysisResultsPropertyAccessor
):
    """RootAssemblySingleWhineAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
    )

    class _Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor:
        """Special nested class for casting RootAssemblySingleWhineAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(
            self: "RootAssemblySingleWhineAnalysisResultsPropertyAccessor._Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
            parent: "RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
        ):
            self._parent = parent

        @property
        def abstract_single_whine_analysis_results_property_accessor(
            self: "RootAssemblySingleWhineAnalysisResultsPropertyAccessor._Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
        ) -> "_5862.AbstractSingleWhineAnalysisResultsPropertyAccessor":
            return self._parent._cast(
                _5862.AbstractSingleWhineAnalysisResultsPropertyAccessor
            )

        @property
        def root_assembly_single_whine_analysis_results_property_accessor(
            self: "RootAssemblySingleWhineAnalysisResultsPropertyAccessor._Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
        ) -> "RootAssemblySingleWhineAnalysisResultsPropertyAccessor":
            return self._parent

        def __getattr__(
            self: "RootAssemblySingleWhineAnalysisResultsPropertyAccessor._Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "RootAssemblySingleWhineAnalysisResultsPropertyAccessor.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orders(self: Self) -> "List[_5878.ResultsForOrderIncludingGroups]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForOrderIncludingGroups]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Orders

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblySingleWhineAnalysisResultsPropertyAccessor._Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor":
        return self._Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor(self)
