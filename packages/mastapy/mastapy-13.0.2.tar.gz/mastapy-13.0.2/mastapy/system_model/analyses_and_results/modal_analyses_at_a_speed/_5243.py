"""TorqueConverterConnectionModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5162
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "TorqueConverterConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2359
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5190,
        _5160,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="TorqueConverterConnectionModalAnalysisAtASpeed")


class TorqueConverterConnectionModalAnalysisAtASpeed(
    _5162.CouplingConnectionModalAnalysisAtASpeed
):
    """TorqueConverterConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionModalAnalysisAtASpeed"
    )

    class _Cast_TorqueConverterConnectionModalAnalysisAtASpeed:
        """Special nested class for casting TorqueConverterConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
            parent: "TorqueConverterConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
        ) -> "_5162.CouplingConnectionModalAnalysisAtASpeed":
            return self._parent._cast(_5162.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
        ) -> "_5190.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(
                _5190.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
        ) -> "_5160.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
        ) -> "TorqueConverterConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed",
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
        instance_to_wrap: "TorqueConverterConnectionModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2359.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6981.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

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
    ) -> "TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed":
        return self._Cast_TorqueConverterConnectionModalAnalysisAtASpeed(self)
