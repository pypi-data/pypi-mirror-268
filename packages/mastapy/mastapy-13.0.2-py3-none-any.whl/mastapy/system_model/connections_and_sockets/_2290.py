"""MountableComponentOuterSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2291
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_OUTER_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "MountableComponentOuterSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2274, _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentOuterSocket",)


Self = TypeVar("Self", bound="MountableComponentOuterSocket")


class MountableComponentOuterSocket(_2291.MountableComponentSocket):
    """MountableComponentOuterSocket

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_OUTER_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentOuterSocket")

    class _Cast_MountableComponentOuterSocket:
        """Special nested class for casting MountableComponentOuterSocket to subclasses."""

        def __init__(
            self: "MountableComponentOuterSocket._Cast_MountableComponentOuterSocket",
            parent: "MountableComponentOuterSocket",
        ):
            self._parent = parent

        @property
        def mountable_component_socket(
            self: "MountableComponentOuterSocket._Cast_MountableComponentOuterSocket",
        ) -> "_2291.MountableComponentSocket":
            return self._parent._cast(_2291.MountableComponentSocket)

        @property
        def cylindrical_socket(
            self: "MountableComponentOuterSocket._Cast_MountableComponentOuterSocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "MountableComponentOuterSocket._Cast_MountableComponentOuterSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def bearing_outer_socket(
            self: "MountableComponentOuterSocket._Cast_MountableComponentOuterSocket",
        ) -> "_2274.BearingOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.BearingOuterSocket)

        @property
        def mountable_component_outer_socket(
            self: "MountableComponentOuterSocket._Cast_MountableComponentOuterSocket",
        ) -> "MountableComponentOuterSocket":
            return self._parent

        def __getattr__(
            self: "MountableComponentOuterSocket._Cast_MountableComponentOuterSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentOuterSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentOuterSocket._Cast_MountableComponentOuterSocket":
        return self._Cast_MountableComponentOuterSocket(self)
