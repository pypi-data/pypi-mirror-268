"""OuterShaftSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2293
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_SHAFT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "OuterShaftSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2301, _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("OuterShaftSocket",)


Self = TypeVar("Self", bound="OuterShaftSocket")


class OuterShaftSocket(_2293.OuterShaftSocketBase):
    """OuterShaftSocket

    This is a mastapy class.
    """

    TYPE = _OUTER_SHAFT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OuterShaftSocket")

    class _Cast_OuterShaftSocket:
        """Special nested class for casting OuterShaftSocket to subclasses."""

        def __init__(
            self: "OuterShaftSocket._Cast_OuterShaftSocket", parent: "OuterShaftSocket"
        ):
            self._parent = parent

        @property
        def outer_shaft_socket_base(
            self: "OuterShaftSocket._Cast_OuterShaftSocket",
        ) -> "_2293.OuterShaftSocketBase":
            return self._parent._cast(_2293.OuterShaftSocketBase)

        @property
        def shaft_socket(
            self: "OuterShaftSocket._Cast_OuterShaftSocket",
        ) -> "_2301.ShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.ShaftSocket)

        @property
        def cylindrical_socket(
            self: "OuterShaftSocket._Cast_OuterShaftSocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(self: "OuterShaftSocket._Cast_OuterShaftSocket") -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def outer_shaft_socket(
            self: "OuterShaftSocket._Cast_OuterShaftSocket",
        ) -> "OuterShaftSocket":
            return self._parent

        def __getattr__(self: "OuterShaftSocket._Cast_OuterShaftSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OuterShaftSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "OuterShaftSocket._Cast_OuterShaftSocket":
        return self._Cast_OuterShaftSocket(self)
