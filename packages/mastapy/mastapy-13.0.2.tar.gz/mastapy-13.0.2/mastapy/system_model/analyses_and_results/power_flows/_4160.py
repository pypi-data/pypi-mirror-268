"""SynchroniserPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "SynchroniserPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6977
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4158,
        _4040,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPowerFlow",)


Self = TypeVar("Self", bound="SynchroniserPowerFlow")


class SynchroniserPowerFlow(_4143.SpecialisedAssemblyPowerFlow):
    """SynchroniserPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPowerFlow")

    class _Cast_SynchroniserPowerFlow:
        """Special nested class for casting SynchroniserPowerFlow to subclasses."""

        def __init__(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow",
            parent: "SynchroniserPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow",
        ) -> "_4143.SpecialisedAssemblyPowerFlow":
            return self._parent._cast(_4143.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow",
        ) -> "_4040.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_power_flow(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow",
        ) -> "SynchroniserPowerFlow":
            return self._parent

        def __getattr__(
            self: "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2610.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6977.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cones(self: Self) -> "List[_4158.SynchroniserHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SynchroniserHalfPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Cones

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "SynchroniserPowerFlow._Cast_SynchroniserPowerFlow":
        return self._Cast_SynchroniserPowerFlow(self)
