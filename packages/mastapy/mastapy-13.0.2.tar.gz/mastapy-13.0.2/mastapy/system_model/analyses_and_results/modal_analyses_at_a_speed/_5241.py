"""SynchroniserPartModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5163
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "SynchroniserPartModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2613
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5239,
        _5242,
        _5203,
        _5150,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SynchroniserPartModalAnalysisAtASpeed")


class SynchroniserPartModalAnalysisAtASpeed(_5163.CouplingHalfModalAnalysisAtASpeed):
    """SynchroniserPartModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartModalAnalysisAtASpeed"
    )

    class _Cast_SynchroniserPartModalAnalysisAtASpeed:
        """Special nested class for casting SynchroniserPartModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
            parent: "SynchroniserPartModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_5163.CouplingHalfModalAnalysisAtASpeed":
            return self._parent._cast(_5163.CouplingHalfModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_5203.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_5150.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_5239.SynchroniserHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "_5242.SynchroniserSleeveModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5242,
            )

            return self._parent._cast(_5242.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
        ) -> "SynchroniserPartModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "SynchroniserPartModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2613.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartModalAnalysisAtASpeed._Cast_SynchroniserPartModalAnalysisAtASpeed":
        return self._Cast_SynchroniserPartModalAnalysisAtASpeed(self)
