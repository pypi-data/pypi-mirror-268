"""RollingRingConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2288
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "RollingRingConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnection",)


Self = TypeVar("Self", bound="RollingRingConnection")


class RollingRingConnection(_2288.InterMountableComponentConnection):
    """RollingRingConnection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingConnection")

    class _Cast_RollingRingConnection:
        """Special nested class for casting RollingRingConnection to subclasses."""

        def __init__(
            self: "RollingRingConnection._Cast_RollingRingConnection",
            parent: "RollingRingConnection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection(
            self: "RollingRingConnection._Cast_RollingRingConnection",
        ) -> "_2288.InterMountableComponentConnection":
            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(
            self: "RollingRingConnection._Cast_RollingRingConnection",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "RollingRingConnection._Cast_RollingRingConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def rolling_ring_connection(
            self: "RollingRingConnection._Cast_RollingRingConnection",
        ) -> "RollingRingConnection":
            return self._parent

        def __getattr__(
            self: "RollingRingConnection._Cast_RollingRingConnection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RollingRingConnection._Cast_RollingRingConnection":
        return self._Cast_RollingRingConnection(self)
