"""ConicalGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConicalGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5720
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5891,
        _5898,
        _5901,
        _5902,
        _5903,
        _5949,
        _5953,
        _5956,
        _5959,
        _5986,
        _5992,
        _5995,
        _5998,
        _5999,
        _6013,
        _5964,
        _5912,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearCompoundHarmonicAnalysis")


class ConicalGearCompoundHarmonicAnalysis(_5945.GearCompoundHarmonicAnalysis):
    """ConicalGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearCompoundHarmonicAnalysis")

    class _Cast_ConicalGearCompoundHarmonicAnalysis:
        """Special nested class for casting ConicalGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
            parent: "ConicalGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5945.GearCompoundHarmonicAnalysis":
            return self._parent._cast(_5945.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5964.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5891.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(
                _5891.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5898.BevelDifferentialGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5898,
            )

            return self._parent._cast(
                _5898.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5901.BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(
                _5901.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5902.BevelDifferentialSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5902,
            )

            return self._parent._cast(
                _5902.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5903.BevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(_5903.BevelGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5949.HypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(_5949.HypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5953.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(
                _5953.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5956.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(
                _5956.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5959.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5959,
            )

            return self._parent._cast(
                _5959.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5986.SpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5986,
            )

            return self._parent._cast(_5986.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5992.StraightBevelDiffGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(
                _5992.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5995.StraightBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5995,
            )

            return self._parent._cast(_5995.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5998.StraightBevelPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5998,
            )

            return self._parent._cast(
                _5998.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5999.StraightBevelSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5999,
            )

            return self._parent._cast(
                _5999.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_6013.ZerolBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6013,
            )

            return self._parent._cast(_6013.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "ConicalGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.ConicalGearCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5720.ConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5720.ConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> (
        "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis"
    ):
        return self._Cast_ConicalGearCompoundHarmonicAnalysis(self)
