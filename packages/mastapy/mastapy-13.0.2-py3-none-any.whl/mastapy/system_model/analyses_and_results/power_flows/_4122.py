"""PartPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PartPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4130,
        _4040,
        _4041,
        _4042,
        _4045,
        _4046,
        _4047,
        _4048,
        _4050,
        _4052,
        _4053,
        _4054,
        _4055,
        _4057,
        _4058,
        _4059,
        _4060,
        _4062,
        _4063,
        _4065,
        _4067,
        _4068,
        _4070,
        _4071,
        _4073,
        _4074,
        _4076,
        _4078,
        _4079,
        _4081,
        _4082,
        _4083,
        _4086,
        _4089,
        _4090,
        _4091,
        _4092,
        _4093,
        _4095,
        _4096,
        _4099,
        _4100,
        _4102,
        _4103,
        _4104,
        _4106,
        _4107,
        _4110,
        _4111,
        _4113,
        _4114,
        _4116,
        _4117,
        _4118,
        _4119,
        _4120,
        _4121,
        _4124,
        _4125,
        _4127,
        _4128,
        _4129,
        _4132,
        _4133,
        _4134,
        _4136,
        _4138,
        _4139,
        _4140,
        _4141,
        _4143,
        _4145,
        _4146,
        _4148,
        _4149,
        _4151,
        _4152,
        _4154,
        _4155,
        _4156,
        _4157,
        _4158,
        _4159,
        _4160,
        _4161,
        _4164,
        _4165,
        _4166,
        _4167,
        _4168,
        _4170,
        _4171,
        _4173,
        _4174,
    )
    from mastapy.system_model.drawing import _2261
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartPowerFlow",)


Self = TypeVar("Self", bound="PartPowerFlow")


class PartPowerFlow(_7556.PartStaticLoadAnalysisCase):
    """PartPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartPowerFlow")

    class _Cast_PartPowerFlow:
        """Special nested class for casting PartPowerFlow to subclasses."""

        def __init__(
            self: "PartPowerFlow._Cast_PartPowerFlow", parent: "PartPowerFlow"
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4040.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4041.AbstractShaftOrHousingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4042.AbstractShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4045.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4046.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4047.AssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.AssemblyPowerFlow)

        @property
        def bearing_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4048.BearingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BearingPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4050.BeltDrivePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4050

            return self._parent._cast(_4050.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4052.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4053.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4054.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4055.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4057.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4058.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4059.BoltedJointPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4060.BoltPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.BoltPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4062.ClutchHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4063.ClutchPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ClutchPowerFlow)

        @property
        def component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4065.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4067.ConceptCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4068.ConceptCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4070.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4071.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4073.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4074.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4076.ConnectorPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(_4076.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4078.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4079.CouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(_4079.CouplingPowerFlow)

        @property
        def cvt_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4081.CVTPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4082.CVTPulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4083.CycloidalAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4086.CycloidalDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4089.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4090.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4091.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4092.DatumPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4093.ExternalCADModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4095.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4096.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4099.FEPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(_4099.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4100.FlexiblePinAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(_4100.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4102.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.GearPowerFlow)

        @property
        def gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4103.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4104.GuideDxfModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(_4104.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4106.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(_4106.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4107.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(_4107.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4110.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(
                _4110.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4111.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(
                _4111.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4113.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4114.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(
                _4114.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4116.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(
                _4116.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4117.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(
                _4117.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4118.MassDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4119.MeasurementComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4120.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4121.OilSealPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4124.PartToPartShearCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(_4124.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4125.PartToPartShearCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(_4125.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4127.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4128.PlanetCarrierPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4129.PointLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4132.PowerLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4133.PulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4134.RingPinsPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4136.RollingRingAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4138.RollingRingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4139.RootAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4140.ShaftHubConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4141.ShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4143.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4145.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4146.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4148.SpringDamperHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4149.SpringDamperPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4151.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4152.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4154.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4155.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4156.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4157.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4158.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4159.SynchroniserPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4160.SynchroniserPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4161.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4164.TorqueConverterPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4165.TorqueConverterPumpPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4166.TorqueConverterTurbinePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4167.UnbalancedMassPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4168.VirtualComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4168

            return self._parent._cast(_4168.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4170.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4171.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4173.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4173

            return self._parent._cast(_4173.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4174.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4174

            return self._parent._cast(_4174.ZerolBevelGearSetPowerFlow)

        @property
        def part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "PartPowerFlow":
            return self._parent

        def __getattr__(self: "PartPowerFlow._Cast_PartPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_power_flow(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2475.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow(self: Self) -> "_4130.PowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2261.PowerFlowViewable":
        """mastapy.system_model.drawing.PowerFlowViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartPowerFlow._Cast_PartPowerFlow":
        return self._Cast_PartPowerFlow(self)
