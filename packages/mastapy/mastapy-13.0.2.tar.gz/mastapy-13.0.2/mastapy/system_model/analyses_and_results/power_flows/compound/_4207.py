"""ConicalGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4233
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConicalGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _541
    from mastapy.system_model.analyses_and_results.power_flows import _4073
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4179,
        _4186,
        _4189,
        _4190,
        _4191,
        _4237,
        _4241,
        _4244,
        _4247,
        _4274,
        _4280,
        _4283,
        _4286,
        _4287,
        _4301,
        _4252,
        _4200,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearCompoundPowerFlow")


class ConicalGearCompoundPowerFlow(_4233.GearCompoundPowerFlow):
    """ConicalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearCompoundPowerFlow")

    class _Cast_ConicalGearCompoundPowerFlow:
        """Special nested class for casting ConicalGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
            parent: "ConicalGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4233.GearCompoundPowerFlow":
            return self._parent._cast(_4233.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4252.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4200.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4179.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4186.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4186,
            )

            return self._parent._cast(_4186.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4189.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(
                _4189.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4190.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4191.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.BevelGearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4237.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(_4237.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4241.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(
                _4241.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4244.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(
                _4244.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4247.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(
                _4247.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4274.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.SpiralBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4280.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4283.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4286.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4287.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.StraightBevelSunGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "_4301.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4301,
            )

            return self._parent._cast(_4301.ZerolBevelGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "ConicalGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self: Self) -> "_541.ConicalGearDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_duty_cycle_rating(self: Self) -> "_541.ConicalGearDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_4073.ConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearPowerFlow]

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
    ) -> "List[_4073.ConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearPowerFlow]

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
    ) -> "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow":
        return self._Cast_ConicalGearCompoundPowerFlow(self)
