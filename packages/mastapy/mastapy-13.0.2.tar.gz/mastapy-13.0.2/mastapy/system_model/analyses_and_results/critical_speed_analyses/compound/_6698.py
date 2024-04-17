"""BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6694,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6566
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
__all__ = ("BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundCriticalSpeedAnalysis")


class BevelDifferentialSunGearCompoundCriticalSpeedAnalysis(
    _6694.BevelDifferentialGearCompoundCriticalSpeedAnalysis
):
    """BevelDifferentialSunGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
            parent: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6694.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6694.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6699.BevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(
                _6687.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6715.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(_6715.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6741.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(_6741.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6760.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(
                _6760.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6566.BevelDifferentialSunGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialSunGearCriticalSpeedAnalysis]

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
    ) -> "List[_6566.BevelDifferentialSunGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialSunGearCriticalSpeedAnalysis]

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
    ) -> "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis(self)
