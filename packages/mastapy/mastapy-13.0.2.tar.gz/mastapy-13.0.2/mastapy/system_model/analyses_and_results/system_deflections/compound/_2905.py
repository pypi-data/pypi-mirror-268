"""CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2862
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
        "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2345
    from mastapy.system_model.analyses_and_results.system_deflections import _2745
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2894,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection"
)


class CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection(
    _2862.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
):
    """CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
            parent: "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
        ) -> (
            "_2862.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ):
            return self._parent._cast(
                _2862.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
        ) -> "_2894.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_system_deflection(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
        ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2345.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(
        self: Self,
    ) -> "_2345.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

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
    ) -> "List[_2745.CycloidalDiscPlanetaryBearingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscPlanetaryBearingConnectionSystemDeflection]

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
    ) -> "List[_2745.CycloidalDiscPlanetaryBearingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscPlanetaryBearingConnectionSystemDeflection]

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection":
        return (
            self._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection(
                self
            )
        )
