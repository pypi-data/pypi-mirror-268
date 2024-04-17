"""SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _4996,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4965,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5002,
        _5006,
        _5009,
        _5014,
        _5016,
        _5017,
        _5022,
        _5027,
        _5030,
        _5033,
        _5037,
        _5039,
        _5045,
        _5051,
        _5053,
        _5056,
        _5060,
        _5064,
        _5067,
        _5070,
        _5076,
        _5080,
        _5087,
        _5097,
        _5098,
        _5103,
        _5106,
        _5109,
        _5113,
        _5121,
        _5124,
        _5075,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundModalAnalysisAtAStiffness")


class SpecialisedAssemblyCompoundModalAnalysisAtAStiffness(
    _4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness
):
    """SpecialisedAssemblyCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SpecialisedAssemblyCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
            parent: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4996.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5002.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5002,
            )

            return self._parent._cast(
                _5002.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5006.BeltDriveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5006,
            )

            return self._parent._cast(_5006.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5009.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(
                _5009.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5014.BevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5014,
            )

            return self._parent._cast(
                _5014.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5016.BoltedJointCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5016,
            )

            return self._parent._cast(
                _5016.BoltedJointCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5017.ClutchCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5017,
            )

            return self._parent._cast(_5017.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5022.ConceptCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5027.ConceptGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(
                _5027.ConceptGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5030.ConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5030,
            )

            return self._parent._cast(
                _5030.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5033.CouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5033,
            )

            return self._parent._cast(_5033.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5037.CVTCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5037,
            )

            return self._parent._cast(_5037.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5039.CycloidalAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5039,
            )

            return self._parent._cast(
                _5039.CycloidalAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5045.CylindricalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(
                _5045.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5051.FaceGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(
                _5051.FaceGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5053.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(
                _5053.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5056.GearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(_5056.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5060.HypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5060,
            )

            return self._parent._cast(
                _5060.HypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5064.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(
                _5067.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5070.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5070,
            )

            return self._parent._cast(
                _5070.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5076.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5076,
            )

            return self._parent._cast(
                _5076.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5080.PlanetaryGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5080,
            )

            return self._parent._cast(
                _5080.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5087.RollingRingAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5087,
            )

            return self._parent._cast(
                _5087.RollingRingAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5097.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5098.SpringDamperCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(
                _5098.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5103.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5103,
            )

            return self._parent._cast(
                _5103.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5106.StraightBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(
                _5106.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5109.SynchroniserCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.SynchroniserCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5113.TorqueConverterCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5113,
            )

            return self._parent._cast(
                _5113.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5121.WormGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5121,
            )

            return self._parent._cast(
                _5121.WormGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5124.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5124,
            )

            return self._parent._cast(
                _5124.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4965.SpecialisedAssemblyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpecialisedAssemblyModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4965.SpecialisedAssemblyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpecialisedAssemblyModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
        return self._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness(self)
