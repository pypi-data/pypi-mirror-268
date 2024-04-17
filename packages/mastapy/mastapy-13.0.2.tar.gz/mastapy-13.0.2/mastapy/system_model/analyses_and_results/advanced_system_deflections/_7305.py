"""CoaxialConnectionAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7381
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CoaxialConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2276
    from mastapy.system_model.analyses_and_results.static_loads import _6845
    from mastapy.system_model.analyses_and_results.system_deflections import _2722
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7327,
        _7281,
        _7316,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CoaxialConnectionAdvancedSystemDeflection")


class CoaxialConnectionAdvancedSystemDeflection(
    _7381.ShaftToMountableComponentConnectionAdvancedSystemDeflection
):
    """CoaxialConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionAdvancedSystemDeflection"
    )

    class _Cast_CoaxialConnectionAdvancedSystemDeflection:
        """Special nested class for casting CoaxialConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
            parent: "CoaxialConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ) -> "_7381.ShaftToMountableComponentConnectionAdvancedSystemDeflection":
            return self._parent._cast(
                _7381.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
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
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ) -> "_7316.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ) -> "_7327.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(
                _7327.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
            )

        @property
        def coaxial_connection_advanced_system_deflection(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ) -> "CoaxialConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CoaxialConnectionAdvancedSystemDeflection.TYPE"
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
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2722.CoaxialConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection":
        return self._Cast_CoaxialConnectionAdvancedSystemDeflection(self)
