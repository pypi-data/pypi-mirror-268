"""BevelGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6687,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6567
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6694,
        _6697,
        _6698,
        _6782,
        _6788,
        _6791,
        _6794,
        _6795,
        _6809,
        _6715,
        _6741,
        _6760,
        _6708,
        _6762,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelGearCompoundCriticalSpeedAnalysis")


class BevelGearCompoundCriticalSpeedAnalysis(
    _6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
):
    """BevelGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_BevelGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
            parent: "BevelGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6715.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(_6715.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6741.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(_6741.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6760.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(
                _6760.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6694.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(
                _6694.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6697.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(
                _6697.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6698.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6698,
            )

            return self._parent._cast(
                _6698.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6782.SpiralBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6788.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6788,
            )

            return self._parent._cast(
                _6788.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6791.StraightBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6791,
            )

            return self._parent._cast(
                _6791.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6794.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6795.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6795,
            )

            return self._parent._cast(
                _6795.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "_6809.ZerolBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6809,
            )

            return self._parent._cast(_6809.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
        ) -> "BevelGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6567.BevelGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelGearCriticalSpeedAnalysis]

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
    ) -> "List[_6567.BevelGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelGearCriticalSpeedAnalysis]

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
    ) -> "BevelGearCompoundCriticalSpeedAnalysis._Cast_BevelGearCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelGearCompoundCriticalSpeedAnalysis(self)
