"""CoaxialConnectionCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CoaxialConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2276
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6460,
        _6419,
        _6451,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundDynamicAnalysis")


class CoaxialConnectionCompoundDynamicAnalysis(
    _6513.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
):
    """CoaxialConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundDynamicAnalysis"
    )

    class _Cast_CoaxialConnectionCompoundDynamicAnalysis:
        """Special nested class for casting CoaxialConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis",
            parent: "CoaxialConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis",
        ) -> "_6513.ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent._cast(
                _6513.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis",
        ) -> "_6419.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6419,
            )

            return self._parent._cast(
                _6419.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis",
        ) -> "_6451.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
            self: "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis",
        ) -> "_6460.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6460,
            )

            return self._parent._cast(
                _6460.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def coaxial_connection_compound_dynamic_analysis(
            self: "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis",
        ) -> "CoaxialConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CoaxialConnectionCompoundDynamicAnalysis.TYPE"
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
    ) -> "List[_6309.CoaxialConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CoaxialConnectionDynamicAnalysis]

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
    ) -> "List[_6309.CoaxialConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CoaxialConnectionDynamicAnalysis]

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
    ) -> "CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis":
        return self._Cast_CoaxialConnectionCompoundDynamicAnalysis(self)
