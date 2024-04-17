"""AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5280,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5127,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5256,
        _5300,
        _5311,
        _5350,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundModalAnalysisAtASpeed")


class AbstractShaftOrHousingCompoundModalAnalysisAtASpeed(
    _5280.ComponentCompoundModalAnalysisAtASpeed
):
    """AbstractShaftOrHousingCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"
    )

    class _Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftOrHousingCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
            parent: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5256.AbstractShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(_5256.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5300.CycloidalDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5300,
            )

            return self._parent._cast(_5300.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5311.FEPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(_5311.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "_5350.ShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(_5350.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
        ) -> "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5127.AbstractShaftOrHousingModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftOrHousingModalAnalysisAtASpeed]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5127.AbstractShaftOrHousingModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftOrHousingModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
        return self._Cast_AbstractShaftOrHousingCompoundModalAnalysisAtASpeed(self)
