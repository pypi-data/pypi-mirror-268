"""PowerLoadCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4297
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PowerLoadCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.power_flows import _4132
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4252,
        _4200,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundPowerFlow",)


Self = TypeVar("Self", bound="PowerLoadCompoundPowerFlow")


class PowerLoadCompoundPowerFlow(_4297.VirtualComponentCompoundPowerFlow):
    """PowerLoadCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadCompoundPowerFlow")

    class _Cast_PowerLoadCompoundPowerFlow:
        """Special nested class for casting PowerLoadCompoundPowerFlow to subclasses."""

        def __init__(
            self: "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow",
            parent: "PowerLoadCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_power_flow(
            self: "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow",
        ) -> "_4297.VirtualComponentCompoundPowerFlow":
            return self._parent._cast(_4297.VirtualComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow",
        ) -> "_4252.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow",
        ) -> "_4200.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def power_load_compound_power_flow(
            self: "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow",
        ) -> "PowerLoadCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4132.PowerLoadPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PowerLoadPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4132.PowerLoadPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PowerLoadPowerFlow]

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
    ) -> "PowerLoadCompoundPowerFlow._Cast_PowerLoadCompoundPowerFlow":
        return self._Cast_PowerLoadCompoundPowerFlow(self)
