"""GuideDxfModelCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5280,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "GuideDxfModelCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5186,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="GuideDxfModelCompoundModalAnalysisAtASpeed")


class GuideDxfModelCompoundModalAnalysisAtASpeed(
    _5280.ComponentCompoundModalAnalysisAtASpeed
):
    """GuideDxfModelCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelCompoundModalAnalysisAtASpeed"
    )

    class _Cast_GuideDxfModelCompoundModalAnalysisAtASpeed:
        """Special nested class for casting GuideDxfModelCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "GuideDxfModelCompoundModalAnalysisAtASpeed._Cast_GuideDxfModelCompoundModalAnalysisAtASpeed",
            parent: "GuideDxfModelCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "GuideDxfModelCompoundModalAnalysisAtASpeed._Cast_GuideDxfModelCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "GuideDxfModelCompoundModalAnalysisAtASpeed._Cast_GuideDxfModelCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "GuideDxfModelCompoundModalAnalysisAtASpeed._Cast_GuideDxfModelCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GuideDxfModelCompoundModalAnalysisAtASpeed._Cast_GuideDxfModelCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCompoundModalAnalysisAtASpeed._Cast_GuideDxfModelCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(
            self: "GuideDxfModelCompoundModalAnalysisAtASpeed._Cast_GuideDxfModelCompoundModalAnalysisAtASpeed",
        ) -> "GuideDxfModelCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCompoundModalAnalysisAtASpeed._Cast_GuideDxfModelCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "GuideDxfModelCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

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
    ) -> "List[_5186.GuideDxfModelModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.GuideDxfModelModalAnalysisAtASpeed]

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
    ) -> "List[_5186.GuideDxfModelModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.GuideDxfModelModalAnalysisAtASpeed]

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
    ) -> "GuideDxfModelCompoundModalAnalysisAtASpeed._Cast_GuideDxfModelCompoundModalAnalysisAtASpeed":
        return self._Cast_GuideDxfModelCompoundModalAnalysisAtASpeed(self)
