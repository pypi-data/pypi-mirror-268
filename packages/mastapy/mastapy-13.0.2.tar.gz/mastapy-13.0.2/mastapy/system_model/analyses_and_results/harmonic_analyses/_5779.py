"""HypoidGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5691
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HypoidGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6914
    from mastapy.system_model.analyses_and_results.system_deflections import _2773
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5720,
        _5761,
        _5794,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="HypoidGearHarmonicAnalysis")


class HypoidGearHarmonicAnalysis(_5691.AGMAGleasonConicalGearHarmonicAnalysis):
    """HypoidGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearHarmonicAnalysis")

    class _Cast_HypoidGearHarmonicAnalysis:
        """Special nested class for casting HypoidGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
            parent: "HypoidGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5691.AGMAGleasonConicalGearHarmonicAnalysis":
            return self._parent._cast(_5691.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5720.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5761.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(_5761.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "HypoidGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6914.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2773.HypoidGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis":
        return self._Cast_HypoidGearHarmonicAnalysis(self)
