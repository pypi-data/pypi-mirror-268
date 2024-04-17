"""CycloidalDiscCentralBearingConnectionCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2883
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2744
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2958,
        _2862,
        _2894,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundSystemDeflection"
)


class CycloidalDiscCentralBearingConnectionCompoundSystemDeflection(
    _2883.CoaxialConnectionCompoundSystemDeflection
):
    """CycloidalDiscCentralBearingConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
            parent: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
        ) -> "_2883.CoaxialConnectionCompoundSystemDeflection":
            return self._parent._cast(_2883.CoaxialConnectionCompoundSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
        ) -> "_2958.ShaftToMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2958,
            )

            return self._parent._cast(
                _2958.ShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
        ) -> (
            "_2862.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2862,
            )

            return self._parent._cast(
                _2862.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
        ) -> "_2894.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2744.CycloidalDiscCentralBearingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscCentralBearingConnectionSystemDeflection]

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
    ) -> "List[_2744.CycloidalDiscCentralBearingConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscCentralBearingConnectionSystemDeflection]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection(
            self
        )
