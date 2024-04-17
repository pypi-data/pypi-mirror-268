"""RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6748,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2348
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6644
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6718,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis")


class RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis(
    _6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis"
    )

    class _Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
            parent: "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6718.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(_6718.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_critical_speed_analysis(
            self: "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
        ) -> "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2348.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2348.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

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
    ) -> "List[_6644.RingPinsToDiscConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.RingPinsToDiscConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6644.RingPinsToDiscConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.RingPinsToDiscConnectionCriticalSpeedAnalysis]

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
    ) -> "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis":
        return self._Cast_RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis(self)
