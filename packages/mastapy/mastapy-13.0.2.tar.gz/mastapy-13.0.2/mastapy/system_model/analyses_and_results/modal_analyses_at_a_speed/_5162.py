"""CouplingConnectionModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5190
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CouplingConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2353
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5146,
        _5151,
        _5206,
        _5228,
        _5243,
        _5160,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CouplingConnectionModalAnalysisAtASpeed")


class CouplingConnectionModalAnalysisAtASpeed(
    _5190.InterMountableComponentConnectionModalAnalysisAtASpeed
):
    """CouplingConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionModalAnalysisAtASpeed"
    )

    class _Cast_CouplingConnectionModalAnalysisAtASpeed:
        """Special nested class for casting CouplingConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
            parent: "CouplingConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5190.InterMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent._cast(
                _5190.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5160.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5146.ClutchConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(_5146.ClutchConnectionModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5151.ConceptCouplingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(
                _5151.ConceptCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5206.PartToPartShearCouplingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(
                _5206.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5228.SpringDamperConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.SpringDamperConnectionModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "_5243.TorqueConverterConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5243,
            )

            return self._parent._cast(
                _5243.TorqueConverterConnectionModalAnalysisAtASpeed
            )

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
        ) -> "CouplingConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CouplingConnectionModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2353.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

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
    ) -> "CouplingConnectionModalAnalysisAtASpeed._Cast_CouplingConnectionModalAnalysisAtASpeed":
        return self._Cast_CouplingConnectionModalAnalysisAtASpeed(self)
