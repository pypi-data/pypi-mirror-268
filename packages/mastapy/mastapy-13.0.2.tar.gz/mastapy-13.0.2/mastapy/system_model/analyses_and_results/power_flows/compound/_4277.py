"""SpringDamperCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4212
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpringDamperCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.power_flows import _4149
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4273,
        _4175,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpringDamperCompoundPowerFlow")


class SpringDamperCompoundPowerFlow(_4212.CouplingCompoundPowerFlow):
    """SpringDamperCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperCompoundPowerFlow")

    class _Cast_SpringDamperCompoundPowerFlow:
        """Special nested class for casting SpringDamperCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow",
            parent: "SpringDamperCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_compound_power_flow(
            self: "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow",
        ) -> "_4212.CouplingCompoundPowerFlow":
            return self._parent._cast(_4212.CouplingCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow",
        ) -> "_4273.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow",
        ) -> "_4175.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_compound_power_flow(
            self: "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow",
        ) -> "SpringDamperCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2608.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4149.SpringDamperPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpringDamperPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4149.SpringDamperPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpringDamperPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperCompoundPowerFlow._Cast_SpringDamperCompoundPowerFlow":
        return self._Cast_SpringDamperCompoundPowerFlow(self)
