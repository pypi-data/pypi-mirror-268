"""FaceGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2321
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "FaceGearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2303


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearTeethSocket",)


Self = TypeVar("Self", bound="FaceGearTeethSocket")


class FaceGearTeethSocket(_2321.GearTeethSocket):
    """FaceGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearTeethSocket")

    class _Cast_FaceGearTeethSocket:
        """Special nested class for casting FaceGearTeethSocket to subclasses."""

        def __init__(
            self: "FaceGearTeethSocket._Cast_FaceGearTeethSocket",
            parent: "FaceGearTeethSocket",
        ):
            self._parent = parent

        @property
        def gear_teeth_socket(
            self: "FaceGearTeethSocket._Cast_FaceGearTeethSocket",
        ) -> "_2321.GearTeethSocket":
            return self._parent._cast(_2321.GearTeethSocket)

        @property
        def socket(
            self: "FaceGearTeethSocket._Cast_FaceGearTeethSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def face_gear_teeth_socket(
            self: "FaceGearTeethSocket._Cast_FaceGearTeethSocket",
        ) -> "FaceGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "FaceGearTeethSocket._Cast_FaceGearTeethSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FaceGearTeethSocket._Cast_FaceGearTeethSocket":
        return self._Cast_FaceGearTeethSocket(self)
