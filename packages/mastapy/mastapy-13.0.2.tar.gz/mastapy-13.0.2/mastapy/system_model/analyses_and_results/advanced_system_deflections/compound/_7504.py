"""RingPinsToDiscConnectionCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7479,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2348
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7374,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionCompoundAdvancedSystemDeflection")


class RingPinsToDiscConnectionCompoundAdvancedSystemDeflection(
    _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
):
    """RingPinsToDiscConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting RingPinsToDiscConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
            parent: "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7449.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_advanced_system_deflection(
            self: "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
        ) -> "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2348.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2348.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7374.RingPinsToDiscConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.RingPinsToDiscConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7374.RingPinsToDiscConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.RingPinsToDiscConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection._Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_RingPinsToDiscConnectionCompoundAdvancedSystemDeflection(self)
