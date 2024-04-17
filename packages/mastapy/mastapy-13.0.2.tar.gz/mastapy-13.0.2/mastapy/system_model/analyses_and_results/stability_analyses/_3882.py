"""StraightBevelDiffGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StraightBevelDiffGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.static_loads import _6970
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3883,
        _3881,
        _3776,
        _3804,
        _3832,
        _3871,
        _3771,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetStabilityAnalysis")


class StraightBevelDiffGearSetStabilityAnalysis(_3788.BevelGearSetStabilityAnalysis):
    """StraightBevelDiffGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetStabilityAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetStabilityAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
            parent: "StraightBevelDiffGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_3788.BevelGearSetStabilityAnalysis":
            return self._parent._cast(_3788.BevelGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_3776.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_3804.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_3832.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(_3832.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_3871.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_3771.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "StraightBevelDiffGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearSetStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2553.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6970.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_stability_analysis(
        self: Self,
    ) -> "List[_3883.StraightBevelDiffGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3881.StraightBevelDiffGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis":
        return self._Cast_StraightBevelDiffGearSetStabilityAnalysis(self)
