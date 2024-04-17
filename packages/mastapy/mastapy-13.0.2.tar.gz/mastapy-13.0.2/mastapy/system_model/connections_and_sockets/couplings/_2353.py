"""CouplingConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2288
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2349,
        _2351,
        _2355,
        _2357,
        _2359,
    )
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnection",)


Self = TypeVar("Self", bound="CouplingConnection")


class CouplingConnection(_2288.InterMountableComponentConnection):
    """CouplingConnection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnection")

    class _Cast_CouplingConnection:
        """Special nested class for casting CouplingConnection to subclasses."""

        def __init__(
            self: "CouplingConnection._Cast_CouplingConnection",
            parent: "CouplingConnection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2288.InterMountableComponentConnection":
            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def clutch_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2349.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2349

            return self._parent._cast(_2349.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2351.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2351

            return self._parent._cast(_2351.ConceptCouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2355.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2355

            return self._parent._cast(_2355.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2357.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2357

            return self._parent._cast(_2357.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2359.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2359

            return self._parent._cast(_2359.TorqueConverterConnection)

        @property
        def coupling_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "CouplingConnection":
            return self._parent

        def __getattr__(self: "CouplingConnection._Cast_CouplingConnection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CouplingConnection._Cast_CouplingConnection":
        return self._Cast_CouplingConnection(self)
