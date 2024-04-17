"""GearCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7226,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "GearCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7077,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7153,
        _7160,
        _7163,
        _7164,
        _7165,
        _7178,
        _7181,
        _7196,
        _7199,
        _7202,
        _7211,
        _7215,
        _7218,
        _7221,
        _7248,
        _7254,
        _7257,
        _7260,
        _7261,
        _7272,
        _7275,
        _7174,
        _7228,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="GearCompoundAdvancedTimeSteppingAnalysisForModulation")


class GearCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7226.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """GearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GearCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7226.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent._cast(
                _7226.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7153.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7153,
            )

            return self._parent._cast(
                _7153.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7160.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7160,
            )

            return self._parent._cast(
                _7160.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7163.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7163,
            )

            return self._parent._cast(
                _7163.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7164.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7164,
            )

            return self._parent._cast(
                _7164.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7165.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7178.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7178,
            )

            return self._parent._cast(
                _7178.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7181.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7181,
            )

            return self._parent._cast(
                _7181.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7196.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7196,
            )

            return self._parent._cast(
                _7196.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7199.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7199,
            )

            return self._parent._cast(
                _7199.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7202.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7202,
            )

            return self._parent._cast(
                _7202.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7211.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7211,
            )

            return self._parent._cast(
                _7211.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7215.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7215,
            )

            return self._parent._cast(
                _7215.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7218.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7218,
            )

            return self._parent._cast(
                _7218.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7221.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7221,
            )

            return self._parent._cast(
                _7221.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7248.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7248,
            )

            return self._parent._cast(
                _7248.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7254.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7254,
            )

            return self._parent._cast(
                _7254.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7257.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7257,
            )

            return self._parent._cast(
                _7257.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7260.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7260,
            )

            return self._parent._cast(
                _7260.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7261.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7261,
            )

            return self._parent._cast(
                _7261.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7272.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7272,
            )

            return self._parent._cast(
                _7272.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7275.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7275,
            )

            return self._parent._cast(
                _7275.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "GearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7077.GearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.GearAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7077.GearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.GearAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "GearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_GearCompoundAdvancedTimeSteppingAnalysisForModulation(self)
