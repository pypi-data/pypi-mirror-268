"""ConnectionCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7549
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6591,
        _6554,
        _6556,
        _6560,
        _6563,
        _6568,
        _6572,
        _6575,
        _6577,
        _6581,
        _6584,
        _6588,
        _6594,
        _6598,
        _6600,
        _6602,
        _6608,
        _6613,
        _6617,
        _6619,
        _6621,
        _6624,
        _6627,
        _6634,
        _6637,
        _6644,
        _6646,
        _6651,
        _6654,
        _6656,
        _6660,
        _6663,
        _6671,
        _6678,
        _6681,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConnectionCriticalSpeedAnalysis")


class ConnectionCriticalSpeedAnalysis(_7549.ConnectionStaticLoadAnalysisCase):
    """ConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCriticalSpeedAnalysis")

    class _Cast_ConnectionCriticalSpeedAnalysis:
        """Special nested class for casting ConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
            parent: "ConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6554.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6554,
            )

            return self._parent._cast(
                _6554.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6556.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(
                _6556.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def belt_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6560.BeltConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6560,
            )

            return self._parent._cast(_6560.BeltConnectionCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6563.BevelDifferentialGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6563,
            )

            return self._parent._cast(
                _6563.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6568.BevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6572.ClutchConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6572,
            )

            return self._parent._cast(_6572.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def coaxial_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6575.CoaxialConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6577.ConceptCouplingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(
                _6577.ConceptCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6581.ConceptGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6581,
            )

            return self._parent._cast(_6581.ConceptGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6584.ConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(_6584.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def coupling_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6588.CouplingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6588,
            )

            return self._parent._cast(_6588.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6594.CVTBeltConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6598.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(
                _6598.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6600.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(
                _6600.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6602.CylindricalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.CylindricalGearMeshCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6608.FaceGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(_6608.FaceGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6613.GearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(_6613.GearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6617.HypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(_6617.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6619.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(
                _6619.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6621.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(
                _6621.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6624.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(
                _6624.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6627.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(
                _6627.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6634.PartToPartShearCouplingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6634,
            )

            return self._parent._cast(
                _6634.PartToPartShearCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6637.PlanetaryConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(_6637.PlanetaryConnectionCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6644.RingPinsToDiscConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(
                _6644.RingPinsToDiscConnectionCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6646.RollingRingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.RollingRingConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6651.ShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(
                _6651.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6654.SpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(_6654.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6656.SpringDamperConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6660.StraightBevelDiffGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(
                _6660.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6663.StraightBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6671.TorqueConverterConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6671,
            )

            return self._parent._cast(
                _6671.TorqueConverterConnectionCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6678.WormGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6678,
            )

            return self._parent._cast(_6678.WormGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "_6681.ZerolBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6681,
            )

            return self._parent._cast(_6681.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "ConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionCriticalSpeedAnalysis.TYPE"):
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
    def critical_speed_analysis(self: Self) -> "_6591.CriticalSpeedAnalysis":
        """mastapy.system_model.analyses_and_results.critical_speed_analyses.CriticalSpeedAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSpeedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis":
        return self._Cast_ConnectionCriticalSpeedAnalysis(self)
