"""CoaxialConnectionModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5223
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CoaxialConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2276
    from mastapy.system_model.analyses_and_results.static_loads import _6845
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5169,
        _5128,
        _5160,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CoaxialConnectionModalAnalysisAtASpeed")


class CoaxialConnectionModalAnalysisAtASpeed(
    _5223.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
):
    """CoaxialConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionModalAnalysisAtASpeed"
    )

    class _Cast_CoaxialConnectionModalAnalysisAtASpeed:
        """Special nested class for casting CoaxialConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
            parent: "CoaxialConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_5223.ShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent._cast(
                _5223.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_5128.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5128,
            )

            return self._parent._cast(
                _5128.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_5160.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "_5169.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5169,
            )

            return self._parent._cast(
                _5169.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def coaxial_connection_modal_analysis_at_a_speed(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
        ) -> "CoaxialConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CoaxialConnectionModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6845.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

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
    ) -> "CoaxialConnectionModalAnalysisAtASpeed._Cast_CoaxialConnectionModalAnalysisAtASpeed":
        return self._Cast_CoaxialConnectionModalAnalysisAtASpeed(self)
