"""StraightBevelGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4058
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "StraightBevelGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.gears.rating.straight_bevel import _400
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4154,
        _4153,
        _4046,
        _4074,
        _4103,
        _4143,
        _4040,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelGearSetPowerFlow")


class StraightBevelGearSetPowerFlow(_4058.BevelGearSetPowerFlow):
    """StraightBevelGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearSetPowerFlow")

    class _Cast_StraightBevelGearSetPowerFlow:
        """Special nested class for casting StraightBevelGearSetPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
            parent: "StraightBevelGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4058.BevelGearSetPowerFlow":
            return self._parent._cast(_4058.BevelGearSetPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4046.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4074.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4103.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4143.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4040.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
        ) -> "StraightBevelGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2555.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6973.StraightBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_400.StraightBevelGearSetRating":
        """mastapy.gears.rating.straight_bevel.StraightBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_400.StraightBevelGearSetRating":
        """mastapy.gears.rating.straight_bevel.StraightBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4154.StraightBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearPowerFlow]

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
    def straight_bevel_gears_power_flow(
        self: Self,
    ) -> "List[_4154.StraightBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(self: Self) -> "List[_4153.StraightBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearMeshPowerFlow]

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
    def straight_bevel_meshes_power_flow(
        self: Self,
    ) -> "List[_4153.StraightBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetPowerFlow._Cast_StraightBevelGearSetPowerFlow":
        return self._Cast_StraightBevelGearSetPowerFlow(self)
