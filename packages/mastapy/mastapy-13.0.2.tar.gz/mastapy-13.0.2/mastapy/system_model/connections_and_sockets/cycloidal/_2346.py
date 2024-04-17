"""CycloidalDiscPlanetaryBearingSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.connections_and_sockets import _2296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscPlanetaryBearingSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingSocket",)


Self = TypeVar("Self", bound="CycloidalDiscPlanetaryBearingSocket")


class CycloidalDiscPlanetaryBearingSocket(_2296.PlanetarySocketBase):
    """CycloidalDiscPlanetaryBearingSocket

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscPlanetaryBearingSocket")

    class _Cast_CycloidalDiscPlanetaryBearingSocket:
        """Special nested class for casting CycloidalDiscPlanetaryBearingSocket to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingSocket._Cast_CycloidalDiscPlanetaryBearingSocket",
            parent: "CycloidalDiscPlanetaryBearingSocket",
        ):
            self._parent = parent

        @property
        def planetary_socket_base(
            self: "CycloidalDiscPlanetaryBearingSocket._Cast_CycloidalDiscPlanetaryBearingSocket",
        ) -> "_2296.PlanetarySocketBase":
            return self._parent._cast(_2296.PlanetarySocketBase)

        @property
        def cylindrical_socket(
            self: "CycloidalDiscPlanetaryBearingSocket._Cast_CycloidalDiscPlanetaryBearingSocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "CycloidalDiscPlanetaryBearingSocket._Cast_CycloidalDiscPlanetaryBearingSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def cycloidal_disc_planetary_bearing_socket(
            self: "CycloidalDiscPlanetaryBearingSocket._Cast_CycloidalDiscPlanetaryBearingSocket",
        ) -> "CycloidalDiscPlanetaryBearingSocket":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingSocket._Cast_CycloidalDiscPlanetaryBearingSocket",
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
        self: Self, instance_to_wrap: "CycloidalDiscPlanetaryBearingSocket.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_for_eccentric_bearing(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsForEccentricBearing

        if temp is None:
            return False

        return temp

    @is_for_eccentric_bearing.setter
    @enforce_parameter_types
    def is_for_eccentric_bearing(self: Self, value: "bool"):
        self.wrapped.IsForEccentricBearing = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CycloidalDiscPlanetaryBearingSocket._Cast_CycloidalDiscPlanetaryBearingSocket"
    ):
        return self._Cast_CycloidalDiscPlanetaryBearingSocket(self)
