"""TorqueConverterSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3030,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "TorqueConverterSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2615
    from mastapy.system_model.analyses_and_results.static_loads import _6982
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3090,
        _2991,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="TorqueConverterSteadyStateSynchronousResponse")


class TorqueConverterSteadyStateSynchronousResponse(
    _3030.CouplingSteadyStateSynchronousResponse
):
    """TorqueConverterSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterSteadyStateSynchronousResponse"
    )

    class _Cast_TorqueConverterSteadyStateSynchronousResponse:
        """Special nested class for casting TorqueConverterSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
            parent: "TorqueConverterSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_3030.CouplingSteadyStateSynchronousResponse":
            return self._parent._cast(_3030.CouplingSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_3090.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(
                _3090.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_2991.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(
                _2991.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
        ) -> "TorqueConverterSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse",
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
        instance_to_wrap: "TorqueConverterSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2615.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6982.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

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
    ) -> "TorqueConverterSteadyStateSynchronousResponse._Cast_TorqueConverterSteadyStateSynchronousResponse":
        return self._Cast_TorqueConverterSteadyStateSynchronousResponse(self)
