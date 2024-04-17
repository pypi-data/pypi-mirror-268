"""CouplingSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2350,
        _2352,
        _2356,
        _2358,
        _2360,
        _2361,
    )
    from mastapy.system_model.connections_and_sockets import _2303


__docformat__ = "restructuredtext en"
__all__ = ("CouplingSocket",)


Self = TypeVar("Self", bound="CouplingSocket")


class CouplingSocket(_2283.CylindricalSocket):
    """CouplingSocket

    This is a mastapy class.
    """

    TYPE = _COUPLING_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingSocket")

    class _Cast_CouplingSocket:
        """Special nested class for casting CouplingSocket to subclasses."""

        def __init__(
            self: "CouplingSocket._Cast_CouplingSocket", parent: "CouplingSocket"
        ):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2283.CylindricalSocket":
            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(self: "CouplingSocket._Cast_CouplingSocket") -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def clutch_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2350.ClutchSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2350

            return self._parent._cast(_2350.ClutchSocket)

        @property
        def concept_coupling_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2352.ConceptCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2352

            return self._parent._cast(_2352.ConceptCouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2356.PartToPartShearCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2356

            return self._parent._cast(_2356.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2358.SpringDamperSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2358

            return self._parent._cast(_2358.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2360.TorqueConverterPumpSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2360

            return self._parent._cast(_2360.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2361.TorqueConverterTurbineSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2361

            return self._parent._cast(_2361.TorqueConverterTurbineSocket)

        @property
        def coupling_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "CouplingSocket":
            return self._parent

        def __getattr__(self: "CouplingSocket._Cast_CouplingSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CouplingSocket._Cast_CouplingSocket":
        return self._Cast_CouplingSocket(self)
