"""CycloidalDiscPlanetaryBearingConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscPlanetaryBearingConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnection",)


Self = TypeVar("Self", bound="CycloidalDiscPlanetaryBearingConnection")


class CycloidalDiscPlanetaryBearingConnection(
    _2272.AbstractShaftToMountableComponentConnection
):
    """CycloidalDiscPlanetaryBearingConnection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscPlanetaryBearingConnection"
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnection:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnection to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnection._Cast_CycloidalDiscPlanetaryBearingConnection",
            parent: "CycloidalDiscPlanetaryBearingConnection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "CycloidalDiscPlanetaryBearingConnection._Cast_CycloidalDiscPlanetaryBearingConnection",
        ) -> "_2272.AbstractShaftToMountableComponentConnection":
            return self._parent._cast(_2272.AbstractShaftToMountableComponentConnection)

        @property
        def connection(
            self: "CycloidalDiscPlanetaryBearingConnection._Cast_CycloidalDiscPlanetaryBearingConnection",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "CycloidalDiscPlanetaryBearingConnection._Cast_CycloidalDiscPlanetaryBearingConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "CycloidalDiscPlanetaryBearingConnection._Cast_CycloidalDiscPlanetaryBearingConnection",
        ) -> "CycloidalDiscPlanetaryBearingConnection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnection._Cast_CycloidalDiscPlanetaryBearingConnection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CycloidalDiscPlanetaryBearingConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscPlanetaryBearingConnection._Cast_CycloidalDiscPlanetaryBearingConnection":
        return self._Cast_CycloidalDiscPlanetaryBearingConnection(self)
