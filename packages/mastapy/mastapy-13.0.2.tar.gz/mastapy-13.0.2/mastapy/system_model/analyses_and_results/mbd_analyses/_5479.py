"""PlanetaryConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5495
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PlanetaryConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2294
    from mastapy.system_model.analyses_and_results.static_loads import _6941
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5387, _5422
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionMultibodyDynamicsAnalysis")


class PlanetaryConnectionMultibodyDynamicsAnalysis(
    _5495.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """PlanetaryConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_PlanetaryConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting PlanetaryConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
            parent: "PlanetaryConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_5495.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5495.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> (
            "_5387.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(
                _5387.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_5422.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_7550.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "PlanetaryConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "PlanetaryConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2294.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6941.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

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
    ) -> "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis":
        return self._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis(self)
