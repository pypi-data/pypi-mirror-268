"""SpecialisedAssemblyPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4040
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "SpecialisedAssemblyPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4046,
        _4050,
        _4053,
        _4058,
        _4059,
        _4063,
        _4068,
        _4071,
        _4074,
        _4079,
        _4081,
        _4083,
        _4090,
        _4096,
        _4100,
        _4103,
        _4107,
        _4111,
        _4114,
        _4117,
        _4125,
        _4127,
        _4136,
        _4146,
        _4149,
        _4152,
        _4155,
        _4160,
        _4164,
        _4171,
        _4174,
        _4122,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyPowerFlow",)


Self = TypeVar("Self", bound="SpecialisedAssemblyPowerFlow")


class SpecialisedAssemblyPowerFlow(_4040.AbstractAssemblyPowerFlow):
    """SpecialisedAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyPowerFlow")

    class _Cast_SpecialisedAssemblyPowerFlow:
        """Special nested class for casting SpecialisedAssemblyPowerFlow to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
            parent: "SpecialisedAssemblyPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_assembly_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4040.AbstractAssemblyPowerFlow":
            return self._parent._cast(_4040.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4122.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4046.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4050.BeltDrivePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4050

            return self._parent._cast(_4050.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4053.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4058.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4059.BoltedJointPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.BoltedJointPowerFlow)

        @property
        def clutch_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4063.ClutchPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ClutchPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4068.ConceptCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.ConceptCouplingPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4071.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.ConceptGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4074.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.ConicalGearSetPowerFlow)

        @property
        def coupling_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4079.CouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(_4079.CouplingPowerFlow)

        @property
        def cvt_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4081.CVTPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.CVTPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4083.CycloidalAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.CycloidalAssemblyPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4090.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.CylindricalGearSetPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4096.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.FaceGearSetPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4100.FlexiblePinAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(_4100.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4103.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.GearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4107.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(_4107.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4111.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(
                _4111.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4114.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(
                _4114.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4117.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(
                _4117.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4125.PartToPartShearCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(_4125.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4127.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.PlanetaryGearSetPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4136.RollingRingAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.RollingRingAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4146.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4149.SpringDamperPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4152.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4155.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.StraightBevelGearSetPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4160.SynchroniserPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.SynchroniserPowerFlow)

        @property
        def torque_converter_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4164.TorqueConverterPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.TorqueConverterPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4171.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "_4174.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4174

            return self._parent._cast(_4174.ZerolBevelGearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
        ) -> "SpecialisedAssemblyPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssemblyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2483.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyPowerFlow._Cast_SpecialisedAssemblyPowerFlow":
        return self._Cast_SpecialisedAssemblyPowerFlow(self)
