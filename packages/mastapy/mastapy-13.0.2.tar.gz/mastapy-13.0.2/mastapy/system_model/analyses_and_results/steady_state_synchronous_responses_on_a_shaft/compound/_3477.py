"""RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3390,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3347,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3383,
        _3462,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"
)


class RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft(
    _3390.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
):
    """RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3390.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3390.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3383.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3383,
            )

            return self._parent._cast(
                _3383.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def root_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3347.RootAssemblySteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.RootAssemblySteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3347.RootAssemblySteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.RootAssemblySteadyStateSynchronousResponseOnAShaft]

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
    ) -> "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
