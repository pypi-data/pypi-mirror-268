"""ShaftToMountableComponentConnectionCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2862
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ShaftToMountableComponentConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2813
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2883,
        _2903,
        _2943,
        _2894,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundSystemDeflection"
)


class ShaftToMountableComponentConnectionCompoundSystemDeflection(
    _2862.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
):
    """ShaftToMountableComponentConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
            parent: "ShaftToMountableComponentConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
        ) -> (
            "_2862.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ):
            return self._parent._cast(
                _2862.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2894.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2883.CoaxialConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(_2883.CoaxialConnectionCompoundSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2903.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2903,
            )

            return self._parent._cast(
                _2903.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
            )

        @property
        def planetary_connection_compound_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2943.PlanetaryConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(_2943.PlanetaryConnectionCompoundSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
        ) -> "ShaftToMountableComponentConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2813.ShaftToMountableComponentConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2813.ShaftToMountableComponentConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection":
        return self._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection(
            self
        )
