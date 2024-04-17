"""FEPartPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4041
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "FEPartPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6896
    from mastapy.system_model.analyses_and_results.power_flows import _4065, _4122
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FEPartPowerFlow",)


Self = TypeVar("Self", bound="FEPartPowerFlow")


class FEPartPowerFlow(_4041.AbstractShaftOrHousingPowerFlow):
    """FEPartPowerFlow

    This is a mastapy class.
    """

    TYPE = _FE_PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartPowerFlow")

    class _Cast_FEPartPowerFlow:
        """Special nested class for casting FEPartPowerFlow to subclasses."""

        def __init__(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow", parent: "FEPartPowerFlow"
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_4041.AbstractShaftOrHousingPowerFlow":
            return self._parent._cast(_4041.AbstractShaftOrHousingPowerFlow)

        @property
        def component_power_flow(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_4065.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def fe_part_power_flow(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "FEPartPowerFlow":
            return self._parent

        def __getattr__(self: "FEPartPowerFlow._Cast_FEPartPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_parts_are_not_used_in_power_flow(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEPartsAreNotUsedInPowerFlow

        if temp is None:
            return ""

        return temp

    @property
    def fe_parts_are_not_used_in_power_flow_select_component_replaced_by_this_fe(
        self: Self,
    ) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEPartsAreNotUsedInPowerFlowSelectComponentReplacedByThisFE

        if temp is None:
            return ""

        return temp

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2460.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6896.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FEPartPowerFlow._Cast_FEPartPowerFlow":
        return self._Cast_FEPartPowerFlow(self)
