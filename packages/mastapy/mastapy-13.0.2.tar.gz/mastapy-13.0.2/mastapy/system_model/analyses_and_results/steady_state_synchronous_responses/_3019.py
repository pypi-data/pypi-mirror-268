"""ConceptCouplingSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3030,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConceptCouplingSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.static_loads import _6849
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3090,
        _2991,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConceptCouplingSteadyStateSynchronousResponse")


class ConceptCouplingSteadyStateSynchronousResponse(
    _3030.CouplingSteadyStateSynchronousResponse
):
    """ConceptCouplingSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingSteadyStateSynchronousResponse"
    )

    class _Cast_ConceptCouplingSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptCouplingSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
            parent: "ConceptCouplingSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_3030.CouplingSteadyStateSynchronousResponse":
            return self._parent._cast(_3030.CouplingSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_3090.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(
                _3090.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_2991.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(
                _2991.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "ConceptCouplingSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConceptCouplingSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2588.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6849.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse":
        return self._Cast_ConceptCouplingSteadyStateSynchronousResponse(self)
