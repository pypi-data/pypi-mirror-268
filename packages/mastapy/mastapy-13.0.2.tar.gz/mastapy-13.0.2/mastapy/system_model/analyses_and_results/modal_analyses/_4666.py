"""MountableComponentModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4605
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "MountableComponentModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.system_deflections import _2790
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4585,
        _4588,
        _4592,
        _4594,
        _4595,
        _4597,
        _4602,
        _4607,
        _4610,
        _4613,
        _4616,
        _4619,
        _4623,
        _4629,
        _4631,
        _4638,
        _4644,
        _4648,
        _4652,
        _4655,
        _4658,
        _4660,
        _4661,
        _4668,
        _4672,
        _4676,
        _4677,
        _4678,
        _4679,
        _4680,
        _4684,
        _4686,
        _4692,
        _4695,
        _4698,
        _4701,
        _4703,
        _4704,
        _4705,
        _4707,
        _4708,
        _4711,
        _4712,
        _4713,
        _4714,
        _4719,
        _4722,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentModalAnalysis",)


Self = TypeVar("Self", bound="MountableComponentModalAnalysis")


class MountableComponentModalAnalysis(_4605.ComponentModalAnalysis):
    """MountableComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentModalAnalysis")

    class _Cast_MountableComponentModalAnalysis:
        """Special nested class for casting MountableComponentModalAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
            parent: "MountableComponentModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4585.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.AGMAGleasonConicalGearModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4588.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BearingModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4592.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592

            return self._parent._cast(_4592.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4594.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4595.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4597.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.BevelGearModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4602.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4607.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4610.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.ConceptGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4613.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.ConicalGearModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4616.ConnectorModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4619.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(_4619.CouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4623.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.CVTPulleyModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4629.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.CylindricalGearModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4631.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.CylindricalPlanetGearModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4638.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.FaceGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4644.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(_4644.GearModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4648.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(_4648.HypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4652.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652

            return self._parent._cast(
                _4652.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4655.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(
                _4655.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4658.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(
                _4658.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4660.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4661.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.MeasurementComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4668.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(_4668.OilSealModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4672.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4676.PlanetCarrierModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676

            return self._parent._cast(_4676.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4677.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677

            return self._parent._cast(_4677.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4678.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4679.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4680.RingPinsModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.RingPinsModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4684.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.RollingRingModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4686.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.ShaftHubConnectionModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4692.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.SpiralBevelGearModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4695.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.SpringDamperHalfModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4698.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4701.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4703.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4704.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4704

            return self._parent._cast(_4704.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4705.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4707.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4708.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4711.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4712.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4713.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4714.VirtualComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4719.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4719

            return self._parent._cast(_4719.WormGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "_4722.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4722

            return self._parent._cast(_4722.ZerolBevelGearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "MountableComponentModalAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentModalAnalysis.TYPE"):
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
    ) -> "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis":
        return self._Cast_MountableComponentModalAnalysis(self)
