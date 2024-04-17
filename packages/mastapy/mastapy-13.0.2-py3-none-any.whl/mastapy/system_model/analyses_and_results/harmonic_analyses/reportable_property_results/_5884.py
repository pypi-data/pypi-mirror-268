"""RootAssemblyHarmonicAnalysisResultsPropertyAccessor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5876,
        _5885,
        _5878,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyHarmonicAnalysisResultsPropertyAccessor",)


Self = TypeVar("Self", bound="RootAssemblyHarmonicAnalysisResultsPropertyAccessor")


class RootAssemblyHarmonicAnalysisResultsPropertyAccessor(_0.APIBase):
    """RootAssemblyHarmonicAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyHarmonicAnalysisResultsPropertyAccessor"
    )

    class _Cast_RootAssemblyHarmonicAnalysisResultsPropertyAccessor:
        """Special nested class for casting RootAssemblyHarmonicAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(
            self: "RootAssemblyHarmonicAnalysisResultsPropertyAccessor._Cast_RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
            parent: "RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
        ):
            self._parent = parent

        @property
        def root_assembly_harmonic_analysis_results_property_accessor(
            self: "RootAssemblyHarmonicAnalysisResultsPropertyAccessor._Cast_RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
        ) -> "RootAssemblyHarmonicAnalysisResultsPropertyAccessor":
            return self._parent

        def __getattr__(
            self: "RootAssemblyHarmonicAnalysisResultsPropertyAccessor._Cast_RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
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
        instance_to_wrap: "RootAssemblyHarmonicAnalysisResultsPropertyAccessor.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def combined_orders(self: Self) -> "_5876.ResultsForMultipleOrdersForGroups":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForMultipleOrdersForGroups

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CombinedOrders

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def excitations(
        self: Self,
    ) -> "List[_5885.RootAssemblySingleWhineAnalysisResultsPropertyAccessor]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.RootAssemblySingleWhineAnalysisResultsPropertyAccessor]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def orders_for_combined_excitations(
        self: Self,
    ) -> "List[_5878.ResultsForOrderIncludingGroups]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForOrderIncludingGroups]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OrdersForCombinedExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def orders_for_combined_excitations_from_same_parts(
        self: Self,
    ) -> "List[_5878.ResultsForOrderIncludingGroups]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForOrderIncludingGroups]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OrdersForCombinedExcitationsFromSameParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyHarmonicAnalysisResultsPropertyAccessor._Cast_RootAssemblyHarmonicAnalysisResultsPropertyAccessor":
        return self._Cast_RootAssemblyHarmonicAnalysisResultsPropertyAccessor(self)
