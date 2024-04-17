"""SpecialisedAssemblyHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5686
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "SpecialisedAssemblyHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483
    from mastapy.system_model.analyses_and_results.system_deflections import _2814
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5693,
        _5697,
        _5700,
        _5705,
        _5706,
        _5710,
        _5716,
        _5719,
        _5722,
        _5727,
        _5729,
        _5731,
        _5737,
        _5757,
        _5759,
        _5766,
        _5781,
        _5785,
        _5788,
        _5791,
        _5799,
        _5802,
        _5810,
        _5822,
        _5825,
        _5829,
        _5832,
        _5836,
        _5840,
        _5848,
        _5851,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyHarmonicAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyHarmonicAnalysis")


class SpecialisedAssemblyHarmonicAnalysis(_5686.AbstractAssemblyHarmonicAnalysis):
    """SpecialisedAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyHarmonicAnalysis")

    class _Cast_SpecialisedAssemblyHarmonicAnalysis:
        """Special nested class for casting SpecialisedAssemblyHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
            parent: "SpecialisedAssemblyHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5686.AbstractAssemblyHarmonicAnalysis":
            return self._parent._cast(_5686.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5693.AGMAGleasonConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5697.BeltDriveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5700.BevelDifferentialGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5705.BevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5706.BoltedJointHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5706,
            )

            return self._parent._cast(_5706.BoltedJointHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5710.ClutchHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ClutchHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5716.ConceptCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5719.ConceptGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5722.ConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.ConicalGearSetHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5727.CouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5727,
            )

            return self._parent._cast(_5727.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5729.CVTHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5729,
            )

            return self._parent._cast(_5729.CVTHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5731.CycloidalAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5737.CylindricalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5737,
            )

            return self._parent._cast(_5737.CylindricalGearSetHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5757.FaceGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5757,
            )

            return self._parent._cast(_5757.FaceGearSetHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5759.FlexiblePinAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5759,
            )

            return self._parent._cast(_5759.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5766.GearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5766,
            )

            return self._parent._cast(_5766.GearSetHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5781.HypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(_5781.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5785.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(
                _5785.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5788.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(
                _5788.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5791.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(
                _5791.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5799.PartToPartShearCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(_5799.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5802.PlanetaryGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(_5802.PlanetaryGearSetHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5810.RollingRingAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.RollingRingAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5822.SpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5825.SpringDamperHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5829.StraightBevelDiffGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5832.StraightBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.StraightBevelGearSetHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5836.SynchroniserHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.SynchroniserHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5840.TorqueConverterHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.TorqueConverterHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5848.WormGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5848,
            )

            return self._parent._cast(_5848.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5851.ZerolBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5851,
            )

            return self._parent._cast(_5851.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "SpecialisedAssemblyHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyHarmonicAnalysis.TYPE"
    ):
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
    ) -> (
        "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis"
    ):
        return self._Cast_SpecialisedAssemblyHarmonicAnalysis(self)
