"""PowerLoadCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5118,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "PowerLoadCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4954,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5073,
        _5021,
        _5075,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PowerLoadCompoundModalAnalysisAtAStiffness")


class PowerLoadCompoundModalAnalysisAtAStiffness(
    _5118.VirtualComponentCompoundModalAnalysisAtAStiffness
):
    """PowerLoadCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PowerLoadCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_PowerLoadCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting PowerLoadCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness",
            parent: "PowerLoadCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness",
        ) -> "_5118.VirtualComponentCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5118.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness",
        ) -> "_5073.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5073,
            )

            return self._parent._cast(
                _5073.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness",
        ) -> "_5021.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(_5021.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness",
        ) -> "PowerLoadCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "PowerLoadCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4954.PowerLoadModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PowerLoadModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4954.PowerLoadModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PowerLoadModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PowerLoadCompoundModalAnalysisAtAStiffness._Cast_PowerLoadCompoundModalAnalysisAtAStiffness":
        return self._Cast_PowerLoadCompoundModalAnalysisAtAStiffness(self)
