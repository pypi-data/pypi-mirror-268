"""StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6788,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6665
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6699,
        _6687,
        _6715,
        _6741,
        _6760,
        _6708,
        _6762,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundCriticalSpeedAnalysis")


class StraightBevelPlanetGearCompoundCriticalSpeedAnalysis(
    _6788.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
):
    """StraightBevelPlanetGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelPlanetGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
            parent: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_6788.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6788.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_6699.BevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(
                _6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_6715.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(_6715.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_6741.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(_6741.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_6760.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(
                _6760.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6665.StraightBevelPlanetGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelPlanetGearCriticalSpeedAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6665.StraightBevelPlanetGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelPlanetGearCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
        return self._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis(self)
