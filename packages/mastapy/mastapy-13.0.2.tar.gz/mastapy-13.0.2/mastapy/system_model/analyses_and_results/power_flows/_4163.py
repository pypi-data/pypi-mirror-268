"""TorqueConverterConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4077
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "TorqueConverterConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2359
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.power_flows import _4108, _4075
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionPowerFlow",)


Self = TypeVar("Self", bound="TorqueConverterConnectionPowerFlow")


class TorqueConverterConnectionPowerFlow(_4077.CouplingConnectionPowerFlow):
    """TorqueConverterConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterConnectionPowerFlow")

    class _Cast_TorqueConverterConnectionPowerFlow:
        """Special nested class for casting TorqueConverterConnectionPowerFlow to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
            parent: "TorqueConverterConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_connection_power_flow(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ) -> "_4077.CouplingConnectionPowerFlow":
            return self._parent._cast(_4077.CouplingConnectionPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ) -> "_4108.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ) -> "_4075.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_connection_power_flow(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ) -> "TorqueConverterConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
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
        self: Self, instance_to_wrap: "TorqueConverterConnectionPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2359.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6981.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow":
        return self._Cast_TorqueConverterConnectionPowerFlow(self)
