"""TorqueConverterPumpSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.couplings import _2354
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "TorqueConverterPumpSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpSocket",)


Self = TypeVar("Self", bound="TorqueConverterPumpSocket")


class TorqueConverterPumpSocket(_2354.CouplingSocket):
    """TorqueConverterPumpSocket

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterPumpSocket")

    class _Cast_TorqueConverterPumpSocket:
        """Special nested class for casting TorqueConverterPumpSocket to subclasses."""

        def __init__(
            self: "TorqueConverterPumpSocket._Cast_TorqueConverterPumpSocket",
            parent: "TorqueConverterPumpSocket",
        ):
            self._parent = parent

        @property
        def coupling_socket(
            self: "TorqueConverterPumpSocket._Cast_TorqueConverterPumpSocket",
        ) -> "_2354.CouplingSocket":
            return self._parent._cast(_2354.CouplingSocket)

        @property
        def cylindrical_socket(
            self: "TorqueConverterPumpSocket._Cast_TorqueConverterPumpSocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "TorqueConverterPumpSocket._Cast_TorqueConverterPumpSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def torque_converter_pump_socket(
            self: "TorqueConverterPumpSocket._Cast_TorqueConverterPumpSocket",
        ) -> "TorqueConverterPumpSocket":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpSocket._Cast_TorqueConverterPumpSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterPumpSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterPumpSocket._Cast_TorqueConverterPumpSocket":
        return self._Cast_TorqueConverterPumpSocket(self)
