"""VirtualComponentCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6631
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "VirtualComponentCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6629,
        _6630,
        _6640,
        _6641,
        _6675,
        _6576,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCriticalSpeedAnalysis")


class VirtualComponentCriticalSpeedAnalysis(
    _6631.MountableComponentCriticalSpeedAnalysis
):
    """VirtualComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCriticalSpeedAnalysis"
    )

    class _Cast_VirtualComponentCriticalSpeedAnalysis:
        """Special nested class for casting VirtualComponentCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
            parent: "VirtualComponentCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6631.MountableComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6631.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6576.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6629.MassDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6630.MeasurementComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6640.PointLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(_6640.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6641.PowerLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(_6641.PowerLoadCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6675.UnbalancedMassCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6675,
            )

            return self._parent._cast(_6675.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "VirtualComponentCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2486.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis":
        return self._Cast_VirtualComponentCriticalSpeedAnalysis(self)
