"""CVTBeltConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CVTBeltConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2280
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3838,
        _3806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionStabilityAnalysis")


class CVTBeltConnectionStabilityAnalysis(_3780.BeltConnectionStabilityAnalysis):
    """CVTBeltConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionStabilityAnalysis")

    class _Cast_CVTBeltConnectionStabilityAnalysis:
        """Special nested class for casting CVTBeltConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
            parent: "CVTBeltConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_stability_analysis(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
        ) -> "_3780.BeltConnectionStabilityAnalysis":
            return self._parent._cast(_3780.BeltConnectionStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
        ) -> "_3838.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(
                _3838.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
        ) -> "_3806.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_stability_analysis(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
        ) -> "CVTBeltConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2280.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionStabilityAnalysis._Cast_CVTBeltConnectionStabilityAnalysis":
        return self._Cast_CVTBeltConnectionStabilityAnalysis(self)
