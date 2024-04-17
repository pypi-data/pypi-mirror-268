"""RingPinsToDiscConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.connections_and_sockets import _2288
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "RingPinsToDiscConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnection",)


Self = TypeVar("Self", bound="RingPinsToDiscConnection")


class RingPinsToDiscConnection(_2288.InterMountableComponentConnection):
    """RingPinsToDiscConnection

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsToDiscConnection")

    class _Cast_RingPinsToDiscConnection:
        """Special nested class for casting RingPinsToDiscConnection to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnection._Cast_RingPinsToDiscConnection",
            parent: "RingPinsToDiscConnection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection(
            self: "RingPinsToDiscConnection._Cast_RingPinsToDiscConnection",
        ) -> "_2288.InterMountableComponentConnection":
            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(
            self: "RingPinsToDiscConnection._Cast_RingPinsToDiscConnection",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "RingPinsToDiscConnection._Cast_RingPinsToDiscConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def ring_pins_to_disc_connection(
            self: "RingPinsToDiscConnection._Cast_RingPinsToDiscConnection",
        ) -> "RingPinsToDiscConnection":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnection._Cast_RingPinsToDiscConnection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsToDiscConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactStiffness

        if temp is None:
            return 0.0

        return temp

    @contact_stiffness.setter
    @enforce_parameter_types
    def contact_stiffness(self: Self, value: "float"):
        self.wrapped.ContactStiffness = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnection._Cast_RingPinsToDiscConnection":
        return self._Cast_RingPinsToDiscConnection(self)
