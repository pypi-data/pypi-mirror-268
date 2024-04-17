"""ConceptGearCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5054,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ConceptGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4895,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5073,
        _5021,
        _5075,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConceptGearCompoundModalAnalysisAtAStiffness")


class ConceptGearCompoundModalAnalysisAtAStiffness(
    _5054.GearCompoundModalAnalysisAtAStiffness
):
    """ConceptGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_ConceptGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ConceptGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness",
            parent: "ConceptGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5054.GearCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5054.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5073.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5073,
            )

            return self._parent._cast(
                _5073.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5021.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(_5021.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness",
        ) -> "ConceptGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "ConceptGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2528.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

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
    ) -> "List[_4895.ConceptGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConceptGearModalAnalysisAtAStiffness]

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
    ) -> "List[_4895.ConceptGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConceptGearModalAnalysisAtAStiffness]

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
    ) -> "ConceptGearCompoundModalAnalysisAtAStiffness._Cast_ConceptGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_ConceptGearCompoundModalAnalysisAtAStiffness(self)
