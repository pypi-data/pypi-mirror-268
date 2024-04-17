"""AdvancedTimeSteppingAnalysisForModulationStaticLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_STATIC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5774
    from mastapy.system_model.analyses_and_results.static_loads import _6812
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",)


Self = TypeVar("Self", bound="AdvancedTimeSteppingAnalysisForModulationStaticLoadCase")


class AdvancedTimeSteppingAnalysisForModulationStaticLoadCase(_6813.StaticLoadCase):
    """AdvancedTimeSteppingAnalysisForModulationStaticLoadCase

    This is a mastapy class.
    """

    TYPE = _ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_STATIC_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
    )

    class _Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase:
        """Special nested class for casting AdvancedTimeSteppingAnalysisForModulationStaticLoadCase to subclasses."""

        def __init__(
            self: "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase._Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
            parent: "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
        ):
            self._parent = parent

        @property
        def static_load_case(
            self: "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase._Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
        ) -> "_6813.StaticLoadCase":
            return self._parent._cast(_6813.StaticLoadCase)

        @property
        def load_case(
            self: "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase._Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
        ) -> "_6812.LoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6812

            return self._parent._cast(_6812.LoadCase)

        @property
        def context(
            self: "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase._Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def advanced_time_stepping_analysis_for_modulation_static_load_case(
            self: "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase._Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
        ) -> "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase":
            return self._parent

        def __getattr__(
            self: "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase._Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
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
        instance_to_wrap: "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_analysis_options(self: Self) -> "_5774.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase._Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase":
        return self._Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase(self)
