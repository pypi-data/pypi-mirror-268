"""CylindricalGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4102
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CylindricalGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.gears.rating.cylindrical import _463
    from mastapy.system_model.analyses_and_results.static_loads import _6870
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4091,
        _4120,
        _4065,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearPowerFlow",)


Self = TypeVar("Self", bound="CylindricalGearPowerFlow")


class CylindricalGearPowerFlow(_4102.GearPowerFlow):
    """CylindricalGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearPowerFlow")

    class _Cast_CylindricalGearPowerFlow:
        """Special nested class for casting CylindricalGearPowerFlow to subclasses."""

        def __init__(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
            parent: "CylindricalGearPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_power_flow(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "_4102.GearPowerFlow":
            return self._parent._cast(_4102.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "_4120.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "_4065.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "_4091.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.CylindricalPlanetGearPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow",
        ) -> "CylindricalGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2532.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_463.CylindricalGearRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6870.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

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
    ) -> "CylindricalGearPowerFlow._Cast_CylindricalGearPowerFlow":
        return self._Cast_CylindricalGearPowerFlow(self)
