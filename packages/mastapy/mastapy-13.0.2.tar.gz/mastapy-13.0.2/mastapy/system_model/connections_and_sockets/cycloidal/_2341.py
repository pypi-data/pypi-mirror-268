"""CycloidalDiscAxialRightSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2293
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_AXIAL_RIGHT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscAxialRightSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2301, _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscAxialRightSocket",)


Self = TypeVar("Self", bound="CycloidalDiscAxialRightSocket")


class CycloidalDiscAxialRightSocket(_2293.OuterShaftSocketBase):
    """CycloidalDiscAxialRightSocket

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_AXIAL_RIGHT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscAxialRightSocket")

    class _Cast_CycloidalDiscAxialRightSocket:
        """Special nested class for casting CycloidalDiscAxialRightSocket to subclasses."""

        def __init__(
            self: "CycloidalDiscAxialRightSocket._Cast_CycloidalDiscAxialRightSocket",
            parent: "CycloidalDiscAxialRightSocket",
        ):
            self._parent = parent

        @property
        def outer_shaft_socket_base(
            self: "CycloidalDiscAxialRightSocket._Cast_CycloidalDiscAxialRightSocket",
        ) -> "_2293.OuterShaftSocketBase":
            return self._parent._cast(_2293.OuterShaftSocketBase)

        @property
        def shaft_socket(
            self: "CycloidalDiscAxialRightSocket._Cast_CycloidalDiscAxialRightSocket",
        ) -> "_2301.ShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.ShaftSocket)

        @property
        def cylindrical_socket(
            self: "CycloidalDiscAxialRightSocket._Cast_CycloidalDiscAxialRightSocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "CycloidalDiscAxialRightSocket._Cast_CycloidalDiscAxialRightSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "CycloidalDiscAxialRightSocket._Cast_CycloidalDiscAxialRightSocket",
        ) -> "CycloidalDiscAxialRightSocket":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscAxialRightSocket._Cast_CycloidalDiscAxialRightSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscAxialRightSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscAxialRightSocket._Cast_CycloidalDiscAxialRightSocket":
        return self._Cast_CycloidalDiscAxialRightSocket(self)
