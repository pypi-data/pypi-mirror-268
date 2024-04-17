"""SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5497
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5543,
        _5547,
        _5550,
        _5555,
        _5557,
        _5558,
        _5563,
        _5568,
        _5571,
        _5574,
        _5578,
        _5580,
        _5586,
        _5592,
        _5594,
        _5597,
        _5601,
        _5605,
        _5608,
        _5611,
        _5617,
        _5621,
        _5628,
        _5638,
        _5639,
        _5644,
        _5647,
        _5650,
        _5654,
        _5662,
        _5665,
        _5616,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis")


class SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis(
    _5537.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
):
    """SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
            parent: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5537.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5537.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5543.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5543,
            )

            return self._parent._cast(
                _5543.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5547.BeltDriveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5547,
            )

            return self._parent._cast(_5547.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5550.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(
                _5550.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5555.BevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5555,
            )

            return self._parent._cast(
                _5555.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5557.BoltedJointCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5558.ClutchCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5558,
            )

            return self._parent._cast(_5558.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5563.ConceptCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(
                _5563.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5568.ConceptGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(
                _5568.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5571.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5571,
            )

            return self._parent._cast(
                _5571.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5574.CouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(_5574.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5578.CVTCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5578,
            )

            return self._parent._cast(_5578.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(
                _5580.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5586.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(
                _5586.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5592.FaceGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5592,
            )

            return self._parent._cast(
                _5592.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5594.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5597.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(_5597.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5601.HypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5601,
            )

            return self._parent._cast(
                _5601.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5605.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(
                _5608.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5611.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5611,
            )

            return self._parent._cast(
                _5611.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5617.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(
                _5617.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5621.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5621,
            )

            return self._parent._cast(
                _5621.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5628.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5628,
            )

            return self._parent._cast(
                _5628.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5638.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5639.SpringDamperCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5644.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5647.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5650.SynchroniserCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5654.TorqueConverterCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(
                _5654.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5662.WormGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5662,
            )

            return self._parent._cast(
                _5662.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5665.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5665,
            )

            return self._parent._cast(
                _5665.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5497.SpecialisedAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpecialisedAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "List[_5497.SpecialisedAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpecialisedAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis(self)
