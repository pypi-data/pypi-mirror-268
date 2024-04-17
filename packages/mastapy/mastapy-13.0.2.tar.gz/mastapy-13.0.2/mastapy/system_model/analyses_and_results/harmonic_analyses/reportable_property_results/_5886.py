"""SingleWhineAnalysisResultsPropertyAccessor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5862,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "SingleWhineAnalysisResultsPropertyAccessor",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5879,
        _5866,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SingleWhineAnalysisResultsPropertyAccessor",)


Self = TypeVar("Self", bound="SingleWhineAnalysisResultsPropertyAccessor")


class SingleWhineAnalysisResultsPropertyAccessor(
    _5862.AbstractSingleWhineAnalysisResultsPropertyAccessor
):
    """SingleWhineAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SingleWhineAnalysisResultsPropertyAccessor"
    )

    class _Cast_SingleWhineAnalysisResultsPropertyAccessor:
        """Special nested class for casting SingleWhineAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(
            self: "SingleWhineAnalysisResultsPropertyAccessor._Cast_SingleWhineAnalysisResultsPropertyAccessor",
            parent: "SingleWhineAnalysisResultsPropertyAccessor",
        ):
            self._parent = parent

        @property
        def abstract_single_whine_analysis_results_property_accessor(
            self: "SingleWhineAnalysisResultsPropertyAccessor._Cast_SingleWhineAnalysisResultsPropertyAccessor",
        ) -> "_5862.AbstractSingleWhineAnalysisResultsPropertyAccessor":
            return self._parent._cast(
                _5862.AbstractSingleWhineAnalysisResultsPropertyAccessor
            )

        @property
        def fe_part_single_whine_analysis_results_property_accessor(
            self: "SingleWhineAnalysisResultsPropertyAccessor._Cast_SingleWhineAnalysisResultsPropertyAccessor",
        ) -> "_5866.FEPartSingleWhineAnalysisResultsPropertyAccessor":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5866,
            )

            return self._parent._cast(
                _5866.FEPartSingleWhineAnalysisResultsPropertyAccessor
            )

        @property
        def single_whine_analysis_results_property_accessor(
            self: "SingleWhineAnalysisResultsPropertyAccessor._Cast_SingleWhineAnalysisResultsPropertyAccessor",
        ) -> "SingleWhineAnalysisResultsPropertyAccessor":
            return self._parent

        def __getattr__(
            self: "SingleWhineAnalysisResultsPropertyAccessor._Cast_SingleWhineAnalysisResultsPropertyAccessor",
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
        self: Self, instance_to_wrap: "SingleWhineAnalysisResultsPropertyAccessor.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orders(self: Self) -> "List[_5879.ResultsForOrderIncludingNodes]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForOrderIncludingNodes]

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
    ) -> "SingleWhineAnalysisResultsPropertyAccessor._Cast_SingleWhineAnalysisResultsPropertyAccessor":
        return self._Cast_SingleWhineAnalysisResultsPropertyAccessor(self)
