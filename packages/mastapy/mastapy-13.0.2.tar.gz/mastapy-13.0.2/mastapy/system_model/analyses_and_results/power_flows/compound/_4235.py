"""GearSetCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4273
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "GearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _365
    from mastapy.system_model.analyses_and_results.power_flows import _4103
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4181,
        _4188,
        _4193,
        _4206,
        _4209,
        _4224,
        _4230,
        _4239,
        _4243,
        _4246,
        _4249,
        _4259,
        _4276,
        _4282,
        _4285,
        _4300,
        _4303,
        _4175,
        _4254,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="GearSetCompoundPowerFlow")


class GearSetCompoundPowerFlow(_4273.SpecialisedAssemblyCompoundPowerFlow):
    """GearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCompoundPowerFlow")

    class _Cast_GearSetCompoundPowerFlow:
        """Special nested class for casting GearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
            parent: "GearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4273.SpecialisedAssemblyCompoundPowerFlow":
            return self._parent._cast(_4273.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4175.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4181.AGMAGleasonConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4188.BevelDifferentialGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4193.BevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.BevelGearSetCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4206.ConceptGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4209.ConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4209,
            )

            return self._parent._cast(_4209.ConicalGearSetCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4224.CylindricalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.CylindricalGearSetCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4230.FaceGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(_4230.FaceGearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4239.HypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(_4239.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4243.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(
                _4243.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4246.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(
                _4246.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4249.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(
                _4249.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def planetary_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4259.PlanetaryGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(_4259.PlanetaryGearSetCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4276.SpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4282.StraightBevelDiffGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4285.StraightBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.StraightBevelGearSetCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4300.WormGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4300,
            )

            return self._parent._cast(_4300.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "_4303.ZerolBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4303,
            )

            return self._parent._cast(_4303.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "GearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_rating(self: Self) -> "_365.GearSetDutyCycleRating":
        """mastapy.gears.rating.GearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4103.GearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearSetPowerFlow]

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
    def assembly_analysis_cases_ready(self: Self) -> "List[_4103.GearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearSetPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow":
        return self._Cast_GearSetCompoundPowerFlow(self)
