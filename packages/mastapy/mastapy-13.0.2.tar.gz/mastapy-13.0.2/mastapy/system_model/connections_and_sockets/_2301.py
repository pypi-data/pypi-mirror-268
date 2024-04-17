"""ShaftSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "ShaftSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import (
        _2286,
        _2287,
        _2292,
        _2293,
        _2303,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2340,
        _2341,
        _2343,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSocket",)


Self = TypeVar("Self", bound="ShaftSocket")


class ShaftSocket(_2283.CylindricalSocket):
    """ShaftSocket

    This is a mastapy class.
    """

    TYPE = _SHAFT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSocket")

    class _Cast_ShaftSocket:
        """Special nested class for casting ShaftSocket to subclasses."""

        def __init__(self: "ShaftSocket._Cast_ShaftSocket", parent: "ShaftSocket"):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2283.CylindricalSocket":
            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(self: "ShaftSocket._Cast_ShaftSocket") -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def inner_shaft_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2286.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2286

            return self._parent._cast(_2286.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2287.InnerShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2287

            return self._parent._cast(_2287.InnerShaftSocketBase)

        @property
        def outer_shaft_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2292.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2293.OuterShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.OuterShaftSocketBase)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2340.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2340

            return self._parent._cast(_2340.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2341.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2341

            return self._parent._cast(_2341.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2343.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2343

            return self._parent._cast(_2343.CycloidalDiscInnerSocket)

        @property
        def shaft_socket(self: "ShaftSocket._Cast_ShaftSocket") -> "ShaftSocket":
            return self._parent

        def __getattr__(self: "ShaftSocket._Cast_ShaftSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftSocket._Cast_ShaftSocket":
        return self._Cast_ShaftSocket(self)
