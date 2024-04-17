"""AbstractAssemblyHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6097,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6022,
        _6023,
        _6026,
        _6029,
        _6034,
        _6035,
        _6039,
        _6044,
        _6047,
        _6050,
        _6055,
        _6057,
        _6059,
        _6065,
        _6071,
        _6073,
        _6076,
        _6081,
        _6085,
        _6088,
        _6091,
        _6100,
        _6102,
        _6109,
        _6112,
        _6116,
        _6119,
        _6122,
        _6125,
        _6128,
        _6132,
        _6136,
        _6143,
        _6146,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="AbstractAssemblyHarmonicAnalysisOfSingleExcitation")


class AbstractAssemblyHarmonicAnalysisOfSingleExcitation(
    _6097.PartHarmonicAnalysisOfSingleExcitation
):
    """AbstractAssemblyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractAssemblyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PartHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6097.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6022.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6022,
            )

            return self._parent._cast(
                _6022.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6023.AssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(_6023.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6026.BeltDriveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6026,
            )

            return self._parent._cast(_6026.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6029.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(
                _6029.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6034.BevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6035.BoltedJointHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(
                _6035.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6039.ClutchHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(_6039.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6044.ConceptCouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(
                _6044.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6047.ConceptGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(
                _6047.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6050.ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(
                _6050.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6055.CouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(_6055.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6057.CVTHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(_6057.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(
                _6059.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6065.CylindricalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(
                _6065.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6071.FaceGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6073.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6076.GearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(_6076.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6081.HypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6085.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(
                _6085.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6088.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(
                _6088.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(
                _6091.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6100.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6100,
            )

            return self._parent._cast(
                _6100.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6102.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(
                _6102.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6109.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(
                _6109.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6112.RootAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6112,
            )

            return self._parent._cast(
                _6112.RootAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6119.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6122.SpringDamperHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6125.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6128.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6132.SynchroniserHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6136.TorqueConverterHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6143.WormGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6143,
            )

            return self._parent._cast(
                _6143.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6146.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6146,
            )

            return self._parent._cast(
                _6146.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
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
        self: Self,
        instance_to_wrap: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2441.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2441.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation(self)
