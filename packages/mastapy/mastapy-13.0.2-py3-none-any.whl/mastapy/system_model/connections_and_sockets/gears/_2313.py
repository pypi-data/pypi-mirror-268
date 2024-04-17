"""ConceptGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2321
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConceptGearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2303


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearTeethSocket",)


Self = TypeVar("Self", bound="ConceptGearTeethSocket")


class ConceptGearTeethSocket(_2321.GearTeethSocket):
    """ConceptGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearTeethSocket")

    class _Cast_ConceptGearTeethSocket:
        """Special nested class for casting ConceptGearTeethSocket to subclasses."""

        def __init__(
            self: "ConceptGearTeethSocket._Cast_ConceptGearTeethSocket",
            parent: "ConceptGearTeethSocket",
        ):
            self._parent = parent

        @property
        def gear_teeth_socket(
            self: "ConceptGearTeethSocket._Cast_ConceptGearTeethSocket",
        ) -> "_2321.GearTeethSocket":
            return self._parent._cast(_2321.GearTeethSocket)

        @property
        def socket(
            self: "ConceptGearTeethSocket._Cast_ConceptGearTeethSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def concept_gear_teeth_socket(
            self: "ConceptGearTeethSocket._Cast_ConceptGearTeethSocket",
        ) -> "ConceptGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "ConceptGearTeethSocket._Cast_ConceptGearTeethSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConceptGearTeethSocket._Cast_ConceptGearTeethSocket":
        return self._Cast_ConceptGearTeethSocket(self)
