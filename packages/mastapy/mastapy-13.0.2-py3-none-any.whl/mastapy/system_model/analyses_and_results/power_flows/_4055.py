"""BevelDifferentialSunGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4052
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "BevelDifferentialSunGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4057,
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
__all__ = ("BevelDifferentialSunGearPowerFlow",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearPowerFlow")


class BevelDifferentialSunGearPowerFlow(_4052.BevelDifferentialGearPowerFlow):
    """BevelDifferentialSunGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialSunGearPowerFlow")

    class _Cast_BevelDifferentialSunGearPowerFlow:
        """Special nested class for casting BevelDifferentialSunGearPowerFlow to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
            parent: "BevelDifferentialSunGearPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_power_flow(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_4052.BevelDifferentialGearPowerFlow":
            return self._parent._cast(_4052.BevelDifferentialGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_4057.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.BevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_4045.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_4073.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_4102.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_4120.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_4065.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
        ) -> "BevelDifferentialSunGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow",
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
        self: Self, instance_to_wrap: "BevelDifferentialSunGearPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialSunGearPowerFlow._Cast_BevelDifferentialSunGearPowerFlow":
        return self._Cast_BevelDifferentialSunGearPowerFlow(self)
