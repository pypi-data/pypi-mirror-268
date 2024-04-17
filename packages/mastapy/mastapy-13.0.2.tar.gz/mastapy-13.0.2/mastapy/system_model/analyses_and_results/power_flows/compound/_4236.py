"""GuideDxfModelCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4200
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "GuideDxfModelCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.power_flows import _4104
    from mastapy.system_model.analyses_and_results.power_flows.compound import _4254
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCompoundPowerFlow",)


Self = TypeVar("Self", bound="GuideDxfModelCompoundPowerFlow")


class GuideDxfModelCompoundPowerFlow(_4200.ComponentCompoundPowerFlow):
    """GuideDxfModelCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelCompoundPowerFlow")

    class _Cast_GuideDxfModelCompoundPowerFlow:
        """Special nested class for casting GuideDxfModelCompoundPowerFlow to subclasses."""

        def __init__(
            self: "GuideDxfModelCompoundPowerFlow._Cast_GuideDxfModelCompoundPowerFlow",
            parent: "GuideDxfModelCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def component_compound_power_flow(
            self: "GuideDxfModelCompoundPowerFlow._Cast_GuideDxfModelCompoundPowerFlow",
        ) -> "_4200.ComponentCompoundPowerFlow":
            return self._parent._cast(_4200.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "GuideDxfModelCompoundPowerFlow._Cast_GuideDxfModelCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "GuideDxfModelCompoundPowerFlow._Cast_GuideDxfModelCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GuideDxfModelCompoundPowerFlow._Cast_GuideDxfModelCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCompoundPowerFlow._Cast_GuideDxfModelCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def guide_dxf_model_compound_power_flow(
            self: "GuideDxfModelCompoundPowerFlow._Cast_GuideDxfModelCompoundPowerFlow",
        ) -> "GuideDxfModelCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCompoundPowerFlow._Cast_GuideDxfModelCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideDxfModelCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

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
    ) -> "List[_4104.GuideDxfModelPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GuideDxfModelPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4104.GuideDxfModelPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GuideDxfModelPowerFlow]

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
    ) -> "GuideDxfModelCompoundPowerFlow._Cast_GuideDxfModelCompoundPowerFlow":
        return self._Cast_GuideDxfModelCompoundPowerFlow(self)
