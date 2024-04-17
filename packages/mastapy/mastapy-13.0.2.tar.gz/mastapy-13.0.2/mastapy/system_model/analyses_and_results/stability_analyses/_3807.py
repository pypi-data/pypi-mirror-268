"""ConnectorStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3850
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConnectorStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3779,
        _3851,
        _3868,
        _3796,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorStabilityAnalysis",)


Self = TypeVar("Self", bound="ConnectorStabilityAnalysis")


class ConnectorStabilityAnalysis(_3850.MountableComponentStabilityAnalysis):
    """ConnectorStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorStabilityAnalysis")

    class _Cast_ConnectorStabilityAnalysis:
        """Special nested class for casting ConnectorStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
            parent: "ConnectorStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3850.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3850.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3796.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3779.BearingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3779,
            )

            return self._parent._cast(_3779.BearingStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3851.OilSealStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.OilSealStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3868.ShaftHubConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(_3868.ShaftHubConnectionStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "ConnectorStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.Connector":
        """mastapy.system_model.part_model.Connector

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
    ) -> "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis":
        return self._Cast_ConnectorStabilityAnalysis(self)
