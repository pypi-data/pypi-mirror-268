"""CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
        "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2342
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7381,
        _7281,
        _7316,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"
)


class CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection(
    _7305.CoaxialConnectionAdvancedSystemDeflection
):
    """CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
            parent: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coaxial_connection_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> "_7305.CoaxialConnectionAdvancedSystemDeflection":
            return self._parent._cast(_7305.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> "_7381.ShaftToMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(
                _7381.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> (
            "_7281.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7281,
            )

            return self._parent._cast(
                _7281.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> "_7316.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2342.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

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
    ) -> "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection":
        return self._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection(
            self
        )
