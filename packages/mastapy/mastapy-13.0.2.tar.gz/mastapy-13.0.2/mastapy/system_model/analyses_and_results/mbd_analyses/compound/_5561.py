"""CoaxialConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5634
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2276
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5411
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5581,
        _5540,
        _5572,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundMultibodyDynamicsAnalysis")


class CoaxialConnectionCompoundMultibodyDynamicsAnalysis(
    _5634.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
):
    """CoaxialConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CoaxialConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5634.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ):
            return self._parent._cast(
                _5634.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5540.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5540,
            )

            return self._parent._cast(
                _5540.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5572.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(_5572.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5581.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(
                _5581.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2276.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2276.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

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
    ) -> "List[_5411.CoaxialConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CoaxialConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5411.CoaxialConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CoaxialConnectionMultibodyDynamicsAnalysis]

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
    ) -> "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis(self)
