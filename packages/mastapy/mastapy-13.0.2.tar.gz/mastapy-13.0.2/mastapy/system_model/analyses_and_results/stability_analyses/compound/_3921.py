"""BevelGearCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3909
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BevelGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3789
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3916,
        _3919,
        _3920,
        _4004,
        _4010,
        _4013,
        _4016,
        _4017,
        _4031,
        _3937,
        _3963,
        _3982,
        _3930,
        _3984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelGearCompoundStabilityAnalysis")


class BevelGearCompoundStabilityAnalysis(
    _3909.AGMAGleasonConicalGearCompoundStabilityAnalysis
):
    """BevelGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearCompoundStabilityAnalysis")

    class _Cast_BevelGearCompoundStabilityAnalysis:
        """Special nested class for casting BevelGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
            parent: "BevelGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3909.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            return self._parent._cast(
                _3909.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3937.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3963.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(_3963.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3982.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3930.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3984.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3916.BevelDifferentialGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3916,
            )

            return self._parent._cast(
                _3916.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3919.BevelDifferentialPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(
                _3919.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3920.BevelDifferentialSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(
                _3920.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4004.SpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(_4004.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4010.StraightBevelDiffGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(
                _4010.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4013.StraightBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(_4013.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4016.StraightBevelPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(
                _4016.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4017.StraightBevelSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(
                _4017.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4031.ZerolBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4031,
            )

            return self._parent._cast(_4031.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "BevelGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3789.BevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3789.BevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis":
        return self._Cast_BevelGearCompoundStabilityAnalysis(self)
