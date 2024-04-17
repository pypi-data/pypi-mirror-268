"""ElectricMachineStatorSocket"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2303
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "ElectricMachineStatorSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineStatorSocket",)


Self = TypeVar("Self", bound="ElectricMachineStatorSocket")


class ElectricMachineStatorSocket(_2303.Socket):
    """ElectricMachineStatorSocket

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineStatorSocket")

    class _Cast_ElectricMachineStatorSocket:
        """Special nested class for casting ElectricMachineStatorSocket to subclasses."""

        def __init__(
            self: "ElectricMachineStatorSocket._Cast_ElectricMachineStatorSocket",
            parent: "ElectricMachineStatorSocket",
        ):
            self._parent = parent

        @property
        def socket(
            self: "ElectricMachineStatorSocket._Cast_ElectricMachineStatorSocket",
        ) -> "_2303.Socket":
            return self._parent._cast(_2303.Socket)

        @property
        def electric_machine_stator_socket(
            self: "ElectricMachineStatorSocket._Cast_ElectricMachineStatorSocket",
        ) -> "ElectricMachineStatorSocket":
            return self._parent

        def __getattr__(
            self: "ElectricMachineStatorSocket._Cast_ElectricMachineStatorSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineStatorSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineStatorSocket._Cast_ElectricMachineStatorSocket":
        return self._Cast_ElectricMachineStatorSocket(self)
