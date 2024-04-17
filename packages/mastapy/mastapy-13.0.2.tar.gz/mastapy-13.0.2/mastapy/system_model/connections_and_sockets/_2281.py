"""CVTPulleySocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2297
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CVTPulleySocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleySocket",)


Self = TypeVar("Self", bound="CVTPulleySocket")


class CVTPulleySocket(_2297.PulleySocket):
    """CVTPulleySocket

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleySocket")

    class _Cast_CVTPulleySocket:
        """Special nested class for casting CVTPulleySocket to subclasses."""

        def __init__(
            self: "CVTPulleySocket._Cast_CVTPulleySocket", parent: "CVTPulleySocket"
        ):
            self._parent = parent

        @property
        def pulley_socket(
            self: "CVTPulleySocket._Cast_CVTPulleySocket",
        ) -> "_2297.PulleySocket":
            return self._parent._cast(_2297.PulleySocket)

        @property
        def cylindrical_socket(
            self: "CVTPulleySocket._Cast_CVTPulleySocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(self: "CVTPulleySocket._Cast_CVTPulleySocket") -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def cvt_pulley_socket(
            self: "CVTPulleySocket._Cast_CVTPulleySocket",
        ) -> "CVTPulleySocket":
            return self._parent

        def __getattr__(self: "CVTPulleySocket._Cast_CVTPulleySocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleySocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CVTPulleySocket._Cast_CVTPulleySocket":
        return self._Cast_CVTPulleySocket(self)
