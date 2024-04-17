"""KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5783
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.static_loads import _6924
    from mastapy.system_model.analyses_and_results.system_deflections import _2781
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
__all__ = ("KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis")


class KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis(
    _5783.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_5783.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
            return self._parent._cast(
                _5783.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def conical_gear_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_5720.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_5761.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(_5761.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6924.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection

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
    ) -> "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis(self)
