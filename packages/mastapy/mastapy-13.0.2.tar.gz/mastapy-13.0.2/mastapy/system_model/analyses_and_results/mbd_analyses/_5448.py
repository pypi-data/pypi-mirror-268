"""GearSetMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5497
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "GearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5447,
        _5445,
        _5390,
        _5399,
        _5404,
        _5418,
        _5421,
        _5436,
        _5442,
        _5452,
        _5460,
        _5463,
        _5466,
        _5480,
        _5500,
        _5506,
        _5509,
        _5527,
        _5530,
        _5384,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="GearSetMultibodyDynamicsAnalysis")


class GearSetMultibodyDynamicsAnalysis(
    _5497.SpecialisedAssemblyMultibodyDynamicsAnalysis
):
    """GearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetMultibodyDynamicsAnalysis")

    class _Cast_GearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting GearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
            parent: "GearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5497.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5497.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5384.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5390.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(
                _5390.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5399.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(
                _5399.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5404.BevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5418.ConceptGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5421.ConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5436.CylindricalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5442.FaceGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5442

            return self._parent._cast(_5442.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5452.HypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(_5452.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5460.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(
                _5460.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5463.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(
                _5463.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> (
            "_5466.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(
                _5466.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5480.PlanetaryGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5480

            return self._parent._cast(_5480.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5500.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(_5500.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5506.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(
                _5506.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5509.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5509

            return self._parent._cast(
                _5509.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5527.WormGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5527

            return self._parent._cast(_5527.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "_5530.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5530

            return self._parent._cast(_5530.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "GearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_5447.GearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes(self: Self) -> "List[_5445.GearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Meshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis":
        return self._Cast_GearSetMultibodyDynamicsAnalysis(self)
