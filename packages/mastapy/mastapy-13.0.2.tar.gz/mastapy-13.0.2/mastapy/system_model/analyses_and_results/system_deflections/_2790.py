"""MountableComponentSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2723
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "MountableComponentSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2765,
        _2699,
        _2706,
        _2711,
        _2712,
        _2713,
        _2716,
        _2720,
        _2726,
        _2730,
        _2734,
        _2736,
        _2738,
        _2741,
        _2753,
        _2754,
        _2755,
        _2758,
        _2764,
        _2769,
        _2773,
        _2778,
        _2781,
        _2784,
        _2787,
        _2788,
        _2792,
        _2795,
        _2798,
        _2799,
        _2800,
        _2801,
        _2802,
        _2807,
        _2809,
        _2817,
        _2819,
        _2823,
        _2826,
        _2827,
        _2828,
        _2829,
        _2830,
        _2831,
        _2837,
        _2839,
        _2842,
        _2843,
        _2846,
        _2849,
        _2793,
    )
    from mastapy.system_model.fe import _2392
    from mastapy.system_model.analyses_and_results.power_flows import _4120
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentSystemDeflection",)


Self = TypeVar("Self", bound="MountableComponentSystemDeflection")


class MountableComponentSystemDeflection(_2723.ComponentSystemDeflection):
    """MountableComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentSystemDeflection")

    class _Cast_MountableComponentSystemDeflection:
        """Special nested class for casting MountableComponentSystemDeflection to subclasses."""

        def __init__(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
            parent: "MountableComponentSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2699.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bearing_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2706.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BearingSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2711.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2712.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2713.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2716.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.BevelGearSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2720.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2726.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2730.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.ConceptGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2734.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2736.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2738.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.CouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2741.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.CVTPulleySystemDeflection)

        @property
        def cylindrical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2753.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2754.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2755.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(
                _2755.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2758.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.CylindricalPlanetGearSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2764.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.FaceGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2769.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(_2769.GearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2773.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(_2773.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2778.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(
                _2778.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(
                _2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2784.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(
                _2784.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2787.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2788.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.MeasurementComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2792.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2795.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2798.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2799.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2800.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2800,
            )

            return self._parent._cast(_2800.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2801.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2802.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.RingPinsSystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2807.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.RollingRingSystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2809.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.ShaftHubConnectionSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2817.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2819.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SpringDamperHalfSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2823.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2826.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2827.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2828.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2829.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2830.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2831.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2837.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2839.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2842.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2843.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.VirtualComponentSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2846.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "_2849.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2849,
            )

            return self._parent._cast(_2849.ZerolBevelGearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "MountableComponentSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "MountableComponentSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dip_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DipFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2471.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_fe_part(self: Self) -> "_2765.FEPartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerFEPart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_fe_substructure_nodes(self: Self) -> "List[_2392.FESubstructureNode]":
        """List[mastapy.system_model.fe.FESubstructureNode]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerFESubstructureNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4120.MountableComponentPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection":
        return self._Cast_MountableComponentSystemDeflection(self)
