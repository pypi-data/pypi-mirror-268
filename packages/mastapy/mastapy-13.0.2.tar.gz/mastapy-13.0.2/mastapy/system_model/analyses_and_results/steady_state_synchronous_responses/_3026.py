"""ConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7549
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3097,
        _2994,
        _2995,
        _3000,
        _3002,
        _3007,
        _3012,
        _3015,
        _3017,
        _3020,
        _3023,
        _3028,
        _3031,
        _3035,
        _3036,
        _3038,
        _3045,
        _3050,
        _3054,
        _3057,
        _3058,
        _3061,
        _3064,
        _3072,
        _3075,
        _3082,
        _3084,
        _3089,
        _3091,
        _3094,
        _3100,
        _3103,
        _3112,
        _3118,
        _3121,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConnectionSteadyStateSynchronousResponse")


class ConnectionSteadyStateSynchronousResponse(_7549.ConnectionStaticLoadAnalysisCase):
    """ConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_ConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting ConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
            parent: "ConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_2994.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2994,
            )

            return self._parent._cast(
                _2994.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_2995.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2995,
            )

            return self._parent._cast(
                _2995.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3000.BeltConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3000,
            )

            return self._parent._cast(
                _3000.BeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3002.BevelDifferentialGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3002,
            )

            return self._parent._cast(
                _3002.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3007.BevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3007,
            )

            return self._parent._cast(_3007.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3012.ClutchConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.ClutchConnectionSteadyStateSynchronousResponse
            )

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3015.CoaxialConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(
                _3015.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3017.ConceptCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3017,
            )

            return self._parent._cast(
                _3017.ConceptCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3020.ConceptGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(
                _3020.ConceptGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3023.ConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(
                _3023.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3028.CouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3028,
            )

            return self._parent._cast(
                _3028.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3031.CVTBeltConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(
                _3031.CVTBeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> (
            "_3035.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3035,
            )

            return self._parent._cast(
                _3035.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3036.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3036,
            )

            return self._parent._cast(
                _3036.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3038.CylindricalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3038,
            )

            return self._parent._cast(
                _3038.CylindricalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3045.FaceGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3050.GearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3050,
            )

            return self._parent._cast(_3050.GearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3054.HypoidGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3057.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3058.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> (
            "_3061.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(
                _3061.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3064.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(
                _3064.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3072.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(
                _3072.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3075.PlanetaryConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3075,
            )

            return self._parent._cast(
                _3075.PlanetaryConnectionSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3082.RingPinsToDiscConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.RingPinsToDiscConnectionSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3084.RollingRingConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.RollingRingConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3089.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3089,
            )

            return self._parent._cast(
                _3089.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3091.SpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3091,
            )

            return self._parent._cast(
                _3091.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3094.SpringDamperConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3094,
            )

            return self._parent._cast(
                _3094.SpringDamperConnectionSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3100.StraightBevelDiffGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3100,
            )

            return self._parent._cast(
                _3100.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3103.StraightBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(
                _3103.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3112.TorqueConverterConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3112,
            )

            return self._parent._cast(
                _3112.TorqueConverterConnectionSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3118.WormGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3118,
            )

            return self._parent._cast(_3118.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "_3121.ZerolBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3121,
            )

            return self._parent._cast(
                _3121.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "ConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "ConnectionSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2279.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2279.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response(
        self: Self,
    ) -> "_3097.SteadyStateSynchronousResponse":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SteadyStateSynchronousResponse

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse":
        return self._Cast_ConnectionSteadyStateSynchronousResponse(self)
