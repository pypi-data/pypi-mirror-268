"""MountableComponentHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5713
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "MountableComponentHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.modal_analyses import _4666
    from mastapy.system_model.analyses_and_results.system_deflections import _2790
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5691,
        _5695,
        _5698,
        _5701,
        _5702,
        _5703,
        _5709,
        _5715,
        _5717,
        _5720,
        _5724,
        _5726,
        _5730,
        _5735,
        _5738,
        _5755,
        _5761,
        _5779,
        _5783,
        _5786,
        _5789,
        _5792,
        _5793,
        _5795,
        _5798,
        _5803,
        _5804,
        _5805,
        _5806,
        _5808,
        _5812,
        _5815,
        _5820,
        _5824,
        _5827,
        _5830,
        _5833,
        _5834,
        _5835,
        _5837,
        _5838,
        _5841,
        _5842,
        _5844,
        _5845,
        _5846,
        _5849,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentHarmonicAnalysis",)


Self = TypeVar("Self", bound="MountableComponentHarmonicAnalysis")


class MountableComponentHarmonicAnalysis(_5713.ComponentHarmonicAnalysis):
    """MountableComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentHarmonicAnalysis")

    class _Cast_MountableComponentHarmonicAnalysis:
        """Special nested class for casting MountableComponentHarmonicAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
            parent: "MountableComponentHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5691.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5695.BearingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BearingHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5698.BevelDifferentialGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5698,
            )

            return self._parent._cast(_5698.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5701.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5702.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5703.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.BevelGearHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5709.ClutchHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5715.ConceptCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5717.ConceptGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.ConceptGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5720.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.ConicalGearHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5724.ConnectorHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(_5724.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5726.CouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.CouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5730.CVTPulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5730,
            )

            return self._parent._cast(_5730.CVTPulleyHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5735.CylindricalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5735,
            )

            return self._parent._cast(_5735.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5738.CylindricalPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5738,
            )

            return self._parent._cast(_5738.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5755.FaceGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(_5755.FaceGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5761.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(_5761.GearHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5779.HypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(_5779.HypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5783.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(
                _5783.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5786.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(
                _5786.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5789.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5789,
            )

            return self._parent._cast(
                _5789.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5792.MassDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5792,
            )

            return self._parent._cast(_5792.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5793.MeasurementComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5793,
            )

            return self._parent._cast(_5793.MeasurementComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5795.OilSealHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(_5795.OilSealHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5798.PartToPartShearCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(_5798.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5803.PlanetCarrierHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(_5803.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5804.PointLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(_5804.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5805.PowerLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(_5805.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5806.PulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5808.RingPinsHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(_5808.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5812.RollingRingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.RollingRingHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5815.ShaftHubConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.ShaftHubConnectionHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5820.SpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.SpiralBevelGearHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5824.SpringDamperHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.SpringDamperHalfHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5827.StraightBevelDiffGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5827,
            )

            return self._parent._cast(_5827.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5830.StraightBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5833.StraightBevelPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5834.StraightBevelSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5835.SynchroniserHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5835,
            )

            return self._parent._cast(_5835.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5837.SynchroniserPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5838.SynchroniserSleeveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5841.TorqueConverterPumpHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5841,
            )

            return self._parent._cast(_5841.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5842.TorqueConverterTurbineHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5842,
            )

            return self._parent._cast(_5842.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5844.UnbalancedMassHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5844,
            )

            return self._parent._cast(_5844.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5845.VirtualComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5845,
            )

            return self._parent._cast(_5845.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5846.WormGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5846,
            )

            return self._parent._cast(_5846.WormGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "_5849.ZerolBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5849,
            )

            return self._parent._cast(_5849.ZerolBevelGearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "MountableComponentHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def coupled_modal_analysis(self: Self) -> "_4666.MountableComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2790.MountableComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis":
        return self._Cast_MountableComponentHarmonicAnalysis(self)
