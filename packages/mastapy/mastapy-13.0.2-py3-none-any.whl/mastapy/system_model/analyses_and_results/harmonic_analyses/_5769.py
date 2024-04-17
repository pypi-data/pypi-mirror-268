"""HarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses", "HarmonicAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6078,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5773
    from mastapy.system_model.analyses_and_results.analysis_cases import _7558, _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysis",)


Self = TypeVar("Self", bound="HarmonicAnalysis")


class HarmonicAnalysis(_7545.CompoundAnalysisCase):
    """HarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicAnalysis")

    class _Cast_HarmonicAnalysis:
        """Special nested class for casting HarmonicAnalysis to subclasses."""

        def __init__(
            self: "HarmonicAnalysis._Cast_HarmonicAnalysis", parent: "HarmonicAnalysis"
        ):
            self._parent = parent

        @property
        def compound_analysis_case(
            self: "HarmonicAnalysis._Cast_HarmonicAnalysis",
        ) -> "_7545.CompoundAnalysisCase":
            return self._parent._cast(_7545.CompoundAnalysisCase)

        @property
        def static_load_analysis_case(
            self: "HarmonicAnalysis._Cast_HarmonicAnalysis",
        ) -> "_7558.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7558

            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "HarmonicAnalysis._Cast_HarmonicAnalysis",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(self: "HarmonicAnalysis._Cast_HarmonicAnalysis") -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "HarmonicAnalysis._Cast_HarmonicAnalysis",
        ) -> "_5773.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(
                _5773.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis(
            self: "HarmonicAnalysis._Cast_HarmonicAnalysis",
        ) -> "HarmonicAnalysis":
            return self._parent

        def __getattr__(self: "HarmonicAnalysis._Cast_HarmonicAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def time_for_modal_analysis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeForModalAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def time_for_single_excitations_post_analysis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeForSingleExcitationsPostAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_run_single_excitations(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToRunSingleExcitations

        if temp is None:
            return 0.0

        return temp

    @property
    def harmonic_analyses_of_single_excitations(
        self: Self,
    ) -> "List[_6078.HarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysesOfSingleExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "HarmonicAnalysis._Cast_HarmonicAnalysis":
        return self._Cast_HarmonicAnalysis(self)
