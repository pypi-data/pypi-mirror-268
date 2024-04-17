"""AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5387
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5561,
        _5581,
        _5583,
        _5620,
        _5634,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)


class AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
    _5572.ConnectionCompoundMultibodyDynamicsAnalysis
):
    """AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5572.ConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5572.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5561.CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(
                _5561.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5581.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(
                _5581.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5583.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(
                _5583.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5620.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(
                _5620.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5634.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(
                _5634.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5387.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5387.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )
