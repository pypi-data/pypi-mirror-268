"""RollingRingConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4650
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "RollingRingConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.static_loads import _6955
    from mastapy.system_model.analyses_and_results.system_deflections import _2806
    from mastapy.system_model.analyses_and_results.modal_analyses import _4615
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionModalAnalysis",)


Self = TypeVar("Self", bound="RollingRingConnectionModalAnalysis")


class RollingRingConnectionModalAnalysis(
    _4650.InterMountableComponentConnectionModalAnalysis
):
    """RollingRingConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingConnectionModalAnalysis")

    class _Cast_RollingRingConnectionModalAnalysis:
        """Special nested class for casting RollingRingConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis",
            parent: "RollingRingConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis",
        ) -> "_4650.InterMountableComponentConnectionModalAnalysis":
            return self._parent._cast(
                _4650.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis",
        ) -> "_4615.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_modal_analysis(
            self: "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis",
        ) -> "RollingRingConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingConnectionModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2299.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6955.RollingRingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2806.RollingRingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RollingRingConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.RollingRingConnectionModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionModalAnalysis._Cast_RollingRingConnectionModalAnalysis":
        return self._Cast_RollingRingConnectionModalAnalysis(self)
