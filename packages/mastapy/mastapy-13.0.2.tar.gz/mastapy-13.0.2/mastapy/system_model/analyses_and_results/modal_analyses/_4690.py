"""SpecialisedAssemblyModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4580
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpecialisedAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483
    from mastapy.system_model.analyses_and_results.system_deflections import _2814
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4586,
        _4590,
        _4593,
        _4598,
        _4599,
        _4603,
        _4608,
        _4611,
        _4614,
        _4620,
        _4622,
        _4624,
        _4630,
        _4639,
        _4641,
        _4645,
        _4649,
        _4653,
        _4656,
        _4659,
        _4673,
        _4675,
        _4682,
        _4693,
        _4696,
        _4699,
        _4702,
        _4706,
        _4710,
        _4720,
        _4723,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyModalAnalysis")


class SpecialisedAssemblyModalAnalysis(_4580.AbstractAssemblyModalAnalysis):
    """SpecialisedAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyModalAnalysis")

    class _Cast_SpecialisedAssemblyModalAnalysis:
        """Special nested class for casting SpecialisedAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
            parent: "SpecialisedAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4580.AbstractAssemblyModalAnalysis":
            return self._parent._cast(_4580.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4586.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4590.BeltDriveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4593.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4598.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4599.BoltedJointModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.BoltedJointModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4603.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4608.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4611.ConceptGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4614.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.ConicalGearSetModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4620.CouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4622.CVTModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.CVTModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4624.CycloidalAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624

            return self._parent._cast(_4624.CycloidalAssemblyModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4630.CylindricalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4639.FaceGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.FaceGearSetModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4641.FlexiblePinAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4645.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(_4645.GearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4649.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(_4649.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4653.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(
                _4653.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4656.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656

            return self._parent._cast(
                _4656.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4659.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(
                _4659.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4673.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4675.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.PlanetaryGearSetModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4682.RollingRingAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.RollingRingAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4693.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4696.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4699.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4702.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.StraightBevelGearSetModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4706.SynchroniserModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.SynchroniserModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4710.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.TorqueConverterModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4720.WormGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4720

            return self._parent._cast(_4720.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "_4723.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4723

            return self._parent._cast(_4723.ZerolBevelGearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "SpecialisedAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssemblyModalAnalysis.TYPE"):
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
    def system_deflection_results(
        self: Self,
    ) -> "_2814.SpecialisedAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection

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
    ) -> "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis":
        return self._Cast_SpecialisedAssemblyModalAnalysis(self)
