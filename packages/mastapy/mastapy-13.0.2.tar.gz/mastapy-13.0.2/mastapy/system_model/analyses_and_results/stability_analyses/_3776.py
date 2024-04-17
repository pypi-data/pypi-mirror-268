"""AGMAGleasonConicalGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3804
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AGMAGleasonConicalGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3783,
        _3788,
        _3836,
        _3873,
        _3882,
        _3885,
        _3903,
        _3832,
        _3871,
        _3771,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetStabilityAnalysis")


class AGMAGleasonConicalGearSetStabilityAnalysis(_3804.ConicalGearSetStabilityAnalysis):
    """AGMAGleasonConicalGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
            parent: "AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3804.ConicalGearSetStabilityAnalysis":
            return self._parent._cast(_3804.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3832.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(_3832.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3871.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3771.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3783.BevelDifferentialGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3788.BevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.BevelGearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3836.HypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(_3836.HypoidGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3873.SpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.SpiralBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3882.StraightBevelDiffGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3885.StraightBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.StraightBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "_3903.ZerolBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3903,
            )

            return self._parent._cast(_3903.ZerolBevelGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2521.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

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
    ) -> "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetStabilityAnalysis(self)
