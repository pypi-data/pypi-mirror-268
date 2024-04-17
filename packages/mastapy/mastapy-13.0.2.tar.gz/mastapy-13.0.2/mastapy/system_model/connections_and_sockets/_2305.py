"""SocketConnectionSelection"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SOCKET_CONNECTION_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "SocketConnectionSelection"
)


__docformat__ = "restructuredtext en"
__all__ = ("SocketConnectionSelection",)


Self = TypeVar("Self", bound="SocketConnectionSelection")


class SocketConnectionSelection(_0.APIBase):
    """SocketConnectionSelection

    This is a mastapy class.
    """

    TYPE = _SOCKET_CONNECTION_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SocketConnectionSelection")

    class _Cast_SocketConnectionSelection:
        """Special nested class for casting SocketConnectionSelection to subclasses."""

        def __init__(
            self: "SocketConnectionSelection._Cast_SocketConnectionSelection",
            parent: "SocketConnectionSelection",
        ):
            self._parent = parent

        @property
        def socket_connection_selection(
            self: "SocketConnectionSelection._Cast_SocketConnectionSelection",
        ) -> "SocketConnectionSelection":
            return self._parent

        def __getattr__(
            self: "SocketConnectionSelection._Cast_SocketConnectionSelection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SocketConnectionSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    def select(self: Self):
        """Method does not return."""
        self.wrapped.Select()

    @property
    def cast_to(
        self: Self,
    ) -> "SocketConnectionSelection._Cast_SocketConnectionSelection":
        return self._Cast_SocketConnectionSelection(self)
