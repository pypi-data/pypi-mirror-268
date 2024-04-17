"""HypoidGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2307
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "HypoidGearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2315, _2321
    from mastapy.system_model.connections_and_sockets import _2303


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearTeethSocket",)


Self = TypeVar("Self", bound="HypoidGearTeethSocket")


class HypoidGearTeethSocket(_2307.AGMAGleasonConicalGearTeethSocket):
    """HypoidGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearTeethSocket")

    class _Cast_HypoidGearTeethSocket:
        """Special nested class for casting HypoidGearTeethSocket to subclasses."""

        def __init__(
            self: "HypoidGearTeethSocket._Cast_HypoidGearTeethSocket",
            parent: "HypoidGearTeethSocket",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "HypoidGearTeethSocket._Cast_HypoidGearTeethSocket",
        ) -> "_2307.AGMAGleasonConicalGearTeethSocket":
            return self._parent._cast(_2307.AGMAGleasonConicalGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "HypoidGearTeethSocket._Cast_HypoidGearTeethSocket",
        ) -> "_2315.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2315

            return self._parent._cast(_2315.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "HypoidGearTeethSocket._Cast_HypoidGearTeethSocket",
        ) -> "_2321.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.GearTeethSocket)

        @property
        def socket(
            self: "HypoidGearTeethSocket._Cast_HypoidGearTeethSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def hypoid_gear_teeth_socket(
            self: "HypoidGearTeethSocket._Cast_HypoidGearTeethSocket",
        ) -> "HypoidGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "HypoidGearTeethSocket._Cast_HypoidGearTeethSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "HypoidGearTeethSocket._Cast_HypoidGearTeethSocket":
        return self._Cast_HypoidGearTeethSocket(self)
