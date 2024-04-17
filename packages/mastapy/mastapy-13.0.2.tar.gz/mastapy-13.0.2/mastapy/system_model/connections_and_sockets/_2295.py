"""PlanetarySocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "PlanetarySocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("PlanetarySocket",)


Self = TypeVar("Self", bound="PlanetarySocket")


class PlanetarySocket(_2296.PlanetarySocketBase):
    """PlanetarySocket

    This is a mastapy class.
    """

    TYPE = _PLANETARY_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetarySocket")

    class _Cast_PlanetarySocket:
        """Special nested class for casting PlanetarySocket to subclasses."""

        def __init__(
            self: "PlanetarySocket._Cast_PlanetarySocket", parent: "PlanetarySocket"
        ):
            self._parent = parent

        @property
        def planetary_socket_base(
            self: "PlanetarySocket._Cast_PlanetarySocket",
        ) -> "_2296.PlanetarySocketBase":
            return self._parent._cast(_2296.PlanetarySocketBase)

        @property
        def cylindrical_socket(
            self: "PlanetarySocket._Cast_PlanetarySocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(self: "PlanetarySocket._Cast_PlanetarySocket") -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def planetary_socket(
            self: "PlanetarySocket._Cast_PlanetarySocket",
        ) -> "PlanetarySocket":
            return self._parent

        def __getattr__(self: "PlanetarySocket._Cast_PlanetarySocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetarySocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planet_tip_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetTipClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "PlanetarySocket._Cast_PlanetarySocket":
        return self._Cast_PlanetarySocket(self)
