"""SpringDamperConnectionCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5293,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SpringDamperConnectionCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2357
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5228,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5320,
        _5290,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpringDamperConnectionCompoundModalAnalysisAtASpeed")


class SpringDamperConnectionCompoundModalAnalysisAtASpeed(
    _5293.CouplingConnectionCompoundModalAnalysisAtASpeed
):
    """SpringDamperConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SpringDamperConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
            parent: "SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5293.CouplingConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5293.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5320.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5290.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(_5290.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ) -> "SpringDamperConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SpringDamperConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2357.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2357.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

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
    ) -> "List[_5228.SpringDamperConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpringDamperConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5228.SpringDamperConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpringDamperConnectionModalAnalysisAtASpeed]

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
    ) -> "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed(self)
