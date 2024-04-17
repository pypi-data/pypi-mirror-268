"""FEPartCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5257,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "FEPartCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5181,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5280,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="FEPartCompoundModalAnalysisAtASpeed")


class FEPartCompoundModalAnalysisAtASpeed(
    _5257.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
):
    """FEPartCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartCompoundModalAnalysisAtASpeed")

    class _Cast_FEPartCompoundModalAnalysisAtASpeed:
        """Special nested class for casting FEPartCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed",
            parent: "FEPartCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed",
        ) -> "_5257.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5257.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed",
        ) -> "FEPartCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "FEPartCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.FEPart":
        """mastapy.system_model.part_model.FEPart

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
    ) -> "List[_5181.FEPartModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.FEPartModalAnalysisAtASpeed]

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
    def planetaries(self: Self) -> "List[FEPartCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.FEPartCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5181.FEPartModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.FEPartModalAnalysisAtASpeed]

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
    ) -> (
        "FEPartCompoundModalAnalysisAtASpeed._Cast_FEPartCompoundModalAnalysisAtASpeed"
    ):
        return self._Cast_FEPartCompoundModalAnalysisAtASpeed(self)
