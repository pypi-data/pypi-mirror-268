"""CVTBeltConnectionDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CVTBeltConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2280
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352, _6320
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionDynamicAnalysis")


class CVTBeltConnectionDynamicAnalysis(_6294.BeltConnectionDynamicAnalysis):
    """CVTBeltConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionDynamicAnalysis")

    class _Cast_CVTBeltConnectionDynamicAnalysis:
        """Special nested class for casting CVTBeltConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
            parent: "CVTBeltConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_dynamic_analysis(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
        ) -> "_6294.BeltConnectionDynamicAnalysis":
            return self._parent._cast(_6294.BeltConnectionDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
        ) -> "_6352.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(
                _6352.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
        ) -> "_6320.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_dynamic_analysis(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
        ) -> "CVTBeltConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTBeltConnectionDynamicAnalysis.TYPE"):
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
    ) -> "CVTBeltConnectionDynamicAnalysis._Cast_CVTBeltConnectionDynamicAnalysis":
        return self._Cast_CVTBeltConnectionDynamicAnalysis(self)
