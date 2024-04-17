"""ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3667,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3564,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3721,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed"
)


class ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed(
    _3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3667.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

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
    ) -> "List[_3564.ExternalCADModelSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ExternalCADModelSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3564.ExternalCADModelSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ExternalCADModelSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
