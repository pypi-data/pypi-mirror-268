"""CoaxialConnectionModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4964,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CoaxialConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2276
    from mastapy.system_model.analyses_and_results.static_loads import _6845
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4909,
        _4868,
        _4900,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CoaxialConnectionModalAnalysisAtAStiffness")


class CoaxialConnectionModalAnalysisAtAStiffness(
    _4964.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
):
    """CoaxialConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_CoaxialConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting CoaxialConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
            parent: "CoaxialConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_4964.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4964.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> (
            "_4868.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4868,
            )

            return self._parent._cast(
                _4868.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_4900.ConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4900,
            )

            return self._parent._cast(_4900.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "_4909.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4909,
            )

            return self._parent._cast(
                _4909.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
        ) -> "CoaxialConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CoaxialConnectionModalAnalysisAtAStiffness.TYPE"
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
    ) -> "CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness":
        return self._Cast_CoaxialConnectionModalAnalysisAtAStiffness(self)
