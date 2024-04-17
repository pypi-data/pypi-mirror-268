"""SpringDamperSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.couplings import _2354
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperSocket",)


Self = TypeVar("Self", bound="SpringDamperSocket")


class SpringDamperSocket(_2354.CouplingSocket):
    """SpringDamperSocket

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperSocket")

    class _Cast_SpringDamperSocket:
        """Special nested class for casting SpringDamperSocket to subclasses."""

        def __init__(
            self: "SpringDamperSocket._Cast_SpringDamperSocket",
            parent: "SpringDamperSocket",
        ):
            self._parent = parent

        @property
        def coupling_socket(
            self: "SpringDamperSocket._Cast_SpringDamperSocket",
        ) -> "_2354.CouplingSocket":
            return self._parent._cast(_2354.CouplingSocket)

        @property
        def cylindrical_socket(
            self: "SpringDamperSocket._Cast_SpringDamperSocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "SpringDamperSocket._Cast_SpringDamperSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def spring_damper_socket(
            self: "SpringDamperSocket._Cast_SpringDamperSocket",
        ) -> "SpringDamperSocket":
            return self._parent

        def __getattr__(self: "SpringDamperSocket._Cast_SpringDamperSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SpringDamperSocket._Cast_SpringDamperSocket":
        return self._Cast_SpringDamperSocket(self)
