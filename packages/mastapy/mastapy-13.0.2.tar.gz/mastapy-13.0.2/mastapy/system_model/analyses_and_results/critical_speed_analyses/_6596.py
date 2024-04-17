"""CVTPulleyCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6642
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CVTPulleyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2595
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6590,
        _6631,
        _6576,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyCriticalSpeedAnalysis")


class CVTPulleyCriticalSpeedAnalysis(_6642.PulleyCriticalSpeedAnalysis):
    """CVTPulleyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyCriticalSpeedAnalysis")

    class _Cast_CVTPulleyCriticalSpeedAnalysis:
        """Special nested class for casting CVTPulleyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
            parent: "CVTPulleyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6642.PulleyCriticalSpeedAnalysis":
            return self._parent._cast(_6642.PulleyCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6590.CouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6590,
            )

            return self._parent._cast(_6590.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "CVTPulleyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2595.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

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
    ) -> "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis":
        return self._Cast_CVTPulleyCriticalSpeedAnalysis(self)
