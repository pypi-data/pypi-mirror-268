"""CylindricalGearMeshCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3183,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2316
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3038,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3189,
        _3159,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="CylindricalGearMeshCompoundSteadyStateSynchronousResponse"
)


class CylindricalGearMeshCompoundSteadyStateSynchronousResponse(
    _3183.GearMeshCompoundSteadyStateSynchronousResponse
):
    """CylindricalGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CylindricalGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3183.GearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3183.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3189.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3189,
            )

            return self._parent._cast(
                _3189.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3159.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3159,
            )

            return self._parent._cast(
                _3159.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response(
            self: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "CylindricalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CylindricalGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2316.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2316.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

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
    ) -> "List[_3038.CylindricalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalGearMeshSteadyStateSynchronousResponse]

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
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearMeshCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.CylindricalGearMeshCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3038.CylindricalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalGearMeshSteadyStateSynchronousResponse]

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
    ) -> "CylindricalGearMeshCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse":
        return self._Cast_CylindricalGearMeshCompoundSteadyStateSynchronousResponse(
            self
        )
