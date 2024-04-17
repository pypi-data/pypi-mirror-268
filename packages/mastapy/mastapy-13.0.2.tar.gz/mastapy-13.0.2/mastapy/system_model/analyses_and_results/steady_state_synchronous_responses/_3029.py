"""CouplingHalfSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3069,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CouplingHalfSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2592
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3013,
        _3018,
        _3032,
        _3073,
        _3080,
        _3085,
        _3095,
        _3108,
        _3109,
        _3110,
        _3113,
        _3115,
        _3016,
        _3071,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CouplingHalfSteadyStateSynchronousResponse")


class CouplingHalfSteadyStateSynchronousResponse(
    _3069.MountableComponentSteadyStateSynchronousResponse
):
    """CouplingHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfSteadyStateSynchronousResponse"
    )

    class _Cast_CouplingHalfSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingHalfSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
            parent: "CouplingHalfSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3069.MountableComponentSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3069.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3016.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3071.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3013.ClutchHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(_3013.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3018.ConceptCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.ConceptCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3032.CVTPulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3032,
            )

            return self._parent._cast(_3032.CVTPulleySteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3073.PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3073,
            )

            return self._parent._cast(
                _3073.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def pulley_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3080.PulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3080,
            )

            return self._parent._cast(_3080.PulleySteadyStateSynchronousResponse)

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3085.RollingRingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3085,
            )

            return self._parent._cast(_3085.RollingRingSteadyStateSynchronousResponse)

        @property
        def spring_damper_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3095.SpringDamperHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3095,
            )

            return self._parent._cast(
                _3095.SpringDamperHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3108.SynchroniserHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3108,
            )

            return self._parent._cast(
                _3108.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3109.SynchroniserPartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3109,
            )

            return self._parent._cast(
                _3109.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3110.SynchroniserSleeveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(
                _3110.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3113.TorqueConverterPumpSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3113,
            )

            return self._parent._cast(
                _3113.TorqueConverterPumpSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3115.TorqueConverterTurbineSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3115,
            )

            return self._parent._cast(
                _3115.TorqueConverterTurbineSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "CouplingHalfSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CouplingHalfSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2592.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse":
        return self._Cast_CouplingHalfSteadyStateSynchronousResponse(self)
