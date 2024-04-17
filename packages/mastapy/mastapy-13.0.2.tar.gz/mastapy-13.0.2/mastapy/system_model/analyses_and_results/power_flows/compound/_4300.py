"""WormGearSetCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "WormGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2559
    from mastapy.gears.rating.worm import _378
    from mastapy.system_model.analyses_and_results.power_flows import _4171
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4298,
        _4299,
        _4273,
        _4175,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="WormGearSetCompoundPowerFlow")


class WormGearSetCompoundPowerFlow(_4235.GearSetCompoundPowerFlow):
    """WormGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetCompoundPowerFlow")

    class _Cast_WormGearSetCompoundPowerFlow:
        """Special nested class for casting WormGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow",
            parent: "WormGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_set_compound_power_flow(
            self: "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow",
        ) -> "_4235.GearSetCompoundPowerFlow":
            return self._parent._cast(_4235.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow",
        ) -> "_4273.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow",
        ) -> "_4175.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def worm_gear_set_compound_power_flow(
            self: "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow",
        ) -> "WormGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2559.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2559.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_duty_cycle_rating(self: Self) -> "_378.WormGearSetDutyCycleRating":
        """mastapy.gears.rating.worm.WormGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gear_set_duty_cycle_rating(
        self: Self,
    ) -> "_378.WormGearSetDutyCycleRating":
        """mastapy.gears.rating.worm.WormGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(self: Self) -> "List[_4171.WormGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.WormGearSetPowerFlow]

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
    def worm_gears_compound_power_flow(
        self: Self,
    ) -> "List[_4298.WormGearCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.WormGearCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_compound_power_flow(
        self: Self,
    ) -> "List[_4299.WormGearMeshCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.WormGearMeshCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4171.WormGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.WormGearSetPowerFlow]

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
    ) -> "WormGearSetCompoundPowerFlow._Cast_WormGearSetCompoundPowerFlow":
        return self._Cast_WormGearSetCompoundPowerFlow(self)
