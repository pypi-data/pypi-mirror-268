"""ConicalGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4102
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConicalGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4045,
        _4052,
        _4054,
        _4055,
        _4057,
        _4106,
        _4110,
        _4113,
        _4116,
        _4145,
        _4151,
        _4154,
        _4156,
        _4157,
        _4173,
        _4120,
        _4065,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearPowerFlow")


class ConicalGearPowerFlow(_4102.GearPowerFlow):
    """ConicalGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearPowerFlow")

    class _Cast_ConicalGearPowerFlow:
        """Special nested class for casting ConicalGearPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
            parent: "ConicalGearPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4102.GearPowerFlow":
            return self._parent._cast(_4102.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4120.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4065.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4045.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.AGMAGleasonConicalGearPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4052.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4054.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4055.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4057.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.BevelGearPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4106.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(_4106.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4110.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(
                _4110.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4113.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4116.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(
                _4116.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def spiral_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4145.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.SpiralBevelGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4151.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4154.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4156.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4157.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.StraightBevelSunGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4173.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4173

            return self._parent._cast(_4173.ZerolBevelGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "ConicalGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2530.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow":
        return self._Cast_ConicalGearPowerFlow(self)
