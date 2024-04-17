"""BeltConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5602
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "BeltConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2275
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5395
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5577,
        _5572,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BeltConnectionCompoundMultibodyDynamicsAnalysis")


class BeltConnectionCompoundMultibodyDynamicsAnalysis(
    _5602.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
):
    """BeltConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BeltConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "BeltConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "BeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5602.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5602.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "BeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5572.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(_5572.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(
            self: "BeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5577.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5577,
            )

            return self._parent._cast(
                _5577.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_compound_multibody_dynamics_analysis(
            self: "BeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "BeltConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "BeltConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2275.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2275.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

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
    ) -> "List[_5395.BeltConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BeltConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5395.BeltConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BeltConnectionMultibodyDynamicsAnalysis]

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
    ) -> "BeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BeltConnectionCompoundMultibodyDynamicsAnalysis(self)
