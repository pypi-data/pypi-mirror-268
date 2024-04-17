"""ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6686,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6651
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6707,
        _6727,
        _6766,
        _6718,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
)


class ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis(
    _6686.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
            parent: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6686.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6686.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6718.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(_6718.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6707.CoaxialConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(
                _6707.CoaxialConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6727.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(
                _6727.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6766.PlanetaryConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(
                _6766.PlanetaryConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6651.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6651.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]

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
    ) -> "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
        return (
            self._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis(
                self
            )
        )
