"""ConnectorModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5203
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ConnectorModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5133,
        _5204,
        _5221,
        _5150,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConnectorModalAnalysisAtASpeed")


class ConnectorModalAnalysisAtASpeed(_5203.MountableComponentModalAnalysisAtASpeed):
    """ConnectorModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorModalAnalysisAtASpeed")

    class _Cast_ConnectorModalAnalysisAtASpeed:
        """Special nested class for casting ConnectorModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
            parent: "ConnectorModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_5203.MountableComponentModalAnalysisAtASpeed":
            return self._parent._cast(_5203.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_5150.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_5133.BearingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5133,
            )

            return self._parent._cast(_5133.BearingModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_5204.OilSealModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5204,
            )

            return self._parent._cast(_5204.OilSealModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "_5221.ShaftHubConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(_5221.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
        ) -> "ConnectorModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorModalAnalysisAtASpeed._Cast_ConnectorModalAnalysisAtASpeed":
        return self._Cast_ConnectorModalAnalysisAtASpeed(self)
