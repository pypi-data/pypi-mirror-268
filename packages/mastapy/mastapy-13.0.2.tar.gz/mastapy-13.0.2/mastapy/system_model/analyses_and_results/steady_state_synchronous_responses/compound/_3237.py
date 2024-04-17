"""SynchroniserCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3222,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "SynchroniserCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3111,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3124,
        _3203,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SynchroniserCompoundSteadyStateSynchronousResponse")


class SynchroniserCompoundSteadyStateSynchronousResponse(
    _3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
):
    """SynchroniserCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_SynchroniserCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting SynchroniserCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SynchroniserCompoundSteadyStateSynchronousResponse._Cast_SynchroniserCompoundSteadyStateSynchronousResponse",
            parent: "SynchroniserCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "SynchroniserCompoundSteadyStateSynchronousResponse._Cast_SynchroniserCompoundSteadyStateSynchronousResponse",
        ) -> "_3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3222.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "SynchroniserCompoundSteadyStateSynchronousResponse._Cast_SynchroniserCompoundSteadyStateSynchronousResponse",
        ) -> "_3124.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "SynchroniserCompoundSteadyStateSynchronousResponse._Cast_SynchroniserCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(_3203.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "SynchroniserCompoundSteadyStateSynchronousResponse._Cast_SynchroniserCompoundSteadyStateSynchronousResponse",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserCompoundSteadyStateSynchronousResponse._Cast_SynchroniserCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserCompoundSteadyStateSynchronousResponse._Cast_SynchroniserCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_compound_steady_state_synchronous_response(
            self: "SynchroniserCompoundSteadyStateSynchronousResponse._Cast_SynchroniserCompoundSteadyStateSynchronousResponse",
        ) -> "SynchroniserCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SynchroniserCompoundSteadyStateSynchronousResponse._Cast_SynchroniserCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SynchroniserCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2610.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3111.SynchroniserSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SynchroniserSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3111.SynchroniserSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SynchroniserSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserCompoundSteadyStateSynchronousResponse._Cast_SynchroniserCompoundSteadyStateSynchronousResponse":
        return self._Cast_SynchroniserCompoundSteadyStateSynchronousResponse(self)
