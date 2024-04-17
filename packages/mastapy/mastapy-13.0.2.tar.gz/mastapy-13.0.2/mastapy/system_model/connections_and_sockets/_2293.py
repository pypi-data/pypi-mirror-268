"""OuterShaftSocketBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_SHAFT_SOCKET_BASE = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "OuterShaftSocketBase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2292, _2283, _2303
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341


__docformat__ = "restructuredtext en"
__all__ = ("OuterShaftSocketBase",)


Self = TypeVar("Self", bound="OuterShaftSocketBase")


class OuterShaftSocketBase(_2301.ShaftSocket):
    """OuterShaftSocketBase

    This is a mastapy class.
    """

    TYPE = _OUTER_SHAFT_SOCKET_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OuterShaftSocketBase")

    class _Cast_OuterShaftSocketBase:
        """Special nested class for casting OuterShaftSocketBase to subclasses."""

        def __init__(
            self: "OuterShaftSocketBase._Cast_OuterShaftSocketBase",
            parent: "OuterShaftSocketBase",
        ):
            self._parent = parent

        @property
        def shaft_socket(
            self: "OuterShaftSocketBase._Cast_OuterShaftSocketBase",
        ) -> "_2301.ShaftSocket":
            return self._parent._cast(_2301.ShaftSocket)

        @property
        def cylindrical_socket(
            self: "OuterShaftSocketBase._Cast_OuterShaftSocketBase",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "OuterShaftSocketBase._Cast_OuterShaftSocketBase",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def outer_shaft_socket(
            self: "OuterShaftSocketBase._Cast_OuterShaftSocketBase",
        ) -> "_2292.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.OuterShaftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "OuterShaftSocketBase._Cast_OuterShaftSocketBase",
        ) -> "_2341.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2341

            return self._parent._cast(_2341.CycloidalDiscAxialRightSocket)

        @property
        def outer_shaft_socket_base(
            self: "OuterShaftSocketBase._Cast_OuterShaftSocketBase",
        ) -> "OuterShaftSocketBase":
            return self._parent

        def __getattr__(
            self: "OuterShaftSocketBase._Cast_OuterShaftSocketBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OuterShaftSocketBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "OuterShaftSocketBase._Cast_OuterShaftSocketBase":
        return self._Cast_OuterShaftSocketBase(self)
