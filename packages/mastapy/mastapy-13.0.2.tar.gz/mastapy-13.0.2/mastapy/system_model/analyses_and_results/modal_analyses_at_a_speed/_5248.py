"""VirtualComponentModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5203
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "VirtualComponentModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5200,
        _5201,
        _5212,
        _5213,
        _5247,
        _5150,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="VirtualComponentModalAnalysisAtASpeed")


class VirtualComponentModalAnalysisAtASpeed(
    _5203.MountableComponentModalAnalysisAtASpeed
):
    """VirtualComponentModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentModalAnalysisAtASpeed"
    )

    class _Cast_VirtualComponentModalAnalysisAtASpeed:
        """Special nested class for casting VirtualComponentModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
            parent: "VirtualComponentModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5203.MountableComponentModalAnalysisAtASpeed":
            return self._parent._cast(_5203.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5150.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5200.MassDiscModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5200,
            )

            return self._parent._cast(_5200.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5201.MeasurementComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5201,
            )

            return self._parent._cast(_5201.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5212.PointLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(_5212.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5213.PowerLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.PowerLoadModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "_5247.UnbalancedMassModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5247,
            )

            return self._parent._cast(_5247.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
        ) -> "VirtualComponentModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "VirtualComponentModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2486.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentModalAnalysisAtASpeed._Cast_VirtualComponentModalAnalysisAtASpeed":
        return self._Cast_VirtualComponentModalAnalysisAtASpeed(self)
