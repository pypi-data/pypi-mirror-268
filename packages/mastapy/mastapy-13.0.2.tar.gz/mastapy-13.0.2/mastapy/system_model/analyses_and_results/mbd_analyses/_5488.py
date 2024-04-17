"""RollingRingConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5457
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "RollingRingConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.static_loads import _6955
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5422
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="RollingRingConnectionMultibodyDynamicsAnalysis")


class RollingRingConnectionMultibodyDynamicsAnalysis(
    _5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """RollingRingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_RollingRingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting RollingRingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
            parent: "RollingRingConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5422.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7550.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "RollingRingConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "RollingRingConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force_on_ring_a(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceOnRingA

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def normal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def separation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Separation

        if temp is None:
            return 0.0

        return temp

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
    def connection_load_case(self: Self) -> "_6955.RollingRingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[RollingRingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.RollingRingConnectionMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis":
        return self._Cast_RollingRingConnectionMultibodyDynamicsAnalysis(self)
