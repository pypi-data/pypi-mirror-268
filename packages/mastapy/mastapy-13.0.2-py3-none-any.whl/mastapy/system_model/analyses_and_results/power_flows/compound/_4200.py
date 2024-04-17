"""ComponentCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4254
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4065
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4176,
        _4177,
        _4179,
        _4183,
        _4186,
        _4189,
        _4190,
        _4191,
        _4194,
        _4198,
        _4203,
        _4204,
        _4207,
        _4211,
        _4214,
        _4217,
        _4220,
        _4222,
        _4225,
        _4226,
        _4227,
        _4228,
        _4231,
        _4233,
        _4236,
        _4237,
        _4241,
        _4244,
        _4247,
        _4250,
        _4251,
        _4252,
        _4253,
        _4257,
        _4260,
        _4261,
        _4262,
        _4263,
        _4264,
        _4267,
        _4270,
        _4271,
        _4274,
        _4279,
        _4280,
        _4283,
        _4286,
        _4287,
        _4289,
        _4290,
        _4291,
        _4294,
        _4295,
        _4296,
        _4297,
        _4298,
        _4301,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="ComponentCompoundPowerFlow")


class ComponentCompoundPowerFlow(_4254.PartCompoundPowerFlow):
    """ComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundPowerFlow")

    class _Cast_ComponentCompoundPowerFlow:
        """Special nested class for casting ComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
            parent: "ComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4254.PartCompoundPowerFlow":
            return self._parent._cast(_4254.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4176.AbstractShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4177.AbstractShaftOrHousingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(_4177.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4179.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4183.BearingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4183,
            )

            return self._parent._cast(_4183.BearingCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4186.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4186,
            )

            return self._parent._cast(_4186.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4189.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(
                _4189.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4190.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4191.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.BevelGearCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4194.BoltCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.BoltCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4198.ClutchHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4203.ConceptCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4204.ConceptGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4207.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4207,
            )

            return self._parent._cast(_4207.ConicalGearCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4211.ConnectorCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4211,
            )

            return self._parent._cast(_4211.ConnectorCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4214.CouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4217.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4220.CycloidalDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.CycloidalDiscCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4222.CylindricalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4225.CylindricalPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4226.DatumCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4227.ExternalCADModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4228.FaceGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4228,
            )

            return self._parent._cast(_4228.FaceGearCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4231.FEPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(_4231.FEPartCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4233.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(_4233.GearCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4236.GuideDxfModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4236,
            )

            return self._parent._cast(_4236.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4237.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(_4237.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4241.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(
                _4241.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4244.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(
                _4244.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4247.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(
                _4247.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4250.MassDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4251.MeasurementComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4252.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4253.OilSealCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(_4253.OilSealCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4257.PartToPartShearCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(
                _4257.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planet_carrier_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4260.PlanetCarrierCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4260,
            )

            return self._parent._cast(_4260.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4261.PointLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(_4261.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4262.PowerLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4263.PulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4264.RingPinsCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4267.RollingRingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.RollingRingCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4270.ShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4271.ShaftHubConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.ShaftHubConnectionCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4274.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.SpiralBevelGearCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4279.SpringDamperHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4280.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4283.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4286.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4287.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4289.SynchroniserHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4290.SynchroniserPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4291.SynchroniserSleeveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4294.TorqueConverterPumpCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4294,
            )

            return self._parent._cast(_4294.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4295.TorqueConverterTurbineCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4296.UnbalancedMassCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4296,
            )

            return self._parent._cast(_4296.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4297.VirtualComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4297,
            )

            return self._parent._cast(_4297.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4298.WormGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4298,
            )

            return self._parent._cast(_4298.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4301.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4301,
            )

            return self._parent._cast(_4301.ZerolBevelGearCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "ComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4065.ComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4065.ComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow":
        return self._Cast_ComponentCompoundPowerFlow(self)
