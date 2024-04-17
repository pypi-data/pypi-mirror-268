"""RingPinsPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4120
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "RingPinsPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2577
    from mastapy.system_model.analyses_and_results.static_loads import _6952
    from mastapy.system_model.analyses_and_results.power_flows import _4065, _4122
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsPowerFlow",)


Self = TypeVar("Self", bound="RingPinsPowerFlow")


class RingPinsPowerFlow(_4120.MountableComponentPowerFlow):
    """RingPinsPowerFlow

    This is a mastapy class.
    """

    TYPE = _RING_PINS_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsPowerFlow")

    class _Cast_RingPinsPowerFlow:
        """Special nested class for casting RingPinsPowerFlow to subclasses."""

        def __init__(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
            parent: "RingPinsPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ) -> "_4120.MountableComponentPowerFlow":
            return self._parent._cast(_4120.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ) -> "_4065.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def ring_pins_power_flow(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ) -> "RingPinsPowerFlow":
            return self._parent

        def __getattr__(self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2577.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6952.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RingPinsPowerFlow._Cast_RingPinsPowerFlow":
        return self._Cast_RingPinsPowerFlow(self)
