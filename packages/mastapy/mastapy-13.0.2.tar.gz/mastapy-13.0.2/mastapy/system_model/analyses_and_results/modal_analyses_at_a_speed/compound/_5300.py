"""CycloidalDiscCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5256,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CycloidalDiscCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2576
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5170,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5257,
        _5280,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundModalAnalysisAtASpeed")


class CycloidalDiscCompoundModalAnalysisAtASpeed(
    _5256.AbstractShaftCompoundModalAnalysisAtASpeed
):
    """CycloidalDiscCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CycloidalDiscCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalDiscCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
            parent: "CycloidalDiscCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_5256.AbstractShaftCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5256.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_5257.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5257,
            )

            return self._parent._cast(
                _5257.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
        ) -> "CycloidalDiscCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CycloidalDiscCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

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
    ) -> "List[_5170.CycloidalDiscModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CycloidalDiscModalAnalysisAtASpeed]

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
    ) -> "List[_5170.CycloidalDiscModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CycloidalDiscModalAnalysisAtASpeed]

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
    ) -> "CycloidalDiscCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed":
        return self._Cast_CycloidalDiscCompoundModalAnalysisAtASpeed(self)
