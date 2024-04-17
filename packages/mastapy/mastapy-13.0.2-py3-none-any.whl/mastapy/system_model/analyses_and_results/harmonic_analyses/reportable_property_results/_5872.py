"""HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5870,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_SURFACE_WITHIN_A_HARMONIC = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5881,
        _5867,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",)


Self = TypeVar(
    "Self", bound="HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic"
)


class HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic(
    _5870.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
):
    """HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_SURFACE_WITHIN_A_HARMONIC
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
    )

    class _Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic:
        """Special nested class for casting HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic to subclasses."""

        def __init__(
            self: "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
            parent: "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
        ):
            self._parent = parent

        @property
        def harmonic_analysis_results_broken_down_by_location_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
        ) -> "_5870.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic":
            return self._parent._cast(
                _5870.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
            )

        @property
        def harmonic_analysis_combined_for_multiple_surfaces_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
        ) -> "_5867.HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
                _5867,
            )

            return self._parent._cast(
                _5867.HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
            )

        @property
        def harmonic_analysis_results_broken_down_by_surface_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
        ) -> "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
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
        instance_to_wrap: "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def surface_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceName

        if temp is None:
            return ""

        return temp

    @property
    def airborne_sound_power(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AirborneSoundPower

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_normal_velocity(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalVelocity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def root_mean_squared_normal_acceleration(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootMeanSquaredNormalAcceleration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def root_mean_squared_normal_displacement(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootMeanSquaredNormalDisplacement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def root_mean_squared_normal_velocity(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootMeanSquaredNormalVelocity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sound_intensity(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SoundIntensity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sound_pressure(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SoundPressure

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic":
        return self._Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic(
            self
        )
