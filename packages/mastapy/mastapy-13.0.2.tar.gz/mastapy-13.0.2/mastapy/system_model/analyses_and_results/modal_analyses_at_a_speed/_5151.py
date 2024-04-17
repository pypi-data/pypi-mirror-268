"""ConceptCouplingConnectionModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5162
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ConceptCouplingConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2351
    from mastapy.system_model.analyses_and_results.static_loads import _6847
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5190,
        _5160,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionModalAnalysisAtASpeed")


class ConceptCouplingConnectionModalAnalysisAtASpeed(
    _5162.CouplingConnectionModalAnalysisAtASpeed
):
    """ConceptCouplingConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionModalAnalysisAtASpeed"
    )

    class _Cast_ConceptCouplingConnectionModalAnalysisAtASpeed:
        """Special nested class for casting ConceptCouplingConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
            parent: "ConceptCouplingConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5162.CouplingConnectionModalAnalysisAtASpeed":
            return self._parent._cast(_5162.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5190.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(
                _5190.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5160.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
        ) -> "ConceptCouplingConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed",
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
        instance_to_wrap: "ConceptCouplingConnectionModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2351.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6847.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionModalAnalysisAtASpeed._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed":
        return self._Cast_ConceptCouplingConnectionModalAnalysisAtASpeed(self)
