"""SynchroniserSleeveCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4290
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SynchroniserSleeveCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2614
    from mastapy.system_model.analyses_and_results.power_flows import _4161
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4214,
        _4252,
        _4200,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundPowerFlow",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundPowerFlow")


class SynchroniserSleeveCompoundPowerFlow(_4290.SynchroniserPartCompoundPowerFlow):
    """SynchroniserSleeveCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeveCompoundPowerFlow")

    class _Cast_SynchroniserSleeveCompoundPowerFlow:
        """Special nested class for casting SynchroniserSleeveCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
            parent: "SynchroniserSleeveCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_power_flow(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
        ) -> "_4290.SynchroniserPartCompoundPowerFlow":
            return self._parent._cast(_4290.SynchroniserPartCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
        ) -> "_4214.CouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
        ) -> "_4252.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
        ) -> "_4200.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
        ) -> "SynchroniserSleeveCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2614.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "List[_4161.SynchroniserSleevePowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SynchroniserSleevePowerFlow]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4161.SynchroniserSleevePowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SynchroniserSleevePowerFlow]

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
    ) -> (
        "SynchroniserSleeveCompoundPowerFlow._Cast_SynchroniserSleeveCompoundPowerFlow"
    ):
        return self._Cast_SynchroniserSleeveCompoundPowerFlow(self)
