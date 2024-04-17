"""MountableComponentCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2884
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "MountableComponentCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2790
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2863,
        _2867,
        _2870,
        _2873,
        _2874,
        _2875,
        _2882,
        _2887,
        _2888,
        _2891,
        _2895,
        _2898,
        _2901,
        _2906,
        _2909,
        _2913,
        _2918,
        _2922,
        _2926,
        _2929,
        _2932,
        _2935,
        _2936,
        _2938,
        _2942,
        _2945,
        _2946,
        _2947,
        _2948,
        _2949,
        _2952,
        _2957,
        _2960,
        _2965,
        _2966,
        _2969,
        _2972,
        _2973,
        _2975,
        _2976,
        _2977,
        _2980,
        _2981,
        _2982,
        _2983,
        _2984,
        _2987,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundSystemDeflection",)


Self = TypeVar("Self", bound="MountableComponentCompoundSystemDeflection")


class MountableComponentCompoundSystemDeflection(
    _2884.ComponentCompoundSystemDeflection
):
    """MountableComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundSystemDeflection"
    )

    class _Cast_MountableComponentCompoundSystemDeflection:
        """Special nested class for casting MountableComponentCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
            parent: "MountableComponentCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2863.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def bearing_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2867.BearingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(_2867.BearingCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2870.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2870,
            )

            return self._parent._cast(
                _2870.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2873.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(
                _2873.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2874.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(
                _2874.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2875.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(_2875.BevelGearCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2882.ClutchHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ClutchHalfCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2887.ConceptCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(_2887.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2888.ConceptGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.ConceptGearCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2891.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.ConicalGearCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2895.ConnectorCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.ConnectorCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2898.CouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(_2898.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2901.CVTPulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2901,
            )

            return self._parent._cast(_2901.CVTPulleyCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2906.CylindricalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2909.CylindricalPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(
                _2909.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def face_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2913.FaceGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.FaceGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2918.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(_2918.GearCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2922.HypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2922,
            )

            return self._parent._cast(_2922.HypoidGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(
                _2926.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2929.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(
                _2929.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2932.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(
                _2932.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def mass_disc_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2935.MassDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2936.MeasurementComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(
                _2936.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def oil_seal_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2938.OilSealCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(_2938.OilSealCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2942.PartToPartShearCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(
                _2942.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def planet_carrier_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2945.PlanetCarrierCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2945,
            )

            return self._parent._cast(_2945.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2946.PointLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(_2946.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2947.PowerLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2947,
            )

            return self._parent._cast(_2947.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2948.PulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2949.RingPinsCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2952.RollingRingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.RollingRingCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2957.ShaftHubConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(_2957.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2960.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(_2960.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2965.SpringDamperHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(_2965.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2966.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(
                _2966.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2969.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2972.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(
                _2972.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2973.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(
                _2973.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def synchroniser_half_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2975.SynchroniserHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2976.SynchroniserPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2977.SynchroniserSleeveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2980.TorqueConverterPumpCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2980,
            )

            return self._parent._cast(_2980.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2981.TorqueConverterTurbineCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2981,
            )

            return self._parent._cast(
                _2981.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2982.UnbalancedMassCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2982,
            )

            return self._parent._cast(_2982.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2983.VirtualComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2983,
            )

            return self._parent._cast(_2983.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2984.WormGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2984,
            )

            return self._parent._cast(_2984.WormGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "_2987.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2987,
            )

            return self._parent._cast(_2987.ZerolBevelGearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
        ) -> "MountableComponentCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "MountableComponentCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2790.MountableComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2790.MountableComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection]

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
    ) -> "MountableComponentCompoundSystemDeflection._Cast_MountableComponentCompoundSystemDeflection":
        return self._Cast_MountableComponentCompoundSystemDeflection(self)
