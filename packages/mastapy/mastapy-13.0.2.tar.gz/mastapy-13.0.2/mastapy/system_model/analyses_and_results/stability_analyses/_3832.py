"""GearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3871
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "GearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3776,
        _3783,
        _3788,
        _3801,
        _3804,
        _3820,
        _3827,
        _3836,
        _3840,
        _3843,
        _3846,
        _3857,
        _3873,
        _3882,
        _3885,
        _3900,
        _3903,
        _3771,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="GearSetStabilityAnalysis")


class GearSetStabilityAnalysis(_3871.SpecialisedAssemblyStabilityAnalysis):
    """GearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetStabilityAnalysis")

    class _Cast_GearSetStabilityAnalysis:
        """Special nested class for casting GearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
            parent: "GearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3871.SpecialisedAssemblyStabilityAnalysis":
            return self._parent._cast(_3871.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3771.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3776.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3783.BevelDifferentialGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3788.BevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.BevelGearSetStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3801.ConceptGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3801,
            )

            return self._parent._cast(_3801.ConceptGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3804.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.ConicalGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3820.CylindricalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.CylindricalGearSetStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3827.FaceGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.FaceGearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3836.HypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(_3836.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3840.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(
                _3840.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3843.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(
                _3843.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3846.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(
                _3846.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def planetary_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3857.PlanetaryGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(_3857.PlanetaryGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3873.SpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.SpiralBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3882.StraightBevelDiffGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3885.StraightBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.StraightBevelGearSetStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3900.WormGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3900,
            )

            return self._parent._cast(_3900.WormGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3903.ZerolBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3903,
            )

            return self._parent._cast(_3903.ZerolBevelGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "GearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetStabilityAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis":
        return self._Cast_GearSetStabilityAnalysis(self)
