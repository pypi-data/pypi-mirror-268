"""ShaftToMountableComponentConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2696
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ShaftToMountableComponentConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2302
    from mastapy.system_model.analyses_and_results.power_flows import _4142
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2722,
        _2744,
        _2797,
        _2735,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionSystemDeflection",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionSystemDeflection")


class ShaftToMountableComponentConnectionSystemDeflection(
    _2696.AbstractShaftToMountableComponentConnectionSystemDeflection
):
    """ShaftToMountableComponentConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionSystemDeflection"
    )

    class _Cast_ShaftToMountableComponentConnectionSystemDeflection:
        """Special nested class for casting ShaftToMountableComponentConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
            parent: "ShaftToMountableComponentConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2696.AbstractShaftToMountableComponentConnectionSystemDeflection":
            return self._parent._cast(
                _2696.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2735.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2722.CoaxialConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.CoaxialConnectionSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2744.CycloidalDiscCentralBearingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(
                _2744.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def planetary_connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2797.PlanetaryConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.PlanetaryConnectionSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "ShaftToMountableComponentConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
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
        self: Self,
        instance_to_wrap: "ShaftToMountableComponentConnectionSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2302.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4142.ShaftToMountableComponentConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ShaftToMountableComponentConnectionPowerFlow

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
    ) -> "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection":
        return self._Cast_ShaftToMountableComponentConnectionSystemDeflection(self)
