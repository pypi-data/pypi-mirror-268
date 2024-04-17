"""SynchroniserPartModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4903,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "SynchroniserPartModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2613
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4980,
        _4983,
        _4944,
        _4890,
        _4946,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SynchroniserPartModalAnalysisAtAStiffness")


class SynchroniserPartModalAnalysisAtAStiffness(
    _4903.CouplingHalfModalAnalysisAtAStiffness
):
    """SynchroniserPartModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartModalAnalysisAtAStiffness"
    )

    class _Cast_SynchroniserPartModalAnalysisAtAStiffness:
        """Special nested class for casting SynchroniserPartModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
            parent: "SynchroniserPartModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4903.CouplingHalfModalAnalysisAtAStiffness":
            return self._parent._cast(_4903.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4944.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4890.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(_4890.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4946.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4980.SynchroniserHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(_4980.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "_4983.SynchroniserSleeveModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4983,
            )

            return self._parent._cast(_4983.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
        ) -> "SynchroniserPartModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "SynchroniserPartModalAnalysisAtAStiffness.TYPE"
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
    ) -> "SynchroniserPartModalAnalysisAtAStiffness._Cast_SynchroniserPartModalAnalysisAtAStiffness":
        return self._Cast_SynchroniserPartModalAnalysisAtAStiffness(self)
