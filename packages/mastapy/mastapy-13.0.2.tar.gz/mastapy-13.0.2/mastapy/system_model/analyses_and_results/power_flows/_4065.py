"""ComponentPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4122
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ComponentPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4041,
        _4042,
        _4045,
        _4048,
        _4052,
        _4054,
        _4055,
        _4057,
        _4060,
        _4062,
        _4067,
        _4070,
        _4073,
        _4076,
        _4078,
        _4082,
        _4086,
        _4089,
        _4091,
        _4092,
        _4093,
        _4095,
        _4099,
        _4102,
        _4104,
        _4106,
        _4110,
        _4113,
        _4116,
        _4118,
        _4119,
        _4120,
        _4121,
        _4124,
        _4128,
        _4129,
        _4132,
        _4133,
        _4134,
        _4138,
        _4140,
        _4141,
        _4145,
        _4148,
        _4151,
        _4154,
        _4156,
        _4157,
        _4158,
        _4159,
        _4161,
        _4165,
        _4166,
        _4167,
        _4168,
        _4170,
        _4173,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentPowerFlow",)


Self = TypeVar("Self", bound="ComponentPowerFlow")


class ComponentPowerFlow(_4122.PartPowerFlow):
    """ComponentPowerFlow

    This is a mastapy class.
    """

    TYPE = _COMPONENT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentPowerFlow")

    class _Cast_ComponentPowerFlow:
        """Special nested class for casting ComponentPowerFlow to subclasses."""

        def __init__(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
            parent: "ComponentPowerFlow",
        ):
            self._parent = parent

        @property
        def part_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4122.PartPowerFlow":
            return self._parent._cast(_4122.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4041.AbstractShaftOrHousingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4042.AbstractShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4045.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.AGMAGleasonConicalGearPowerFlow)

        @property
        def bearing_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4048.BearingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BearingPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4052.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4054.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4055.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4057.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.BevelGearPowerFlow)

        @property
        def bolt_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4060.BoltPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.BoltPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4062.ClutchHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ClutchHalfPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4067.ConceptCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConceptCouplingHalfPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4070.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.ConceptGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4073.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.ConicalGearPowerFlow)

        @property
        def connector_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4076.ConnectorPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(_4076.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4078.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.CouplingHalfPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4082.CVTPulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.CVTPulleyPowerFlow)

        @property
        def cycloidal_disc_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4086.CycloidalDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4089.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.CylindricalGearPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4091.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4092.DatumPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4093.ExternalCADModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4095.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.FaceGearPowerFlow)

        @property
        def fe_part_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4099.FEPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(_4099.FEPartPowerFlow)

        @property
        def gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4102.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.GearPowerFlow)

        @property
        def guide_dxf_model_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4104.GuideDxfModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(_4104.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4106.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(_4106.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4110.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(
                _4110.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4113.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4116.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(
                _4116.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4118.MassDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4119.MeasurementComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4120.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4121.OilSealPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4124.PartToPartShearCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(_4124.PartToPartShearCouplingHalfPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4128.PlanetCarrierPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4129.PointLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4132.PowerLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4133.PulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4134.RingPinsPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.RingPinsPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4138.RollingRingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.RollingRingPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4140.ShaftHubConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4141.ShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.ShaftPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4145.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.SpiralBevelGearPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4148.SpringDamperHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.SpringDamperHalfPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4151.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4154.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4156.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4157.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4158.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4159.SynchroniserPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.SynchroniserPartPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4161.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4165.TorqueConverterPumpPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4166.TorqueConverterTurbinePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4167.UnbalancedMassPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4168.VirtualComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4168

            return self._parent._cast(_4168.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4170.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.WormGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "_4173.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4173

            return self._parent._cast(_4173.ZerolBevelGearPowerFlow)

        @property
        def component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "ComponentPowerFlow":
            return self._parent

        def __getattr__(self: "ComponentPowerFlow._Cast_ComponentPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2451.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ComponentPowerFlow._Cast_ComponentPowerFlow":
        return self._Cast_ComponentPowerFlow(self)
