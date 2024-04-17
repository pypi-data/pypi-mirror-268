"""WormGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2321
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "WormGearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2303


__docformat__ = "restructuredtext en"
__all__ = ("WormGearTeethSocket",)


Self = TypeVar("Self", bound="WormGearTeethSocket")


class WormGearTeethSocket(_2321.GearTeethSocket):
    """WormGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearTeethSocket")

    class _Cast_WormGearTeethSocket:
        """Special nested class for casting WormGearTeethSocket to subclasses."""

        def __init__(
            self: "WormGearTeethSocket._Cast_WormGearTeethSocket",
            parent: "WormGearTeethSocket",
        ):
            self._parent = parent

        @property
        def gear_teeth_socket(
            self: "WormGearTeethSocket._Cast_WormGearTeethSocket",
        ) -> "_2321.GearTeethSocket":
            return self._parent._cast(_2321.GearTeethSocket)

        @property
        def socket(
            self: "WormGearTeethSocket._Cast_WormGearTeethSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def worm_gear_teeth_socket(
            self: "WormGearTeethSocket._Cast_WormGearTeethSocket",
        ) -> "WormGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "WormGearTeethSocket._Cast_WormGearTeethSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "WormGearTeethSocket._Cast_WormGearTeethSocket":
        return self._Cast_WormGearTeethSocket(self)
