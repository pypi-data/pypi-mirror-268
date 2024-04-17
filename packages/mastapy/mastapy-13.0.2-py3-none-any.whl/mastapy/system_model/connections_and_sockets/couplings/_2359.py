"""TorqueConverterConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.couplings import _2353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "TorqueConverterConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2288, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnection",)


Self = TypeVar("Self", bound="TorqueConverterConnection")


class TorqueConverterConnection(_2353.CouplingConnection):
    """TorqueConverterConnection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterConnection")

    class _Cast_TorqueConverterConnection:
        """Special nested class for casting TorqueConverterConnection to subclasses."""

        def __init__(
            self: "TorqueConverterConnection._Cast_TorqueConverterConnection",
            parent: "TorqueConverterConnection",
        ):
            self._parent = parent

        @property
        def coupling_connection(
            self: "TorqueConverterConnection._Cast_TorqueConverterConnection",
        ) -> "_2353.CouplingConnection":
            return self._parent._cast(_2353.CouplingConnection)

        @property
        def inter_mountable_component_connection(
            self: "TorqueConverterConnection._Cast_TorqueConverterConnection",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(
            self: "TorqueConverterConnection._Cast_TorqueConverterConnection",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "TorqueConverterConnection._Cast_TorqueConverterConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def torque_converter_connection(
            self: "TorqueConverterConnection._Cast_TorqueConverterConnection",
        ) -> "TorqueConverterConnection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnection._Cast_TorqueConverterConnection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterConnection._Cast_TorqueConverterConnection":
        return self._Cast_TorqueConverterConnection(self)
