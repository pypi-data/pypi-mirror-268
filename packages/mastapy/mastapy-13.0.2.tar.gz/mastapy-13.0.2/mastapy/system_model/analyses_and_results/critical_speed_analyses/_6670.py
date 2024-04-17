"""SynchroniserSleeveCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6669
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SynchroniserSleeveCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2614
    from mastapy.system_model.analyses_and_results.static_loads import _6979
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6590,
        _6631,
        _6576,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveCriticalSpeedAnalysis")


class SynchroniserSleeveCriticalSpeedAnalysis(
    _6669.SynchroniserPartCriticalSpeedAnalysis
):
    """SynchroniserSleeveCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveCriticalSpeedAnalysis"
    )

    class _Cast_SynchroniserSleeveCriticalSpeedAnalysis:
        """Special nested class for casting SynchroniserSleeveCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
            parent: "SynchroniserSleeveCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "_6669.SynchroniserPartCriticalSpeedAnalysis":
            return self._parent._cast(_6669.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "_6590.CouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6590,
            )

            return self._parent._cast(_6590.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
        ) -> "SynchroniserSleeveCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2614.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6979.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

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
    ) -> "SynchroniserSleeveCriticalSpeedAnalysis._Cast_SynchroniserSleeveCriticalSpeedAnalysis":
        return self._Cast_SynchroniserSleeveCriticalSpeedAnalysis(self)
