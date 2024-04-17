"""GearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2937
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "GearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _361
    from mastapy.system_model.analyses_and_results.system_deflections import _2769
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2863,
        _2870,
        _2873,
        _2874,
        _2875,
        _2888,
        _2891,
        _2906,
        _2909,
        _2913,
        _2922,
        _2926,
        _2929,
        _2932,
        _2960,
        _2966,
        _2969,
        _2972,
        _2973,
        _2984,
        _2987,
        _2884,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="GearCompoundSystemDeflection")


class GearCompoundSystemDeflection(_2937.MountableComponentCompoundSystemDeflection):
    """GearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundSystemDeflection")

    class _Cast_GearCompoundSystemDeflection:
        """Special nested class for casting GearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
            parent: "GearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2863.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2870.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2870,
            )

            return self._parent._cast(
                _2870.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2873.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(
                _2873.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2874.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(
                _2874.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2875.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(_2875.BevelGearCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2888.ConceptGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.ConceptGearCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2891.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.ConicalGearCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2906.CylindricalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2909.CylindricalPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(
                _2909.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def face_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2913.FaceGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.FaceGearCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2922.HypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2922,
            )

            return self._parent._cast(_2922.HypoidGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(
                _2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2929.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(
                _2929.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2932.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(
                _2932.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2960.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(_2960.SpiralBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2966.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(
                _2966.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2969.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2972.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(
                _2972.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2973.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(
                _2973.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def worm_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2984.WormGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2984,
            )

            return self._parent._cast(_2984.WormGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "_2987.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2987,
            )

            return self._parent._cast(_2987.ZerolBevelGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "GearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_rating(self: Self) -> "_361.GearDutyCycleRating":
        """mastapy.gears.rating.GearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_2769.GearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection]

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
    ) -> "List[_2769.GearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection]

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
    ) -> "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection":
        return self._Cast_GearCompoundSystemDeflection(self)
