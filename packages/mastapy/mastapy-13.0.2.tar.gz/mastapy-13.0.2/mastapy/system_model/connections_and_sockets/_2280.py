"""CVTBeltConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2275
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CVTBeltConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2288, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnection",)


Self = TypeVar("Self", bound="CVTBeltConnection")


class CVTBeltConnection(_2275.BeltConnection):
    """CVTBeltConnection

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnection")

    class _Cast_CVTBeltConnection:
        """Special nested class for casting CVTBeltConnection to subclasses."""

        def __init__(
            self: "CVTBeltConnection._Cast_CVTBeltConnection",
            parent: "CVTBeltConnection",
        ):
            self._parent = parent

        @property
        def belt_connection(
            self: "CVTBeltConnection._Cast_CVTBeltConnection",
        ) -> "_2275.BeltConnection":
            return self._parent._cast(_2275.BeltConnection)

        @property
        def inter_mountable_component_connection(
            self: "CVTBeltConnection._Cast_CVTBeltConnection",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(
            self: "CVTBeltConnection._Cast_CVTBeltConnection",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "CVTBeltConnection._Cast_CVTBeltConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def cvt_belt_connection(
            self: "CVTBeltConnection._Cast_CVTBeltConnection",
        ) -> "CVTBeltConnection":
            return self._parent

        def __getattr__(self: "CVTBeltConnection._Cast_CVTBeltConnection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTBeltConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def belt_efficiency(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BeltEfficiency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @belt_efficiency.setter
    @enforce_parameter_types
    def belt_efficiency(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BeltEfficiency = value

    @property
    def cast_to(self: Self) -> "CVTBeltConnection._Cast_CVTBeltConnection":
        return self._Cast_CVTBeltConnection(self)
