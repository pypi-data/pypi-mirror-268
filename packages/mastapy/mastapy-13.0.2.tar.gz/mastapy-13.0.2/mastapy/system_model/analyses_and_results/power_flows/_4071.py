"""ConceptGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConceptGearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.system_model.analyses_and_results.static_loads import _6852
    from mastapy.gears.rating.concept import _556
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4070,
        _4069,
        _4143,
        _4040,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetPowerFlow",)


Self = TypeVar("Self", bound="ConceptGearSetPowerFlow")


class ConceptGearSetPowerFlow(_4103.GearSetPowerFlow):
    """ConceptGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetPowerFlow")

    class _Cast_ConceptGearSetPowerFlow:
        """Special nested class for casting ConceptGearSetPowerFlow to subclasses."""

        def __init__(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
            parent: "ConceptGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_set_power_flow(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
        ) -> "_4103.GearSetPowerFlow":
            return self._parent._cast(_4103.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
        ) -> "_4143.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
        ) -> "_4040.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_set_power_flow(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow",
        ) -> "ConceptGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2529.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6852.ConceptGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_556.ConceptGearSetRating":
        """mastapy.gears.rating.concept.ConceptGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_556.ConceptGearSetRating":
        """mastapy.gears.rating.concept.ConceptGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4070.ConceptGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_gears_power_flow(self: Self) -> "List[_4070.ConceptGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(self: Self) -> "List[_4069.ConceptGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_power_flow(self: Self) -> "List[_4069.ConceptGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConceptGearSetPowerFlow._Cast_ConceptGearSetPowerFlow":
        return self._Cast_ConceptGearSetPowerFlow(self)
