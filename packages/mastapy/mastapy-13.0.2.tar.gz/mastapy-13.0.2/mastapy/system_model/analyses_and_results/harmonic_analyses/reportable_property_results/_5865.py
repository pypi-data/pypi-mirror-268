"""FEPartHarmonicAnalysisResultsPropertyAccessor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5873,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "FEPartHarmonicAnalysisResultsPropertyAccessor",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5875,
        _5866,
        _5880,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FEPartHarmonicAnalysisResultsPropertyAccessor",)


Self = TypeVar("Self", bound="FEPartHarmonicAnalysisResultsPropertyAccessor")


class FEPartHarmonicAnalysisResultsPropertyAccessor(
    _5873.HarmonicAnalysisResultsPropertyAccessor
):
    """FEPartHarmonicAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _FE_PART_HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FEPartHarmonicAnalysisResultsPropertyAccessor"
    )

    class _Cast_FEPartHarmonicAnalysisResultsPropertyAccessor:
        """Special nested class for casting FEPartHarmonicAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(
            self: "FEPartHarmonicAnalysisResultsPropertyAccessor._Cast_FEPartHarmonicAnalysisResultsPropertyAccessor",
            parent: "FEPartHarmonicAnalysisResultsPropertyAccessor",
        ):
            self._parent = parent

        @property
        def harmonic_analysis_results_property_accessor(
            self: "FEPartHarmonicAnalysisResultsPropertyAccessor._Cast_FEPartHarmonicAnalysisResultsPropertyAccessor",
        ) -> "_5873.HarmonicAnalysisResultsPropertyAccessor":
            return self._parent._cast(_5873.HarmonicAnalysisResultsPropertyAccessor)

        @property
        def fe_part_harmonic_analysis_results_property_accessor(
            self: "FEPartHarmonicAnalysisResultsPropertyAccessor._Cast_FEPartHarmonicAnalysisResultsPropertyAccessor",
        ) -> "FEPartHarmonicAnalysisResultsPropertyAccessor":
            return self._parent

        def __getattr__(
            self: "FEPartHarmonicAnalysisResultsPropertyAccessor._Cast_FEPartHarmonicAnalysisResultsPropertyAccessor",
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
        instance_to_wrap: "FEPartHarmonicAnalysisResultsPropertyAccessor.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def combined_orders(self: Self) -> "_5875.ResultsForMultipleOrdersForFESurface":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForMultipleOrdersForFESurface

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
    ) -> "List[_5866.FEPartSingleWhineAnalysisResultsPropertyAccessor]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.FEPartSingleWhineAnalysisResultsPropertyAccessor]

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
    ) -> "List[_5880.ResultsForOrderIncludingSurfaces]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForOrderIncludingSurfaces]

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
    ) -> "List[_5880.ResultsForOrderIncludingSurfaces]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForOrderIncludingSurfaces]

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
    ) -> "FEPartHarmonicAnalysisResultsPropertyAccessor._Cast_FEPartHarmonicAnalysisResultsPropertyAccessor":
        return self._Cast_FEPartHarmonicAnalysisResultsPropertyAccessor(self)
