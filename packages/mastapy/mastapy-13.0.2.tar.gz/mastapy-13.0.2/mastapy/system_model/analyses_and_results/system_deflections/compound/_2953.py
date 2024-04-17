"""RollingRingConnectionCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2925
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "RollingRingConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.system_deflections import _2806
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2894,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionCompoundSystemDeflection",)


Self = TypeVar("Self", bound="RollingRingConnectionCompoundSystemDeflection")


class RollingRingConnectionCompoundSystemDeflection(
    _2925.InterMountableComponentConnectionCompoundSystemDeflection
):
    """RollingRingConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingConnectionCompoundSystemDeflection"
    )

    class _Cast_RollingRingConnectionCompoundSystemDeflection:
        """Special nested class for casting RollingRingConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "RollingRingConnectionCompoundSystemDeflection._Cast_RollingRingConnectionCompoundSystemDeflection",
            parent: "RollingRingConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "RollingRingConnectionCompoundSystemDeflection._Cast_RollingRingConnectionCompoundSystemDeflection",
        ) -> "_2925.InterMountableComponentConnectionCompoundSystemDeflection":
            return self._parent._cast(
                _2925.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "RollingRingConnectionCompoundSystemDeflection._Cast_RollingRingConnectionCompoundSystemDeflection",
        ) -> "_2894.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "RollingRingConnectionCompoundSystemDeflection._Cast_RollingRingConnectionCompoundSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingConnectionCompoundSystemDeflection._Cast_RollingRingConnectionCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionCompoundSystemDeflection._Cast_RollingRingConnectionCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_compound_system_deflection(
            self: "RollingRingConnectionCompoundSystemDeflection._Cast_RollingRingConnectionCompoundSystemDeflection",
        ) -> "RollingRingConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionCompoundSystemDeflection._Cast_RollingRingConnectionCompoundSystemDeflection",
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
        instance_to_wrap: "RollingRingConnectionCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2299.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2806.RollingRingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingConnectionSystemDeflection]

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
    def planetaries(
        self: Self,
    ) -> "List[RollingRingConnectionCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.RollingRingConnectionCompoundSystemDeflection]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2806.RollingRingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingConnectionSystemDeflection]

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
    ) -> "RollingRingConnectionCompoundSystemDeflection._Cast_RollingRingConnectionCompoundSystemDeflection":
        return self._Cast_RollingRingConnectionCompoundSystemDeflection(self)
