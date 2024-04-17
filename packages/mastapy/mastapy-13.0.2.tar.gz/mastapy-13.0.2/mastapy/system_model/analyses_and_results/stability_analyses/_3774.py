"""AbstractShaftToMountableComponentConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
        "AbstractShaftToMountableComponentConnectionStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2272
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3795,
        _3816,
        _3817,
        _3856,
        _3870,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionStabilityAnalysis"
)


class AbstractShaftToMountableComponentConnectionStabilityAnalysis(
    _3806.ConnectionStabilityAnalysis
):
    """AbstractShaftToMountableComponentConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3806.ConnectionStabilityAnalysis":
            return self._parent._cast(_3806.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3795.CoaxialConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.CoaxialConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3816.CycloidalDiscCentralBearingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(
                _3816.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3817.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(
                _3817.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
            )

        @property
        def planetary_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3856.PlanetaryConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(_3856.PlanetaryConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3870.ShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3870,
            )

            return self._parent._cast(
                _3870.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2272.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

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
    ) -> "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis(
            self
        )
