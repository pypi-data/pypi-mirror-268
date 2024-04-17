"""HarmonicAnalysisResultsPropertyAccessor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "HarmonicAnalysisResultsPropertyAccessor",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5886,
        _5879,
        _5865,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisResultsPropertyAccessor",)


Self = TypeVar("Self", bound="HarmonicAnalysisResultsPropertyAccessor")


class HarmonicAnalysisResultsPropertyAccessor(_0.APIBase):
    """HarmonicAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HarmonicAnalysisResultsPropertyAccessor"
    )

    class _Cast_HarmonicAnalysisResultsPropertyAccessor:
        """Special nested class for casting HarmonicAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(
            self: "HarmonicAnalysisResultsPropertyAccessor._Cast_HarmonicAnalysisResultsPropertyAccessor",
            parent: "HarmonicAnalysisResultsPropertyAccessor",
        ):
            self._parent = parent

        @property
        def fe_part_harmonic_analysis_results_property_accessor(
            self: "HarmonicAnalysisResultsPropertyAccessor._Cast_HarmonicAnalysisResultsPropertyAccessor",
        ) -> "_5865.FEPartHarmonicAnalysisResultsPropertyAccessor":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5865,
            )

            return self._parent._cast(
                _5865.FEPartHarmonicAnalysisResultsPropertyAccessor
            )

        @property
        def harmonic_analysis_results_property_accessor(
            self: "HarmonicAnalysisResultsPropertyAccessor._Cast_HarmonicAnalysisResultsPropertyAccessor",
        ) -> "HarmonicAnalysisResultsPropertyAccessor":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisResultsPropertyAccessor._Cast_HarmonicAnalysisResultsPropertyAccessor",
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
        self: Self, instance_to_wrap: "HarmonicAnalysisResultsPropertyAccessor.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitations(
        self: Self,
    ) -> "List[_5886.SingleWhineAnalysisResultsPropertyAccessor]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.SingleWhineAnalysisResultsPropertyAccessor]

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
    ) -> "List[_5879.ResultsForOrderIncludingNodes]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForOrderIncludingNodes]

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
    ) -> "List[_5879.ResultsForOrderIncludingNodes]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForOrderIncludingNodes]

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
    ) -> "HarmonicAnalysisResultsPropertyAccessor._Cast_HarmonicAnalysisResultsPropertyAccessor":
        return self._Cast_HarmonicAnalysisResultsPropertyAccessor(self)
