"""CoaxialConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CoaxialConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2342
    from mastapy.system_model.connections_and_sockets import _2272, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnection",)


Self = TypeVar("Self", bound="CoaxialConnection")


class CoaxialConnection(_2302.ShaftToMountableComponentConnection):
    """CoaxialConnection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnection")

    class _Cast_CoaxialConnection:
        """Special nested class for casting CoaxialConnection to subclasses."""

        def __init__(
            self: "CoaxialConnection._Cast_CoaxialConnection",
            parent: "CoaxialConnection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection(
            self: "CoaxialConnection._Cast_CoaxialConnection",
        ) -> "_2302.ShaftToMountableComponentConnection":
            return self._parent._cast(_2302.ShaftToMountableComponentConnection)

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "CoaxialConnection._Cast_CoaxialConnection",
        ) -> "_2272.AbstractShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.AbstractShaftToMountableComponentConnection)

        @property
        def connection(
            self: "CoaxialConnection._Cast_CoaxialConnection",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "CoaxialConnection._Cast_CoaxialConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "CoaxialConnection._Cast_CoaxialConnection",
        ) -> "_2342.CycloidalDiscCentralBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2342

            return self._parent._cast(_2342.CycloidalDiscCentralBearingConnection)

        @property
        def coaxial_connection(
            self: "CoaxialConnection._Cast_CoaxialConnection",
        ) -> "CoaxialConnection":
            return self._parent

        def __getattr__(self: "CoaxialConnection._Cast_CoaxialConnection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoaxialConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CoaxialConnection._Cast_CoaxialConnection":
        return self._Cast_CoaxialConnection(self)
