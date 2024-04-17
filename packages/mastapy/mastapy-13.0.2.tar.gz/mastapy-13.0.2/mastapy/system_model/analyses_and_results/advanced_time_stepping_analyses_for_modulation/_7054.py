"""ConnectionAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7549
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7018,
        _7017,
        _7023,
        _7028,
        _7031,
        _7036,
        _7041,
        _7043,
        _7046,
        _7049,
        _7052,
        _7057,
        _7060,
        _7064,
        _7065,
        _7067,
        _7073,
        _7078,
        _7083,
        _7085,
        _7087,
        _7090,
        _7093,
        _7101,
        _7103,
        _7110,
        _7113,
        _7117,
        _7120,
        _7123,
        _7126,
        _7129,
        _7138,
        _7144,
        _7147,
    )
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model.analyses_and_results.system_deflections import _2735
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="ConnectionAdvancedTimeSteppingAnalysisForModulation")


class ConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7549.ConnectionStaticLoadAnalysisCase
):
    """ConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7017.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7017,
            )

            return self._parent._cast(
                _7017.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7023.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7023,
            )

            return self._parent._cast(
                _7023.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7028.BeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7028,
            )

            return self._parent._cast(
                _7028.BeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7031.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7031,
            )

            return self._parent._cast(
                _7031.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7036.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7041.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7043.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7046.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7049.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7049,
            )

            return self._parent._cast(
                _7049.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7052.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7057.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7057,
            )

            return self._parent._cast(
                _7057.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7060.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7060,
            )

            return self._parent._cast(
                _7060.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7064.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7064,
            )

            return self._parent._cast(
                _7064.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7065.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7065,
            )

            return self._parent._cast(
                _7065.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7067.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7073.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7073,
            )

            return self._parent._cast(
                _7073.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7078.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7078,
            )

            return self._parent._cast(
                _7078.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7083.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7083,
            )

            return self._parent._cast(
                _7083.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7087.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7090.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7093.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7101.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7101,
            )

            return self._parent._cast(
                _7101.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7103.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7110.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7113.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7120.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7123.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7126.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7126,
            )

            return self._parent._cast(
                _7126.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7129.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7138.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7138,
            )

            return self._parent._cast(
                _7138.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7144.WormGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7144,
            )

            return self._parent._cast(
                _7144.WormGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7147.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7147,
            )

            return self._parent._cast(
                _7147.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "_7018.AdvancedTimeSteppingAnalysisForModulation":
        """mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AdvancedTimeSteppingAnalysisForModulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def system_deflection_results(self: Self) -> "_2735.ConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation(self)
