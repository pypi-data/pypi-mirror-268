"""ComponentSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2793
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ComponentSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.math_utility import _1525
    from mastapy.materials.efficiency import _305, _306
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2856,
    )
    from mastapy.math_utility.measured_vectors import _1568, _1569
    from mastapy.system_model.analyses_and_results.power_flows import _4065
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2694,
        _2695,
        _2699,
        _2706,
        _2711,
        _2712,
        _2713,
        _2716,
        _2718,
        _2720,
        _2726,
        _2730,
        _2734,
        _2736,
        _2738,
        _2741,
        _2746,
        _2753,
        _2754,
        _2755,
        _2758,
        _2759,
        _2760,
        _2764,
        _2765,
        _2769,
        _2770,
        _2773,
        _2778,
        _2781,
        _2784,
        _2787,
        _2788,
        _2790,
        _2792,
        _2795,
        _2798,
        _2799,
        _2800,
        _2801,
        _2802,
        _2807,
        _2809,
        _2812,
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
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ComponentSystemDeflection",)


Self = TypeVar("Self", bound="ComponentSystemDeflection")


class ComponentSystemDeflection(_2793.PartSystemDeflection):
    """ComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentSystemDeflection")

    class _Cast_ComponentSystemDeflection:
        """Special nested class for casting ComponentSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
            parent: "ComponentSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2694.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2694,
            )

            return self._parent._cast(_2694.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2695.AbstractShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2695,
            )

            return self._parent._cast(_2695.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2699.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bearing_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2706.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BearingSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2711.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2712.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2713.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2716.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.BevelGearSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2718.BoltSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2718,
            )

            return self._parent._cast(_2718.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2720.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2726.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2730.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.ConceptGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2734.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2736.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2738.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.CouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2741.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.CVTPulleySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2746.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2746,
            )

            return self._parent._cast(_2746.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2753.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2754.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2755.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(
                _2755.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2758.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2759.DatumSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2760.ExternalCADModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.ExternalCADModelSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2764.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2765.FEPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(_2765.FEPartSystemDeflection)

        @property
        def gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2769.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(_2769.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2770.GuideDxfModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(_2770.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2773.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(_2773.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2778.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(
                _2778.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(
                _2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2784.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(
                _2784.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2787.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2788.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2790.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2792.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2795.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2798.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2799.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2800.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2800,
            )

            return self._parent._cast(_2800.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2801.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2802.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.RingPinsSystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2807.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.RollingRingSystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2809.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2812.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.ShaftSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2817.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2819.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SpringDamperHalfSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2823.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2826.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2827.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2828.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2829.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2830.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2831.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2837.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2839.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2842.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2843.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.VirtualComponentSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2846.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2849.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2849,
            )

            return self._parent._cast(_2849.ZerolBevelGearSystemDeflection)

        @property
        def component_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "ComponentSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def energy_loss_during_load_case(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyLossDuringLoadCase

        if temp is None:
            return 0.0

        return temp

    @property
    def has_converged(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasConverged

        if temp is None:
            return False

        return temp

    @property
    def percentage_of_iterations_converged(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageOfIterationsConverged

        if temp is None:
            return 0.0

        return temp

    @property
    def reason_for_non_convergence(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonForNonConvergence

        if temp is None:
            return ""

        return temp

    @property
    def reason_mass_properties_are_unknown(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonMassPropertiesAreUnknown

        if temp is None:
            return ""

        return temp

    @property
    def reason_mass_properties_are_zero(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonMassPropertiesAreZero

        if temp is None:
            return ""

        return temp

    @property
    def relaxation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Relaxation

        if temp is None:
            return 0.0

        return temp

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
    def mass_properties_in_local_coordinate_system_from_node_model(
        self: Self,
    ) -> "_1525.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesInLocalCoordinateSystemFromNodeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_loss(self: Self) -> "_305.PowerLoss":
        """mastapy.materials.efficiency.PowerLoss

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def resistive_torque(self: Self) -> "_306.ResistiveTorque":
        """mastapy.materials.efficiency.ResistiveTorque

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rigidly_connected_components(
        self: Self,
    ) -> "_2856.RigidlyConnectedComponentGroupSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.reporting.RigidlyConnectedComponentGroupSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedComponents

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connected_components_forces_in_lcs(self: Self) -> "List[_1568.ForceResults]":
        """List[mastapy.math_utility.measured_vectors.ForceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponentsForcesInLCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connected_components_forces_in_wcs(self: Self) -> "List[_1568.ForceResults]":
        """List[mastapy.math_utility.measured_vectors.ForceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponentsForcesInWCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def node_results(self: Self) -> "List[_1569.NodeResults]":
        """List[mastapy.math_utility.measured_vectors.NodeResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4065.ComponentPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow

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
    ) -> "ComponentSystemDeflection._Cast_ComponentSystemDeflection":
        return self._Cast_ComponentSystemDeflection(self)
