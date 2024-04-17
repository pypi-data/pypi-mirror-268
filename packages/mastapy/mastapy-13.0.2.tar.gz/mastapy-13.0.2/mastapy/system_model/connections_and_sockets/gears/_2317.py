"""CylindricalGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "CylindricalGearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2303


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearTeethSocket",)


Self = TypeVar("Self", bound="CylindricalGearTeethSocket")


class CylindricalGearTeethSocket(_2283.CylindricalSocket):
    """CylindricalGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearTeethSocket")

    class _Cast_CylindricalGearTeethSocket:
        """Special nested class for casting CylindricalGearTeethSocket to subclasses."""

        def __init__(
            self: "CylindricalGearTeethSocket._Cast_CylindricalGearTeethSocket",
            parent: "CylindricalGearTeethSocket",
        ):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "CylindricalGearTeethSocket._Cast_CylindricalGearTeethSocket",
        ) -> "_2283.CylindricalSocket":
            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "CylindricalGearTeethSocket._Cast_CylindricalGearTeethSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def cylindrical_gear_teeth_socket(
            self: "CylindricalGearTeethSocket._Cast_CylindricalGearTeethSocket",
        ) -> "CylindricalGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "CylindricalGearTeethSocket._Cast_CylindricalGearTeethSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearTeethSocket._Cast_CylindricalGearTeethSocket":
        return self._Cast_CylindricalGearTeethSocket(self)
