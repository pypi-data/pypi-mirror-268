"""PartToPartShearCouplingConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.couplings import _2353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "PartToPartShearCouplingConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2288, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnection",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnection")


class PartToPartShearCouplingConnection(_2353.CouplingConnection):
    """PartToPartShearCouplingConnection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartToPartShearCouplingConnection")

    class _Cast_PartToPartShearCouplingConnection:
        """Special nested class for casting PartToPartShearCouplingConnection to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnection._Cast_PartToPartShearCouplingConnection",
            parent: "PartToPartShearCouplingConnection",
        ):
            self._parent = parent

        @property
        def coupling_connection(
            self: "PartToPartShearCouplingConnection._Cast_PartToPartShearCouplingConnection",
        ) -> "_2353.CouplingConnection":
            return self._parent._cast(_2353.CouplingConnection)

        @property
        def inter_mountable_component_connection(
            self: "PartToPartShearCouplingConnection._Cast_PartToPartShearCouplingConnection",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(
            self: "PartToPartShearCouplingConnection._Cast_PartToPartShearCouplingConnection",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "PartToPartShearCouplingConnection._Cast_PartToPartShearCouplingConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def part_to_part_shear_coupling_connection(
            self: "PartToPartShearCouplingConnection._Cast_PartToPartShearCouplingConnection",
        ) -> "PartToPartShearCouplingConnection":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnection._Cast_PartToPartShearCouplingConnection",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnection._Cast_PartToPartShearCouplingConnection":
        return self._Cast_PartToPartShearCouplingConnection(self)
