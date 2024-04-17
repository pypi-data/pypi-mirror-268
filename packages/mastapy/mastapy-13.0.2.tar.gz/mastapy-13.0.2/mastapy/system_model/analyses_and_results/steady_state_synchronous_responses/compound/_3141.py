"""BevelGearMeshCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3129,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BevelGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3007,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3136,
        _3224,
        _3230,
        _3233,
        _3251,
        _3157,
        _3183,
        _3189,
        _3159,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundSteadyStateSynchronousResponse")


class BevelGearMeshCompoundSteadyStateSynchronousResponse(
    _3129.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
):
    """BevelGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting BevelGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3129.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3129.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3157.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3157,
            )

            return self._parent._cast(
                _3157.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3183.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3183,
            )

            return self._parent._cast(
                _3183.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3189.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3189,
            )

            return self._parent._cast(
                _3189.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3159.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3159,
            )

            return self._parent._cast(
                _3159.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3136.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3136,
            )

            return self._parent._cast(
                _3136.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3224.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3224,
            )

            return self._parent._cast(
                _3224.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3230.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3230,
            )

            return self._parent._cast(
                _3230.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3233.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3233,
            )

            return self._parent._cast(
                _3233.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3251.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3251,
            )

            return self._parent._cast(
                _3251.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "BevelGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3007.BevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3007.BevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse":
        return self._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse(self)
