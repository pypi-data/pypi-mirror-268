"""TorqueConverterConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2737
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "TorqueConverterConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2359
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.power_flows import _4163
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2775,
        _2735,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterConnectionSystemDeflection")


class TorqueConverterConnectionSystemDeflection(
    _2737.CouplingConnectionSystemDeflection
):
    """TorqueConverterConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionSystemDeflection"
    )

    class _Cast_TorqueConverterConnectionSystemDeflection:
        """Special nested class for casting TorqueConverterConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
            parent: "TorqueConverterConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_system_deflection(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
        ) -> "_2737.CouplingConnectionSystemDeflection":
            return self._parent._cast(_2737.CouplingConnectionSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
        ) -> "_2775.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
        ) -> "_2735.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_connection_system_deflection(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
        ) -> "TorqueConverterConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "TorqueConverterConnectionSystemDeflection.TYPE"
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
    def power_flow_results(self: Self) -> "_4163.TorqueConverterConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.TorqueConverterConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterConnectionSystemDeflection._Cast_TorqueConverterConnectionSystemDeflection":
        return self._Cast_TorqueConverterConnectionSystemDeflection(self)
