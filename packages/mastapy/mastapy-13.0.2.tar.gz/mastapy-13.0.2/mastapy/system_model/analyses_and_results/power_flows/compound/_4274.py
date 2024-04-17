"""SpiralBevelGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4191
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpiralBevelGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.power_flows import _4145
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4179,
        _4207,
        _4233,
        _4252,
        _4200,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpiralBevelGearCompoundPowerFlow")


class SpiralBevelGearCompoundPowerFlow(_4191.BevelGearCompoundPowerFlow):
    """SpiralBevelGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearCompoundPowerFlow")

    class _Cast_SpiralBevelGearCompoundPowerFlow:
        """Special nested class for casting SpiralBevelGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
            parent: "SpiralBevelGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4191.BevelGearCompoundPowerFlow":
            return self._parent._cast(_4191.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4179.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4207.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4207,
            )

            return self._parent._cast(_4207.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4233.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(_4233.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4252.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4200.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "SpiralBevelGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

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
    ) -> "List[_4145.SpiralBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4145.SpiralBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearPowerFlow]

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
    ) -> "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow":
        return self._Cast_SpiralBevelGearCompoundPowerFlow(self)
