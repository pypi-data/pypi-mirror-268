"""HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5870,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_COMPONENT_WITHIN_A_HARMONIC = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults",
    "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5881,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",)


Self = TypeVar(
    "Self", bound="HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic"
)


class HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic(
    _5870.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
):
    """HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_COMPONENT_WITHIN_A_HARMONIC
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
    )

    class _Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic:
        """Special nested class for casting HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic to subclasses."""

        def __init__(
            self: "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
            parent: "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
        ):
            self._parent = parent

        @property
        def harmonic_analysis_results_broken_down_by_location_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
        ) -> "_5870.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic":
            return self._parent._cast(
                _5870.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
            )

        @property
        def harmonic_analysis_results_broken_down_by_component_within_a_harmonic(
            self: "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
        ) -> "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
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
        instance_to_wrap: "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentName

        if temp is None:
            return ""

        return temp

    @property
    def dynamic_mesh_force(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicMeshForce

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def dynamic_mesh_moment(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicMeshMoment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def dynamic_misalignment(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicMisalignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def dynamic_te(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicTE

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def kinetic_energy(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KineticEnergy

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def strain_energy(
        self: Self,
    ) -> "_5881.ResultsForResponseOfAComponentOrSurfaceInAHarmonic":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.ResultsForResponseOfAComponentOrSurfaceInAHarmonic

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrainEnergy

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic":
        return self._Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic(
            self
        )
