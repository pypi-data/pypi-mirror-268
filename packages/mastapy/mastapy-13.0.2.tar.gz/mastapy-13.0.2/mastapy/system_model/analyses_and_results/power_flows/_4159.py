"""SynchroniserPartPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4078
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "SynchroniserPartPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2613
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4158,
        _4161,
        _4120,
        _4065,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartPowerFlow",)


Self = TypeVar("Self", bound="SynchroniserPartPowerFlow")


class SynchroniserPartPowerFlow(_4078.CouplingHalfPowerFlow):
    """SynchroniserPartPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartPowerFlow")

    class _Cast_SynchroniserPartPowerFlow:
        """Special nested class for casting SynchroniserPartPowerFlow to subclasses."""

        def __init__(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
            parent: "SynchroniserPartPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4078.CouplingHalfPowerFlow":
            return self._parent._cast(_4078.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4120.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4065.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4158.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "_4161.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.SynchroniserSleevePowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "SynchroniserPartPowerFlow":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2613.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow":
        return self._Cast_SynchroniserPartPowerFlow(self)
