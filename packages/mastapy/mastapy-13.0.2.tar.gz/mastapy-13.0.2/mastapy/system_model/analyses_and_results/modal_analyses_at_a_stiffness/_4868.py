"""AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4900,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
        "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2272
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4889,
        _4909,
        _4911,
        _4950,
        _4964,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness"
)


class AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness(
    _4900.ConnectionModalAnalysisAtAStiffness
):
    """AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = (
        _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
            parent: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4900.ConnectionModalAnalysisAtAStiffness":
            return self._parent._cast(_4900.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4889.CoaxialConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.CoaxialConnectionModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4909.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4909,
            )

            return self._parent._cast(
                _4909.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4911.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4911,
            )

            return self._parent._cast(
                _4911.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4950.PlanetaryConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4950,
            )

            return self._parent._cast(
                _4950.PlanetaryConnectionModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4964.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4964,
            )

            return self._parent._cast(
                _4964.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2272.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness":
        return self._Cast_AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness(
            self
        )
