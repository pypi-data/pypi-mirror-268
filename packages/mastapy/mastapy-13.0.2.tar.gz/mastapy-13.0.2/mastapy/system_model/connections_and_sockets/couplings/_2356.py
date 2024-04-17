"""PartToPartShearCouplingSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.couplings import _2354
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "PartToPartShearCouplingSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283, _2303


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingSocket",)


Self = TypeVar("Self", bound="PartToPartShearCouplingSocket")


class PartToPartShearCouplingSocket(_2354.CouplingSocket):
    """PartToPartShearCouplingSocket

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartToPartShearCouplingSocket")

    class _Cast_PartToPartShearCouplingSocket:
        """Special nested class for casting PartToPartShearCouplingSocket to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingSocket._Cast_PartToPartShearCouplingSocket",
            parent: "PartToPartShearCouplingSocket",
        ):
            self._parent = parent

        @property
        def coupling_socket(
            self: "PartToPartShearCouplingSocket._Cast_PartToPartShearCouplingSocket",
        ) -> "_2354.CouplingSocket":
            return self._parent._cast(_2354.CouplingSocket)

        @property
        def cylindrical_socket(
            self: "PartToPartShearCouplingSocket._Cast_PartToPartShearCouplingSocket",
        ) -> "_2283.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "PartToPartShearCouplingSocket._Cast_PartToPartShearCouplingSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "PartToPartShearCouplingSocket._Cast_PartToPartShearCouplingSocket",
        ) -> "PartToPartShearCouplingSocket":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingSocket._Cast_PartToPartShearCouplingSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartToPartShearCouplingSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingSocket._Cast_PartToPartShearCouplingSocket":
        return self._Cast_PartToPartShearCouplingSocket(self)
