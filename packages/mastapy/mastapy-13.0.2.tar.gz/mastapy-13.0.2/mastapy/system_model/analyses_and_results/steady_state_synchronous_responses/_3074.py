"""PartToPartShearCouplingSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3030,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "PartToPartShearCouplingSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6940
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3090,
        _2991,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="PartToPartShearCouplingSteadyStateSynchronousResponse")


class PartToPartShearCouplingSteadyStateSynchronousResponse(
    _3030.CouplingSteadyStateSynchronousResponse
):
    """PartToPartShearCouplingSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingSteadyStateSynchronousResponse"
    )

    class _Cast_PartToPartShearCouplingSteadyStateSynchronousResponse:
        """Special nested class for casting PartToPartShearCouplingSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
            parent: "PartToPartShearCouplingSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
        ) -> "_3030.CouplingSteadyStateSynchronousResponse":
            return self._parent._cast(_3030.CouplingSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
        ) -> "_3090.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(
                _3090.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
        ) -> "_2991.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(
                _2991.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
        ) -> "PartToPartShearCouplingSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PartToPartShearCouplingSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2596.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6940.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

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
    ) -> "PartToPartShearCouplingSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse":
        return self._Cast_PartToPartShearCouplingSteadyStateSynchronousResponse(self)
