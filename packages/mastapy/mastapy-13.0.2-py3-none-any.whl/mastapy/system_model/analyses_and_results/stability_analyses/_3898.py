"""VirtualComponentStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3850
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "VirtualComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3848,
        _3849,
        _3859,
        _3860,
        _3897,
        _3796,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentStabilityAnalysis")


class VirtualComponentStabilityAnalysis(_3850.MountableComponentStabilityAnalysis):
    """VirtualComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentStabilityAnalysis")

    class _Cast_VirtualComponentStabilityAnalysis:
        """Special nested class for casting VirtualComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
            parent: "VirtualComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3850.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3850.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3796.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3848.MassDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3849.MeasurementComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.MeasurementComponentStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3859.PointLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(_3859.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3860.PowerLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.PowerLoadStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3897.UnbalancedMassStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3897,
            )

            return self._parent._cast(_3897.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "VirtualComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentStabilityAnalysis.TYPE"
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
    ) -> "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis":
        return self._Cast_VirtualComponentStabilityAnalysis(self)
