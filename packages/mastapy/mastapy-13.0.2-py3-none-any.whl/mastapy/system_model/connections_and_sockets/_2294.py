"""PlanetaryConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "PlanetaryConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2272, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnection",)


Self = TypeVar("Self", bound="PlanetaryConnection")


class PlanetaryConnection(_2302.ShaftToMountableComponentConnection):
    """PlanetaryConnection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnection")

    class _Cast_PlanetaryConnection:
        """Special nested class for casting PlanetaryConnection to subclasses."""

        def __init__(
            self: "PlanetaryConnection._Cast_PlanetaryConnection",
            parent: "PlanetaryConnection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection(
            self: "PlanetaryConnection._Cast_PlanetaryConnection",
        ) -> "_2302.ShaftToMountableComponentConnection":
            return self._parent._cast(_2302.ShaftToMountableComponentConnection)

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "PlanetaryConnection._Cast_PlanetaryConnection",
        ) -> "_2272.AbstractShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.AbstractShaftToMountableComponentConnection)

        @property
        def connection(
            self: "PlanetaryConnection._Cast_PlanetaryConnection",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "PlanetaryConnection._Cast_PlanetaryConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def planetary_connection(
            self: "PlanetaryConnection._Cast_PlanetaryConnection",
        ) -> "PlanetaryConnection":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnection._Cast_PlanetaryConnection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PlanetaryConnection._Cast_PlanetaryConnection":
        return self._Cast_PlanetaryConnection(self)
