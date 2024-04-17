"""CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5411
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2342
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5495,
        _5387,
        _5422,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis"
)


class CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis(
    _5411.CoaxialConnectionMultibodyDynamicsAnalysis
):
    """CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5411.CoaxialConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(_5411.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5495.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ) -> (
            "_5387.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(
                _5387.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5422.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7550.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis.TYPE",
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
    ) -> "CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
        return (
            self._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis(
                self
            )
        )
