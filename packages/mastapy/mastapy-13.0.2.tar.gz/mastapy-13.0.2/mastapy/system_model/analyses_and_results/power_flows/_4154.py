"""StraightBevelGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4057
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "StraightBevelGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.gears.rating.straight_bevel import _399
    from mastapy.system_model.analyses_and_results.static_loads import _6971
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4045,
        _4073,
        _4102,
        _4120,
        _4065,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelGearPowerFlow")


class StraightBevelGearPowerFlow(_4057.BevelGearPowerFlow):
    """StraightBevelGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearPowerFlow")

    class _Cast_StraightBevelGearPowerFlow:
        """Special nested class for casting StraightBevelGearPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
            parent: "StraightBevelGearPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_power_flow(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_4057.BevelGearPowerFlow":
            return self._parent._cast(_4057.BevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_4045.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_4073.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_4102.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_4120.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_4065.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_power_flow(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
        ) -> "StraightBevelGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_399.StraightBevelGearRating":
        """mastapy.gears.rating.straight_bevel.StraightBevelGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6971.StraightBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearPowerFlow._Cast_StraightBevelGearPowerFlow":
        return self._Cast_StraightBevelGearPowerFlow(self)
