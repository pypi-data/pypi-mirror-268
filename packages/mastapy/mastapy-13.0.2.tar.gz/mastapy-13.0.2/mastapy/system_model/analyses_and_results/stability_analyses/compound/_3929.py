"""CoaxialConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CoaxialConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2276
    from mastapy.system_model.analyses_and_results.stability_analyses import _3795
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3949,
        _3908,
        _3940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundStabilityAnalysis")


class CoaxialConnectionCompoundStabilityAnalysis(
    _4002.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
):
    """CoaxialConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundStabilityAnalysis"
    )

    class _Cast_CoaxialConnectionCompoundStabilityAnalysis:
        """Special nested class for casting CoaxialConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
            parent: "CoaxialConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_4002.ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent._cast(
                _4002.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> (
            "_3908.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3908,
            )

            return self._parent._cast(
                _3908.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_3940.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_3949.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(
                _3949.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "CoaxialConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CoaxialConnectionCompoundStabilityAnalysis.TYPE"
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
    ) -> "List[_3795.CoaxialConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CoaxialConnectionStabilityAnalysis]

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
    ) -> "List[_3795.CoaxialConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CoaxialConnectionStabilityAnalysis]

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
    ) -> "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis":
        return self._Cast_CoaxialConnectionCompoundStabilityAnalysis(self)
