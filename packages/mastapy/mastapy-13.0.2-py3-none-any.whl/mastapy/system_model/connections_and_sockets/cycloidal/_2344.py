"""CycloidalDiscOuterSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_OUTER_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscOuterSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2303


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscOuterSocket",)


Self = TypeVar("Self", bound="CycloidalDiscOuterSocket")


class CycloidalDiscOuterSocket(_2283.CylindricalSocket):
    """CycloidalDiscOuterSocket

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_OUTER_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscOuterSocket")

    class _Cast_CycloidalDiscOuterSocket:
        """Special nested class for casting CycloidalDiscOuterSocket to subclasses."""

        def __init__(
            self: "CycloidalDiscOuterSocket._Cast_CycloidalDiscOuterSocket",
            parent: "CycloidalDiscOuterSocket",
        ):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "CycloidalDiscOuterSocket._Cast_CycloidalDiscOuterSocket",
        ) -> "_2283.CylindricalSocket":
            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "CycloidalDiscOuterSocket._Cast_CycloidalDiscOuterSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def cycloidal_disc_outer_socket(
            self: "CycloidalDiscOuterSocket._Cast_CycloidalDiscOuterSocket",
        ) -> "CycloidalDiscOuterSocket":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscOuterSocket._Cast_CycloidalDiscOuterSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscOuterSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscOuterSocket._Cast_CycloidalDiscOuterSocket":
        return self._Cast_CycloidalDiscOuterSocket(self)
