"""GearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "GearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.gears.rating import _366
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4102,
        _4101,
        _4046,
        _4053,
        _4058,
        _4071,
        _4074,
        _4090,
        _4096,
        _4107,
        _4111,
        _4114,
        _4117,
        _4127,
        _4146,
        _4152,
        _4155,
        _4171,
        _4174,
        _4040,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSetPowerFlow",)


Self = TypeVar("Self", bound="GearSetPowerFlow")


class GearSetPowerFlow(_4143.SpecialisedAssemblyPowerFlow):
    """GearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetPowerFlow")

    class _Cast_GearSetPowerFlow:
        """Special nested class for casting GearSetPowerFlow to subclasses."""

        def __init__(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow", parent: "GearSetPowerFlow"
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4143.SpecialisedAssemblyPowerFlow":
            return self._parent._cast(_4143.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4040.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4046.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4053.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4058.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.BevelGearSetPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4071.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.ConceptGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4074.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.ConicalGearSetPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4090.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.CylindricalGearSetPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4096.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.FaceGearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4107.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(_4107.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4111.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(
                _4111.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4114.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(
                _4114.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4117.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(
                _4117.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def planetary_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4127.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.PlanetaryGearSetPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4146.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4152.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4155.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.StraightBevelGearSetPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4171.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4174.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4174

            return self._parent._cast(_4174.ZerolBevelGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "GearSetPowerFlow":
            return self._parent

        def __getattr__(self: "GearSetPowerFlow._Cast_GearSetPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_366.GearSetRating":
        """mastapy.gears.rating.GearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4102.GearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow]

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
    def meshes_power_flow(self: Self) -> "List[_4101.GearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow]

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

    def set_face_widths_for_specified_safety_factors(self: Self):
        """Method does not return."""
        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()

    @property
    def cast_to(self: Self) -> "GearSetPowerFlow._Cast_GearSetPowerFlow":
        return self._Cast_GearSetPowerFlow(self)
