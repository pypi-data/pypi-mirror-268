"""RollingRingSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "RollingRingSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2303


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingSocket",)


Self = TypeVar("Self", bound="RollingRingSocket")


class RollingRingSocket(_2283.CylindricalSocket):
    """RollingRingSocket

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingSocket")

    class _Cast_RollingRingSocket:
        """Special nested class for casting RollingRingSocket to subclasses."""

        def __init__(
            self: "RollingRingSocket._Cast_RollingRingSocket",
            parent: "RollingRingSocket",
        ):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "RollingRingSocket._Cast_RollingRingSocket",
        ) -> "_2283.CylindricalSocket":
            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(self: "RollingRingSocket._Cast_RollingRingSocket") -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def rolling_ring_socket(
            self: "RollingRingSocket._Cast_RollingRingSocket",
        ) -> "RollingRingSocket":
            return self._parent

        def __getattr__(self: "RollingRingSocket._Cast_RollingRingSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RollingRingSocket._Cast_RollingRingSocket":
        return self._Cast_RollingRingSocket(self)
