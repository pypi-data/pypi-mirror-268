"""CycloidalDiscInnerSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2287
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_INNER_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscInnerSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2301, _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscInnerSocket",)


Self = TypeVar("Self", bound="CycloidalDiscInnerSocket")


class CycloidalDiscInnerSocket(_2287.InnerShaftSocketBase):
    """CycloidalDiscInnerSocket

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_INNER_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscInnerSocket")

    class _Cast_CycloidalDiscInnerSocket:
        """Special nested class for casting CycloidalDiscInnerSocket to subclasses."""

        def __init__(
            self: "CycloidalDiscInnerSocket._Cast_CycloidalDiscInnerSocket",
            parent: "CycloidalDiscInnerSocket",
        ):
            self._parent = parent

        @property
        def inner_shaft_socket_base(
            self: "CycloidalDiscInnerSocket._Cast_CycloidalDiscInnerSocket",
        ) -> "_2287.InnerShaftSocketBase":
            return self._parent._cast(_2287.InnerShaftSocketBase)

        @property
        def shaft_socket(
            self: "CycloidalDiscInnerSocket._Cast_CycloidalDiscInnerSocket",
        ) -> "_2301.ShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.ShaftSocket)

        @property
        def cylindrical_socket(
            self: "CycloidalDiscInnerSocket._Cast_CycloidalDiscInnerSocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "CycloidalDiscInnerSocket._Cast_CycloidalDiscInnerSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def cycloidal_disc_inner_socket(
            self: "CycloidalDiscInnerSocket._Cast_CycloidalDiscInnerSocket",
        ) -> "CycloidalDiscInnerSocket":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscInnerSocket._Cast_CycloidalDiscInnerSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscInnerSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscInnerSocket._Cast_CycloidalDiscInnerSocket":
        return self._Cast_CycloidalDiscInnerSocket(self)
