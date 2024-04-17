"""CylindricalSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2303
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CylindricalSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import (
        _2273,
        _2274,
        _2281,
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
    from mastapy.system_model.connections_and_sockets.gears import _2317
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
__all__ = ("CylindricalSocket",)


Self = TypeVar("Self", bound="CylindricalSocket")


class CylindricalSocket(_2303.Socket):
    """CylindricalSocket

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalSocket")

    class _Cast_CylindricalSocket:
        """Special nested class for casting CylindricalSocket to subclasses."""

        def __init__(
            self: "CylindricalSocket._Cast_CylindricalSocket",
            parent: "CylindricalSocket",
        ):
            self._parent = parent

        @property
        def socket(self: "CylindricalSocket._Cast_CylindricalSocket") -> "_2303.Socket":
            return self._parent._cast(_2303.Socket)

        @property
        def bearing_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2273.BearingInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2273

            return self._parent._cast(_2273.BearingInnerSocket)

        @property
        def bearing_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2274.BearingOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.BearingOuterSocket)

        @property
        def cvt_pulley_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2281.CVTPulleySocket":
            from mastapy.system_model.connections_and_sockets import _2281

            return self._parent._cast(_2281.CVTPulleySocket)

        @property
        def inner_shaft_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2286.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2286

            return self._parent._cast(_2286.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2287.InnerShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2287

            return self._parent._cast(_2287.InnerShaftSocketBase)

        @property
        def mountable_component_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2289.MountableComponentInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2289

            return self._parent._cast(_2289.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2290.MountableComponentOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2291.MountableComponentSocket":
            from mastapy.system_model.connections_and_sockets import _2291

            return self._parent._cast(_2291.MountableComponentSocket)

        @property
        def outer_shaft_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2292.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2293.OuterShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.OuterShaftSocketBase)

        @property
        def planetary_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2295.PlanetarySocket":
            from mastapy.system_model.connections_and_sockets import _2295

            return self._parent._cast(_2295.PlanetarySocket)

        @property
        def planetary_socket_base(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2296.PlanetarySocketBase":
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.PlanetarySocketBase)

        @property
        def pulley_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2297.PulleySocket":
            from mastapy.system_model.connections_and_sockets import _2297

            return self._parent._cast(_2297.PulleySocket)

        @property
        def rolling_ring_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2300.RollingRingSocket":
            from mastapy.system_model.connections_and_sockets import _2300

            return self._parent._cast(_2300.RollingRingSocket)

        @property
        def shaft_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2301.ShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.ShaftSocket)

        @property
        def cylindrical_gear_teeth_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2317.CylindricalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.CylindricalGearTeethSocket)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2340.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2340

            return self._parent._cast(_2340.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2341.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2341

            return self._parent._cast(_2341.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2343.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2343

            return self._parent._cast(_2343.CycloidalDiscInnerSocket)

        @property
        def cycloidal_disc_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2344.CycloidalDiscOuterSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2344

            return self._parent._cast(_2344.CycloidalDiscOuterSocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2346.CycloidalDiscPlanetaryBearingSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2346

            return self._parent._cast(_2346.CycloidalDiscPlanetaryBearingSocket)

        @property
        def ring_pins_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2347.RingPinsSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2347

            return self._parent._cast(_2347.RingPinsSocket)

        @property
        def clutch_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2350.ClutchSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2350

            return self._parent._cast(_2350.ClutchSocket)

        @property
        def concept_coupling_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2352.ConceptCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2352

            return self._parent._cast(_2352.ConceptCouplingSocket)

        @property
        def coupling_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2354.CouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2354

            return self._parent._cast(_2354.CouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2356.PartToPartShearCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2356

            return self._parent._cast(_2356.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2358.SpringDamperSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2358

            return self._parent._cast(_2358.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2360.TorqueConverterPumpSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2360

            return self._parent._cast(_2360.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2361.TorqueConverterTurbineSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2361

            return self._parent._cast(_2361.TorqueConverterTurbineSocket)

        @property
        def cylindrical_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "CylindricalSocket":
            return self._parent

        def __getattr__(self: "CylindricalSocket._Cast_CylindricalSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CylindricalSocket._Cast_CylindricalSocket":
        return self._Cast_CylindricalSocket(self)
