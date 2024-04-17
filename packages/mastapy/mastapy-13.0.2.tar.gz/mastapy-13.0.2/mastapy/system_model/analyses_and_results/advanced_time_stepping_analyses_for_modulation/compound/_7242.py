"""RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7214,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7113,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7184,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self",
    bound="RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7214.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = (
        _ROLLING_RING_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7214.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7214.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7184.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7184,
            )

            return self._parent._cast(
                _7184.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    ) -> "List[_7113.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7113.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
