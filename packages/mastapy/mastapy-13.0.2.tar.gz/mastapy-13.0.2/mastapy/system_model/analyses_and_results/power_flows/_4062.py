"""ClutchHalfPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4078
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ClutchHalfPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.static_loads import _6842
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4120,
        _4065,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfPowerFlow",)


Self = TypeVar("Self", bound="ClutchHalfPowerFlow")


class ClutchHalfPowerFlow(_4078.CouplingHalfPowerFlow):
    """ClutchHalfPowerFlow

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfPowerFlow")

    class _Cast_ClutchHalfPowerFlow:
        """Special nested class for casting ClutchHalfPowerFlow to subclasses."""

        def __init__(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
            parent: "ClutchHalfPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
        ) -> "_4078.CouplingHalfPowerFlow":
            return self._parent._cast(_4078.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
        ) -> "_4120.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
        ) -> "_4065.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_power_flow(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow",
        ) -> "ClutchHalfPowerFlow":
            return self._parent

        def __getattr__(
            self: "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalfPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2586.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6842.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchHalfPowerFlow._Cast_ClutchHalfPowerFlow":
        return self._Cast_ClutchHalfPowerFlow(self)
