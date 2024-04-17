"""ConnectionDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7548
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6337,
        _6288,
        _6290,
        _6294,
        _6297,
        _6302,
        _6306,
        _6309,
        _6311,
        _6315,
        _6318,
        _6322,
        _6325,
        _6329,
        _6331,
        _6333,
        _6341,
        _6346,
        _6350,
        _6352,
        _6354,
        _6357,
        _6360,
        _6367,
        _6370,
        _6377,
        _6379,
        _6384,
        _6387,
        _6389,
        _6393,
        _6396,
        _6404,
        _6411,
        _6414,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="ConnectionDynamicAnalysis")


class ConnectionDynamicAnalysis(_7548.ConnectionFEAnalysis):
    """ConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionDynamicAnalysis")

    class _Cast_ConnectionDynamicAnalysis:
        """Special nested class for casting ConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
            parent: "ConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_fe_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_7548.ConnectionFEAnalysis":
            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6288.AbstractShaftToMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(
                _6288.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6290.AGMAGleasonConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def belt_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6294.BeltConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.BeltConnectionDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6297.BevelDifferentialGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297

            return self._parent._cast(_6297.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6302.BevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.BevelGearMeshDynamicAnalysis)

        @property
        def clutch_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6306.ClutchConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.ClutchConnectionDynamicAnalysis)

        @property
        def coaxial_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6309.CoaxialConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.CoaxialConnectionDynamicAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6311.ConceptCouplingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConceptCouplingConnectionDynamicAnalysis)

        @property
        def concept_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6315.ConceptGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.ConceptGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6318.ConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.ConicalGearMeshDynamicAnalysis)

        @property
        def coupling_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6322.CouplingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.CouplingConnectionDynamicAnalysis)

        @property
        def cvt_belt_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6325.CVTBeltConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.CVTBeltConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6329.CycloidalDiscCentralBearingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329

            return self._parent._cast(
                _6329.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6331.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(
                _6331.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis
            )

        @property
        def cylindrical_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6333.CylindricalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.CylindricalGearMeshDynamicAnalysis)

        @property
        def face_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6341.FaceGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(_6341.FaceGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6346.GearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(_6346.GearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6350.HypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(_6350.HypoidGearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6352.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(
                _6352.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6354.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(
                _6354.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6357.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(
                _6357.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6360.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(
                _6360.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6367.PartToPartShearCouplingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(
                _6367.PartToPartShearCouplingConnectionDynamicAnalysis
            )

        @property
        def planetary_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6370.PlanetaryConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.PlanetaryConnectionDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6377.RingPinsToDiscConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.RingPinsToDiscConnectionDynamicAnalysis)

        @property
        def rolling_ring_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6379.RollingRingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.RollingRingConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6384.ShaftToMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(
                _6384.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6387.SpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def spring_damper_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6389.SpringDamperConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.SpringDamperConnectionDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6393.StraightBevelDiffGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6396.StraightBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.StraightBevelGearMeshDynamicAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6404.TorqueConverterConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.TorqueConverterConnectionDynamicAnalysis)

        @property
        def worm_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6411.WormGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6411

            return self._parent._cast(_6411.WormGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "_6414.ZerolBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6414

            return self._parent._cast(_6414.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def connection_dynamic_analysis(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis",
        ) -> "ConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionDynamicAnalysis.TYPE"):
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
    def dynamic_analysis(self: Self) -> "_6337.DynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.DynamicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionDynamicAnalysis._Cast_ConnectionDynamicAnalysis":
        return self._Cast_ConnectionDynamicAnalysis(self)
