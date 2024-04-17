"""KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3191,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2326
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3061,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3157,
        _3183,
        _3189,
        _3159,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
)


class KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse(
    _3191.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3191.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3191.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3157.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3157,
            )

            return self._parent._cast(
                _3157.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3183.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3183,
            )

            return self._parent._cast(
                _3183.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3189.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3189,
            )

            return self._parent._cast(
                _3189.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3159.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3159,
            )

            return self._parent._cast(
                _3159.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2326.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2326.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3061.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3061.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse(
            self
        )
