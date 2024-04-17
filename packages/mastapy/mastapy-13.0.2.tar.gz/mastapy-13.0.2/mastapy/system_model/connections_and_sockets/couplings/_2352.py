"""ConceptCouplingSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.couplings import _2354
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "ConceptCouplingSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingSocket",)


Self = TypeVar("Self", bound="ConceptCouplingSocket")


class ConceptCouplingSocket(_2354.CouplingSocket):
    """ConceptCouplingSocket

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingSocket")

    class _Cast_ConceptCouplingSocket:
        """Special nested class for casting ConceptCouplingSocket to subclasses."""

        def __init__(
            self: "ConceptCouplingSocket._Cast_ConceptCouplingSocket",
            parent: "ConceptCouplingSocket",
        ):
            self._parent = parent

        @property
        def coupling_socket(
            self: "ConceptCouplingSocket._Cast_ConceptCouplingSocket",
        ) -> "_2354.CouplingSocket":
            return self._parent._cast(_2354.CouplingSocket)

        @property
        def cylindrical_socket(
            self: "ConceptCouplingSocket._Cast_ConceptCouplingSocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "ConceptCouplingSocket._Cast_ConceptCouplingSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def concept_coupling_socket(
            self: "ConceptCouplingSocket._Cast_ConceptCouplingSocket",
        ) -> "ConceptCouplingSocket":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingSocket._Cast_ConceptCouplingSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConceptCouplingSocket._Cast_ConceptCouplingSocket":
        return self._Cast_ConceptCouplingSocket(self)
