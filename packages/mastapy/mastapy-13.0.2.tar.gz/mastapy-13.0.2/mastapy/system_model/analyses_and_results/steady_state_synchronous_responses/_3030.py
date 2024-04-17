"""CouplingSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3090,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CouplingSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3014,
        _3019,
        _3074,
        _3096,
        _3114,
        _2991,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CouplingSteadyStateSynchronousResponse")


class CouplingSteadyStateSynchronousResponse(
    _3090.SpecialisedAssemblySteadyStateSynchronousResponse
):
    """CouplingSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingSteadyStateSynchronousResponse"
    )

    class _Cast_CouplingSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
            parent: "CouplingSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3090.SpecialisedAssemblySteadyStateSynchronousResponse":
            return self._parent._cast(
                _3090.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_2991.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(
                _2991.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3014.ClutchSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(_3014.ClutchSteadyStateSynchronousResponse)

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3019.ConceptCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(
                _3019.ConceptCouplingSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3074.PartToPartShearCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(
                _3074.PartToPartShearCouplingSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3096.SpringDamperSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(_3096.SpringDamperSteadyStateSynchronousResponse)

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3114.TorqueConverterSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3114,
            )

            return self._parent._cast(
                _3114.TorqueConverterSteadyStateSynchronousResponse
            )

        @property
        def coupling_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "CouplingSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CouplingSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2591.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse":
        return self._Cast_CouplingSteadyStateSynchronousResponse(self)
