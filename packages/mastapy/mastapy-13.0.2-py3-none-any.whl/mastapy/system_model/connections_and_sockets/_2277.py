"""ComponentConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets import _2278
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "ComponentConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.connections_and_sockets import _2282


__docformat__ = "restructuredtext en"
__all__ = ("ComponentConnection",)


Self = TypeVar("Self", bound="ComponentConnection")


class ComponentConnection(_2278.ComponentMeasurer):
    """ComponentConnection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentConnection")

    class _Cast_ComponentConnection:
        """Special nested class for casting ComponentConnection to subclasses."""

        def __init__(
            self: "ComponentConnection._Cast_ComponentConnection",
            parent: "ComponentConnection",
        ):
            self._parent = parent

        @property
        def component_measurer(
            self: "ComponentConnection._Cast_ComponentConnection",
        ) -> "_2278.ComponentMeasurer":
            return self._parent._cast(_2278.ComponentMeasurer)

        @property
        def cylindrical_component_connection(
            self: "ComponentConnection._Cast_ComponentConnection",
        ) -> "_2282.CylindricalComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2282

            return self._parent._cast(_2282.CylindricalComponentConnection)

        @property
        def component_connection(
            self: "ComponentConnection._Cast_ComponentConnection",
        ) -> "ComponentConnection":
            return self._parent

        def __getattr__(
            self: "ComponentConnection._Cast_ComponentConnection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def connected_components_socket(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponentsSocket

        if temp is None:
            return ""

        return temp

    @property
    def detail_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DetailView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def socket(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Socket

        if temp is None:
            return ""

        return temp

    @property
    def connected_component(self: Self) -> "_2451.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    def swap(self: Self):
        """Method does not return."""
        self.wrapped.Swap()

    @property
    def cast_to(self: Self) -> "ComponentConnection._Cast_ComponentConnection":
        return self._Cast_ComponentConnection(self)
