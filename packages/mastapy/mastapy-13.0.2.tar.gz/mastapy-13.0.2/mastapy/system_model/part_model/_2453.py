"""ConnectedSockets"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTED_SOCKETS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "ConnectedSockets"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279, _2303


__docformat__ = "restructuredtext en"
__all__ = ("ConnectedSockets",)


Self = TypeVar("Self", bound="ConnectedSockets")


class ConnectedSockets(_0.APIBase):
    """ConnectedSockets

    This is a mastapy class.
    """

    TYPE = _CONNECTED_SOCKETS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectedSockets")

    class _Cast_ConnectedSockets:
        """Special nested class for casting ConnectedSockets to subclasses."""

        def __init__(
            self: "ConnectedSockets._Cast_ConnectedSockets", parent: "ConnectedSockets"
        ):
            self._parent = parent

        @property
        def connected_sockets(
            self: "ConnectedSockets._Cast_ConnectedSockets",
        ) -> "ConnectedSockets":
            return self._parent

        def __getattr__(self: "ConnectedSockets._Cast_ConnectedSockets", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectedSockets.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection(self: Self) -> "_2279.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket_a(self: Self) -> "_2303.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket_b(self: Self) -> "_2303.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectedSockets._Cast_ConnectedSockets":
        return self._Cast_ConnectedSockets(self)
