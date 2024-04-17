"""RollingRingConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5602
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5488
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5572
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="RollingRingConnectionCompoundMultibodyDynamicsAnalysis")


class RollingRingConnectionCompoundMultibodyDynamicsAnalysis(
    _5602.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
):
    """RollingRingConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting RollingRingConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "RollingRingConnectionCompoundMultibodyDynamicsAnalysis._Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "RollingRingConnectionCompoundMultibodyDynamicsAnalysis._Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5602.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5602.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "RollingRingConnectionCompoundMultibodyDynamicsAnalysis._Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5572.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(_5572.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "RollingRingConnectionCompoundMultibodyDynamicsAnalysis._Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingConnectionCompoundMultibodyDynamicsAnalysis._Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionCompoundMultibodyDynamicsAnalysis._Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(
            self: "RollingRingConnectionCompoundMultibodyDynamicsAnalysis._Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "RollingRingConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionCompoundMultibodyDynamicsAnalysis._Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "RollingRingConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
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
    ) -> "List[_5488.RollingRingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.RollingRingConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[RollingRingConnectionCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RollingRingConnectionCompoundMultibodyDynamicsAnalysis]

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
    ) -> "List[_5488.RollingRingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.RollingRingConnectionMultibodyDynamicsAnalysis]

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
    ) -> "RollingRingConnectionCompoundMultibodyDynamicsAnalysis._Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_RollingRingConnectionCompoundMultibodyDynamicsAnalysis(self)
