"""InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3159,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3057,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3129,
        _3133,
        _3136,
        _3141,
        _3146,
        _3151,
        _3154,
        _3157,
        _3162,
        _3164,
        _3172,
        _3178,
        _3183,
        _3187,
        _3191,
        _3194,
        _3197,
        _3205,
        _3214,
        _3217,
        _3224,
        _3227,
        _3230,
        _3233,
        _3242,
        _3248,
        _3251,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)


class InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
    _3159.ConnectionCompoundSteadyStateSynchronousResponse
):
    """InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = (
        _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
            parent: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3159.ConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3159.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3129.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3129,
            )

            return self._parent._cast(
                _3129.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3133.BeltConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3133,
            )

            return self._parent._cast(
                _3133.BeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3136.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3136,
            )

            return self._parent._cast(
                _3136.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3141.BevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3146.ClutchConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3146,
            )

            return self._parent._cast(
                _3146.ClutchConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3154.ConceptGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3154,
            )

            return self._parent._cast(
                _3154.ConceptGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3157.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3157,
            )

            return self._parent._cast(
                _3157.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.CouplingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.CouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.CVTBeltConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.CVTBeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.CylindricalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.CylindricalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3178.FaceGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3178,
            )

            return self._parent._cast(
                _3178.FaceGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3183.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3183,
            )

            return self._parent._cast(
                _3183.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3187.HypoidGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3187,
            )

            return self._parent._cast(
                _3187.HypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3191.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3194.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3194,
            )

            return self._parent._cast(
                _3194.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(
                _3197.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3205.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3205,
            )

            return self._parent._cast(
                _3205.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3214.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3217.RollingRingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3217,
            )

            return self._parent._cast(
                _3217.RollingRingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3224.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3224,
            )

            return self._parent._cast(
                _3224.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3227.SpringDamperConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3227,
            )

            return self._parent._cast(
                _3227.SpringDamperConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3230.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3230,
            )

            return self._parent._cast(
                _3230.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3233.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3233,
            )

            return self._parent._cast(
                _3233.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3242.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3242,
            )

            return self._parent._cast(
                _3242.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3248.WormGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3248,
            )

            return self._parent._cast(
                _3248.WormGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3251.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3251,
            )

            return self._parent._cast(
                _3251.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.InterMountableComponentConnectionSteadyStateSynchronousResponse]

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
    ) -> "List[_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.InterMountableComponentConnectionSteadyStateSynchronousResponse]

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
    ) -> "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
            self
        )
