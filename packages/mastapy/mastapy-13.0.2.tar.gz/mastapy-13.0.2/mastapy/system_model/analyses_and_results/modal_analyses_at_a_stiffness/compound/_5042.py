"""CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _4999,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2345
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4911,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5031,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
)


class CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness(
    _4999.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
):
    """CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
            parent: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_4999.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4999.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5031.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(_5031.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2345.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(
        self: Self,
    ) -> "_2345.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

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
    ) -> "List[_4911.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4911.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness]

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness(
            self
        )
