"""ConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2657
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectionLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6813,
        _6814,
        _6818,
        _6823,
        _6829,
        _6832,
        _6837,
        _6841,
        _6845,
        _6847,
        _6851,
        _6855,
        _6860,
        _6863,
        _6867,
        _6869,
        _6872,
        _6894,
        _6901,
        _6915,
        _6920,
        _6922,
        _6925,
        _6928,
        _6938,
        _6941,
        _6953,
        _6955,
        _6960,
        _6963,
        _6965,
        _6969,
        _6972,
        _6981,
        _6992,
        _6995,
    )
    from mastapy.system_model.analyses_and_results import _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionLoadCase",)


Self = TypeVar("Self", bound="ConnectionLoadCase")


class ConnectionLoadCase(_2657.ConnectionAnalysis):
    """ConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionLoadCase")

    class _Cast_ConnectionLoadCase:
        """Special nested class for casting ConnectionLoadCase to subclasses."""

        def __init__(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
            parent: "ConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def connection_analysis(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_2657.ConnectionAnalysis":
            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6818.AbstractShaftToMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6818

            return self._parent._cast(
                _6818.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6823.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6829.BeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6832.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6832

            return self._parent._cast(_6832.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6837.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6841.ClutchConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ClutchConnectionLoadCase)

        @property
        def coaxial_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6845.CoaxialConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.CoaxialConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6847.ConceptCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6851.ConceptGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6855.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6860.CouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6863.CVTBeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6863

            return self._parent._cast(_6863.CVTBeltConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6867.CycloidalDiscCentralBearingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6867

            return self._parent._cast(
                _6867.CycloidalDiscCentralBearingConnectionLoadCase
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6869.CycloidalDiscPlanetaryBearingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6869

            return self._parent._cast(
                _6869.CycloidalDiscPlanetaryBearingConnectionLoadCase
            )

        @property
        def cylindrical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6872.CylindricalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6872

            return self._parent._cast(_6872.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6894.FaceGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6894

            return self._parent._cast(_6894.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6901.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6901

            return self._parent._cast(_6901.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6915.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(_6915.HypoidGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6920.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(_6920.InterMountableComponentConnectionLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6922.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(
                _6922.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6925.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(
                _6925.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6928.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(
                _6928.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6938.PartToPartShearCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.PartToPartShearCouplingConnectionLoadCase)

        @property
        def planetary_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6941.PlanetaryConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(_6941.PlanetaryConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6953.RingPinsToDiscConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6955.RollingRingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.RollingRingConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6960.ShaftToMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.ShaftToMountableComponentConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6963.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6965.SpringDamperConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6969.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6972.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6972

            return self._parent._cast(_6972.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6981.TorqueConverterConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6992.WormGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6992

            return self._parent._cast(_6992.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "_6995.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6995

            return self._parent._cast(_6995.ZerolBevelGearMeshLoadCase)

        @property
        def connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "ConnectionLoadCase":
            return self._parent

        def __getattr__(self: "ConnectionLoadCase._Cast_ConnectionLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionLoadCase.TYPE"):
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
    def static_load_case(self: Self) -> "_6813.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case(self: Self) -> "_6814.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectionLoadCase._Cast_ConnectionLoadCase":
        return self._Cast_ConnectionLoadCase(self)
