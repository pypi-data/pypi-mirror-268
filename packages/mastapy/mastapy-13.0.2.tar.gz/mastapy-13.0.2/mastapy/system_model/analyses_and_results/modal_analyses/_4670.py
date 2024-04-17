"""PartModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "PartModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4662,
        _4580,
        _4581,
        _4582,
        _4585,
        _4586,
        _4587,
        _4588,
        _4590,
        _4592,
        _4593,
        _4594,
        _4595,
        _4597,
        _4598,
        _4599,
        _4600,
        _4602,
        _4603,
        _4605,
        _4607,
        _4608,
        _4610,
        _4611,
        _4613,
        _4614,
        _4616,
        _4619,
        _4620,
        _4622,
        _4623,
        _4624,
        _4626,
        _4629,
        _4630,
        _4631,
        _4632,
        _4636,
        _4638,
        _4639,
        _4640,
        _4641,
        _4644,
        _4645,
        _4646,
        _4648,
        _4649,
        _4652,
        _4653,
        _4655,
        _4656,
        _4658,
        _4659,
        _4660,
        _4661,
        _4666,
        _4668,
        _4672,
        _4673,
        _4675,
        _4676,
        _4677,
        _4678,
        _4679,
        _4680,
        _4682,
        _4684,
        _4685,
        _4686,
        _4687,
        _4690,
        _4692,
        _4693,
        _4695,
        _4696,
        _4698,
        _4699,
        _4701,
        _4702,
        _4703,
        _4704,
        _4705,
        _4706,
        _4707,
        _4708,
        _4710,
        _4711,
        _4712,
        _4713,
        _4714,
        _4719,
        _4720,
        _4722,
        _4723,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4734,
        _4732,
        _4735,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2793
    from mastapy.system_model.drawing import _2258
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartModalAnalysis",)


Self = TypeVar("Self", bound="PartModalAnalysis")


class PartModalAnalysis(_7556.PartStaticLoadAnalysisCase):
    """PartModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartModalAnalysis")

    class _Cast_PartModalAnalysis:
        """Special nested class for casting PartModalAnalysis to subclasses."""

        def __init__(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
            parent: "PartModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4580.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.AbstractAssemblyModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4581.AbstractShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4582.AbstractShaftOrHousingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4585.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.AGMAGleasonConicalGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4586.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4587.AssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.AssemblyModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4588.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BearingModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4590.BeltDriveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4592.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592

            return self._parent._cast(_4592.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4593.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4594.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4595.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4597.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.BevelGearModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4598.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4599.BoltedJointModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.BoltedJointModalAnalysis)

        @property
        def bolt_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4600.BoltModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4602.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ClutchHalfModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4603.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ClutchModalAnalysis)

        @property
        def component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4607.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4608.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4610.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.ConceptGearModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4611.ConceptGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4613.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.ConicalGearModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4614.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.ConicalGearSetModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4616.ConnectorModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4619.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(_4619.CouplingHalfModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4620.CouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4622.CVTModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.CVTModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4623.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.CVTPulleyModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4624.CycloidalAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624

            return self._parent._cast(_4624.CycloidalAssemblyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4626.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4629.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.CylindricalGearModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4630.CylindricalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.CylindricalGearSetModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4631.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4632.DatumModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4636.ExternalCADModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4638.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.FaceGearModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4639.FaceGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.FaceGearSetModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4640.FEPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(_4640.FEPartModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4641.FlexiblePinAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4644.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(_4644.GearModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4645.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(_4645.GearSetModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4646.GuideDxfModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(_4646.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4648.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(_4648.HypoidGearModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4649.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(_4649.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4652.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652

            return self._parent._cast(
                _4652.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4653.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(
                _4653.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4655.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(
                _4655.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4656.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656

            return self._parent._cast(
                _4656.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4658.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(
                _4658.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4659.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(
                _4659.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4660.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4661.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4666.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4668.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(_4668.OilSealModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4672.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4673.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4675.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.PlanetaryGearSetModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4676.PlanetCarrierModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676

            return self._parent._cast(_4676.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4677.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677

            return self._parent._cast(_4677.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4678.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4679.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4680.RingPinsModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.RingPinsModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4682.RollingRingAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.RollingRingAssemblyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4684.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.RollingRingModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4685.RootAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.RootAssemblyModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4686.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4687.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.ShaftModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4690.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4692.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.SpiralBevelGearModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4693.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4695.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.SpringDamperHalfModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4696.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4698.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4699.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4701.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4702.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.StraightBevelGearSetModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4703.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4704.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4704

            return self._parent._cast(_4704.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4705.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4706.SynchroniserModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.SynchroniserModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4707.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4708.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4710.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.TorqueConverterModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4711.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4712.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4713.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4714.VirtualComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4719.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4719

            return self._parent._cast(_4719.WormGearModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4720.WormGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4720

            return self._parent._cast(_4720.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4722.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4722

            return self._parent._cast(_4722.ZerolBevelGearModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4723.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4723

            return self._parent._cast(_4723.ZerolBevelGearSetModalAnalysis)

        @property
        def part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "PartModalAnalysis":
            return self._parent

        def __getattr__(self: "PartModalAnalysis._Cast_PartModalAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def modal_analysis(self: Self) -> "_4662.ModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def excited_modes_summary(
        self: Self,
    ) -> "List[_4734.SingleExcitationResultsModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.SingleExcitationResultsModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitedModesSummary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_excitation_details(
        self: Self,
    ) -> "List[_4732.RigidlyConnectedDesignEntityGroupModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_for_modes(self: Self) -> "List[_4735.SingleModeResults]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.SingleModeResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForModes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_excitation_details(
        self: Self,
    ) -> "List[_4732.RigidlyConnectedDesignEntityGroupModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2793.PartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2258.ModalAnalysisViewable":
        """mastapy.system_model.drawing.ModalAnalysisViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartModalAnalysis._Cast_PartModalAnalysis":
        return self._Cast_PartModalAnalysis(self)
