"""CoaxialConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CoaxialConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2276
    from mastapy.system_model.analyses_and_results.static_loads import _6845
    from mastapy.system_model.analyses_and_results.power_flows import _4064
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2744,
        _2696,
        _2735,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionSystemDeflection",)


Self = TypeVar("Self", bound="CoaxialConnectionSystemDeflection")


class CoaxialConnectionSystemDeflection(
    _2813.ShaftToMountableComponentConnectionSystemDeflection
):
    """CoaxialConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionSystemDeflection")

    class _Cast_CoaxialConnectionSystemDeflection:
        """Special nested class for casting CoaxialConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
            parent: "CoaxialConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "_2813.ShaftToMountableComponentConnectionSystemDeflection":
            return self._parent._cast(
                _2813.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "_2696.AbstractShaftToMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2696,
            )

            return self._parent._cast(
                _2696.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "_2735.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "_2744.CycloidalDiscCentralBearingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(
                _2744.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def coaxial_connection_system_deflection(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "CoaxialConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "CoaxialConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2276.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6845.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4064.CoaxialConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CoaxialConnectionPowerFlow

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
    ) -> "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection":
        return self._Cast_CoaxialConnectionSystemDeflection(self)
