"""ConceptGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6741,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConceptGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6760,
        _6708,
        _6762,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConceptGearCompoundCriticalSpeedAnalysis")


class ConceptGearCompoundCriticalSpeedAnalysis(_6741.GearCompoundCriticalSpeedAnalysis):
    """ConceptGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ConceptGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConceptGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
            parent: "ConceptGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_critical_speed_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_6741.GearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6741.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_6760.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(
                _6760.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_6708.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_6762.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
        ) -> "ConceptGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConceptGearCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2528.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

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
    ) -> "List[_6580.ConceptGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptGearCriticalSpeedAnalysis]

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
    ) -> "List[_6580.ConceptGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptGearCriticalSpeedAnalysis]

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
    ) -> "ConceptGearCompoundCriticalSpeedAnalysis._Cast_ConceptGearCompoundCriticalSpeedAnalysis":
        return self._Cast_ConceptGearCompoundCriticalSpeedAnalysis(self)
