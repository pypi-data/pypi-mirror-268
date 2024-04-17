"""CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3774
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2345
    from mastapy.system_model.analyses_and_results.static_loads import _6869
    from mastapy.system_model.analyses_and_results.stability_analyses import _3806
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis")


class CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis(
    _3774.AbstractShaftToMountableComponentConnectionStabilityAnalysis
):
    """CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
            parent: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
        ) -> "_3774.AbstractShaftToMountableComponentConnectionStabilityAnalysis":
            return self._parent._cast(
                _3774.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
        ) -> "_3806.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
        ) -> "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(
        self: Self,
    ) -> "_6869.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis(self)
