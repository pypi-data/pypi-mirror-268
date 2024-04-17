"""KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6749,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6623
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6715,
        _6741,
        _6760,
        _6708,
        _6762,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis(
    _6749.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6749.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6749.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6715.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(_6715.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6741.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(_6741.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6760.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(
                _6760.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6623.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis]

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
    ) -> "List[_6623.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis(
                self
            )
        )
