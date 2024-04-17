"""HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5870,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_NODE_WITHIN_A_HARMONIC = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5882,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",)


Self = TypeVar("Self", bound="HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic")


class HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic(
    _5870.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
):
    """HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_NODE_WITHIN_A_HARMONIC
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
    )

    class _Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic:
        """Special nested class for casting HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic to subclasses."""

        def __init__(
            self: "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
            parent: "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
        ):
            self._parent = parent

        @property
        def harmonic_analysis_results_broken_down_by_location_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
        ) -> "_5870.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic":
            return self._parent._cast(
                _5870.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
            )

        @property
        def harmonic_analysis_results_broken_down_by_node_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
        ) -> "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
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
        instance_to_wrap: "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeName

        if temp is None:
            return ""

        return temp

    @property
    def acceleration(self: Self) -> "_5882.ResultsForResponseOfANodeOnAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfANodeOnAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Acceleration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def displacement(self: Self) -> "_5882.ResultsForResponseOfANodeOnAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfANodeOnAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Displacement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force(self: Self) -> "_5882.ResultsForResponseOfANodeOnAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfANodeOnAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Force

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def velocity(self: Self) -> "_5882.ResultsForResponseOfANodeOnAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfANodeOnAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Velocity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic":
        return self._Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic(self)
