"""KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5786
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5919,
        _5945,
        _5964,
        _5912,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis(
    _5953.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ) -> "_5953.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5953.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ) -> "_5919.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5919,
            )

            return self._parent._cast(_5919.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ) -> "_5945.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(_5945.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ) -> "_5964.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis.TYPE",
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5786.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5786.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis(
            self
        )
