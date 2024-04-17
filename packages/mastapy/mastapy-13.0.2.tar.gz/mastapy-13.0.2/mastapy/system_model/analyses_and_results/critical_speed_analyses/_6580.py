"""ConceptGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConceptGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.static_loads import _6850
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6631,
        _6576,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConceptGearCriticalSpeedAnalysis")


class ConceptGearCriticalSpeedAnalysis(_6612.GearCriticalSpeedAnalysis):
    """ConceptGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearCriticalSpeedAnalysis")

    class _Cast_ConceptGearCriticalSpeedAnalysis:
        """Special nested class for casting ConceptGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
            parent: "ConceptGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_critical_speed_analysis(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
        ) -> "_6612.GearCriticalSpeedAnalysis":
            return self._parent._cast(_6612.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
        ) -> "ConceptGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearCriticalSpeedAnalysis.TYPE"):
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
    def component_load_case(self: Self) -> "_6850.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis":
        return self._Cast_ConceptGearCriticalSpeedAnalysis(self)
