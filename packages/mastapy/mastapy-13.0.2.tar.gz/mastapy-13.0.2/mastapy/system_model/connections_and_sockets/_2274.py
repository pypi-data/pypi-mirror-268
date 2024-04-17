"""BearingOuterSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2290
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_OUTER_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "BearingOuterSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2291, _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("BearingOuterSocket",)


Self = TypeVar("Self", bound="BearingOuterSocket")


class BearingOuterSocket(_2290.MountableComponentOuterSocket):
    """BearingOuterSocket

    This is a mastapy class.
    """

    TYPE = _BEARING_OUTER_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingOuterSocket")

    class _Cast_BearingOuterSocket:
        """Special nested class for casting BearingOuterSocket to subclasses."""

        def __init__(
            self: "BearingOuterSocket._Cast_BearingOuterSocket",
            parent: "BearingOuterSocket",
        ):
            self._parent = parent

        @property
        def mountable_component_outer_socket(
            self: "BearingOuterSocket._Cast_BearingOuterSocket",
        ) -> "_2290.MountableComponentOuterSocket":
            return self._parent._cast(_2290.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(
            self: "BearingOuterSocket._Cast_BearingOuterSocket",
        ) -> "_2291.MountableComponentSocket":
            from mastapy.system_model.connections_and_sockets import _2291

            return self._parent._cast(_2291.MountableComponentSocket)

        @property
        def cylindrical_socket(
            self: "BearingOuterSocket._Cast_BearingOuterSocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "BearingOuterSocket._Cast_BearingOuterSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def bearing_outer_socket(
            self: "BearingOuterSocket._Cast_BearingOuterSocket",
        ) -> "BearingOuterSocket":
            return self._parent

        def __getattr__(self: "BearingOuterSocket._Cast_BearingOuterSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingOuterSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BearingOuterSocket._Cast_BearingOuterSocket":
        return self._Cast_BearingOuterSocket(self)
