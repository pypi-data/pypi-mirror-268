"""SynchroniserPartCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6590
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SynchroniserPartCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2613
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6668,
        _6670,
        _6631,
        _6576,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCriticalSpeedAnalysis")


class SynchroniserPartCriticalSpeedAnalysis(_6590.CouplingHalfCriticalSpeedAnalysis):
    """SynchroniserPartCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCriticalSpeedAnalysis"
    )

    class _Cast_SynchroniserPartCriticalSpeedAnalysis:
        """Special nested class for casting SynchroniserPartCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
            parent: "SynchroniserPartCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_6590.CouplingHalfCriticalSpeedAnalysis":
            return self._parent._cast(_6590.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_6668.SynchroniserHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "_6670.SynchroniserSleeveCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "SynchroniserPartCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2613.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis":
        return self._Cast_SynchroniserPartCriticalSpeedAnalysis(self)
