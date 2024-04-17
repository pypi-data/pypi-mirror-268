"""FEPartSingleWhineAnalysisResultsPropertyAccessor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5886,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "FEPartSingleWhineAnalysisResultsPropertyAccessor",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5880,
        _5862,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FEPartSingleWhineAnalysisResultsPropertyAccessor",)


Self = TypeVar("Self", bound="FEPartSingleWhineAnalysisResultsPropertyAccessor")


class FEPartSingleWhineAnalysisResultsPropertyAccessor(
    _5886.SingleWhineAnalysisResultsPropertyAccessor
):
    """FEPartSingleWhineAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _FE_PART_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor"
    )

    class _Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor:
        """Special nested class for casting FEPartSingleWhineAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(
            self: "FEPartSingleWhineAnalysisResultsPropertyAccessor._Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor",
            parent: "FEPartSingleWhineAnalysisResultsPropertyAccessor",
        ):
            self._parent = parent

        @property
        def single_whine_analysis_results_property_accessor(
            self: "FEPartSingleWhineAnalysisResultsPropertyAccessor._Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor",
        ) -> "_5886.SingleWhineAnalysisResultsPropertyAccessor":
            return self._parent._cast(_5886.SingleWhineAnalysisResultsPropertyAccessor)

        @property
        def abstract_single_whine_analysis_results_property_accessor(
            self: "FEPartSingleWhineAnalysisResultsPropertyAccessor._Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor",
        ) -> "_5862.AbstractSingleWhineAnalysisResultsPropertyAccessor":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5862,
            )

            return self._parent._cast(
                _5862.AbstractSingleWhineAnalysisResultsPropertyAccessor
            )

        @property
        def fe_part_single_whine_analysis_results_property_accessor(
            self: "FEPartSingleWhineAnalysisResultsPropertyAccessor._Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor",
        ) -> "FEPartSingleWhineAnalysisResultsPropertyAccessor":
            return self._parent

        def __getattr__(
            self: "FEPartSingleWhineAnalysisResultsPropertyAccessor._Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor",
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
        instance_to_wrap: "FEPartSingleWhineAnalysisResultsPropertyAccessor.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orders(self: Self) -> "List[_5880.ResultsForOrderIncludingSurfaces]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForOrderIncludingSurfaces]

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
    ) -> "FEPartSingleWhineAnalysisResultsPropertyAccessor._Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor":
        return self._Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor(self)
