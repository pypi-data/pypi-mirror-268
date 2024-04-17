"""Socket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451, _2452
    from mastapy.system_model.connections_and_sockets import (
        _2279,
        _2273,
        _2274,
        _2281,
        _2283,
        _2285,
        _2286,
        _2287,
        _2289,
        _2290,
        _2291,
        _2292,
        _2293,
        _2295,
        _2296,
        _2297,
        _2300,
        _2301,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2307,
        _2309,
        _2311,
        _2313,
        _2315,
        _2317,
        _2319,
        _2321,
        _2323,
        _2324,
        _2328,
        _2329,
        _2331,
        _2333,
        _2335,
        _2337,
        _2339,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2340,
        _2341,
        _2343,
        _2344,
        _2346,
        _2347,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2350,
        _2352,
        _2354,
        _2356,
        _2358,
        _2360,
        _2361,
    )


__docformat__ = "restructuredtext en"
__all__ = ("Socket",)


Self = TypeVar("Self", bound="Socket")


class Socket(_0.APIBase):
    """Socket

    This is a mastapy class.
    """

    TYPE = _SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Socket")

    class _Cast_Socket:
        """Special nested class for casting Socket to subclasses."""

        def __init__(self: "Socket._Cast_Socket", parent: "Socket"):
            self._parent = parent

        @property
        def bearing_inner_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2273.BearingInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2273

            return self._parent._cast(_2273.BearingInnerSocket)

        @property
        def bearing_outer_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2274.BearingOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.BearingOuterSocket)

        @property
        def cvt_pulley_socket(self: "Socket._Cast_Socket") -> "_2281.CVTPulleySocket":
            from mastapy.system_model.connections_and_sockets import _2281

            return self._parent._cast(_2281.CVTPulleySocket)

        @property
        def cylindrical_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def electric_machine_stator_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2285.ElectricMachineStatorSocket":
            from mastapy.system_model.connections_and_sockets import _2285

            return self._parent._cast(_2285.ElectricMachineStatorSocket)

        @property
        def inner_shaft_socket(self: "Socket._Cast_Socket") -> "_2286.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2286

            return self._parent._cast(_2286.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(
            self: "Socket._Cast_Socket",
        ) -> "_2287.InnerShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2287

            return self._parent._cast(_2287.InnerShaftSocketBase)

        @property
        def mountable_component_inner_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2289.MountableComponentInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2289

            return self._parent._cast(_2289.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2290.MountableComponentOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2291.MountableComponentSocket":
            from mastapy.system_model.connections_and_sockets import _2291

            return self._parent._cast(_2291.MountableComponentSocket)

        @property
        def outer_shaft_socket(self: "Socket._Cast_Socket") -> "_2292.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(
            self: "Socket._Cast_Socket",
        ) -> "_2293.OuterShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.OuterShaftSocketBase)

        @property
        def planetary_socket(self: "Socket._Cast_Socket") -> "_2295.PlanetarySocket":
            from mastapy.system_model.connections_and_sockets import _2295

            return self._parent._cast(_2295.PlanetarySocket)

        @property
        def planetary_socket_base(
            self: "Socket._Cast_Socket",
        ) -> "_2296.PlanetarySocketBase":
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.PlanetarySocketBase)

        @property
        def pulley_socket(self: "Socket._Cast_Socket") -> "_2297.PulleySocket":
            from mastapy.system_model.connections_and_sockets import _2297

            return self._parent._cast(_2297.PulleySocket)

        @property
        def rolling_ring_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2300.RollingRingSocket":
            from mastapy.system_model.connections_and_sockets import _2300

            return self._parent._cast(_2300.RollingRingSocket)

        @property
        def shaft_socket(self: "Socket._Cast_Socket") -> "_2301.ShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.ShaftSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2307.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2307

            return self._parent._cast(_2307.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2309.BevelDifferentialGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2309

            return self._parent._cast(_2309.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2311.BevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2311

            return self._parent._cast(_2311.BevelGearTeethSocket)

        @property
        def concept_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2313.ConceptGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2313

            return self._parent._cast(_2313.ConceptGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2315.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2315

            return self._parent._cast(_2315.ConicalGearTeethSocket)

        @property
        def cylindrical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2317.CylindricalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.CylindricalGearTeethSocket)

        @property
        def face_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2319.FaceGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.FaceGearTeethSocket)

        @property
        def gear_teeth_socket(self: "Socket._Cast_Socket") -> "_2321.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.GearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2323.HypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2324.KlingelnbergConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2328.KlingelnbergHypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2329.KlingelnbergSpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2331.SpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2333.StraightBevelDiffGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2335.StraightBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2335

            return self._parent._cast(_2335.StraightBevelGearTeethSocket)

        @property
        def worm_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2337.WormGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2337

            return self._parent._cast(_2337.WormGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2339.ZerolBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2339

            return self._parent._cast(_2339.ZerolBevelGearTeethSocket)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2340.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2340

            return self._parent._cast(_2340.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2341.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2341

            return self._parent._cast(_2341.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2343.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2343

            return self._parent._cast(_2343.CycloidalDiscInnerSocket)

        @property
        def cycloidal_disc_outer_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2344.CycloidalDiscOuterSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2344

            return self._parent._cast(_2344.CycloidalDiscOuterSocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2346.CycloidalDiscPlanetaryBearingSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2346

            return self._parent._cast(_2346.CycloidalDiscPlanetaryBearingSocket)

        @property
        def ring_pins_socket(self: "Socket._Cast_Socket") -> "_2347.RingPinsSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2347

            return self._parent._cast(_2347.RingPinsSocket)

        @property
        def clutch_socket(self: "Socket._Cast_Socket") -> "_2350.ClutchSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2350

            return self._parent._cast(_2350.ClutchSocket)

        @property
        def concept_coupling_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2352.ConceptCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2352

            return self._parent._cast(_2352.ConceptCouplingSocket)

        @property
        def coupling_socket(self: "Socket._Cast_Socket") -> "_2354.CouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2354

            return self._parent._cast(_2354.CouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2356.PartToPartShearCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2356

            return self._parent._cast(_2356.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2358.SpringDamperSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2358

            return self._parent._cast(_2358.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2360.TorqueConverterPumpSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2360

            return self._parent._cast(_2360.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2361.TorqueConverterTurbineSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2361

            return self._parent._cast(_2361.TorqueConverterTurbineSocket)

        @property
        def socket(self: "Socket._Cast_Socket") -> "Socket":
            return self._parent

        def __getattr__(self: "Socket._Cast_Socket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Socket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def connected_components(self: Self) -> "List[_2451.Component]":
        """List[mastapy.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connections(self: Self) -> "List[_2279.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def owner(self: Self) -> "_2451.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Owner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def connect_to(
        self: Self, component: "_2451.Component"
    ) -> "_2452.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connect_to_socket(
        self: Self, socket: "Socket"
    ) -> "_2452.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connection_to(self: Self, socket: "Socket") -> "_2279.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectionTo(socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def get_possible_sockets_to_connect_to(
        self: Self, component_to_connect_to: "_2451.Component"
    ) -> "List[Socket]":
        """List[mastapy.system_model.connections_and_sockets.Socket]

        Args:
            component_to_connect_to (mastapy.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetPossibleSocketsToConnectTo(
                component_to_connect_to.wrapped if component_to_connect_to else None
            )
        )

    @property
    def cast_to(self: Self) -> "Socket._Cast_Socket":
        return self._Cast_Socket(self)
