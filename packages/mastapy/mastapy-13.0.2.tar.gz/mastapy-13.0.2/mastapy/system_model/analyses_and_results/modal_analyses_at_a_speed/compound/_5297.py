"""CVTPulleyCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5343,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CVTPulleyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5167,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5294,
        _5332,
        _5280,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CVTPulleyCompoundModalAnalysisAtASpeed")


class CVTPulleyCompoundModalAnalysisAtASpeed(_5343.PulleyCompoundModalAnalysisAtASpeed):
    """CVTPulleyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CVTPulleyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CVTPulleyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
            parent: "CVTPulleyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
        ) -> "_5343.PulleyCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5343.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
        ) -> "_5294.CouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(_5294.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
        ) -> "_5332.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(
                _5332.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
        ) -> "CVTPulleyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5167.CVTPulleyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CVTPulleyModalAnalysisAtASpeed]

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
    ) -> "List[_5167.CVTPulleyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CVTPulleyModalAnalysisAtASpeed]

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
    ) -> "CVTPulleyCompoundModalAnalysisAtASpeed._Cast_CVTPulleyCompoundModalAnalysisAtASpeed":
        return self._Cast_CVTPulleyCompoundModalAnalysisAtASpeed(self)
