"""CylindricalComponentConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2277
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CylindricalComponentConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2278


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalComponentConnection",)


Self = TypeVar("Self", bound="CylindricalComponentConnection")


class CylindricalComponentConnection(_2277.ComponentConnection):
    """CylindricalComponentConnection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_COMPONENT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalComponentConnection")

    class _Cast_CylindricalComponentConnection:
        """Special nested class for casting CylindricalComponentConnection to subclasses."""

        def __init__(
            self: "CylindricalComponentConnection._Cast_CylindricalComponentConnection",
            parent: "CylindricalComponentConnection",
        ):
            self._parent = parent

        @property
        def component_connection(
            self: "CylindricalComponentConnection._Cast_CylindricalComponentConnection",
        ) -> "_2277.ComponentConnection":
            return self._parent._cast(_2277.ComponentConnection)

        @property
        def component_measurer(
            self: "CylindricalComponentConnection._Cast_CylindricalComponentConnection",
        ) -> "_2278.ComponentMeasurer":
            from mastapy.system_model.connections_and_sockets import _2278

            return self._parent._cast(_2278.ComponentMeasurer)

        @property
        def cylindrical_component_connection(
            self: "CylindricalComponentConnection._Cast_CylindricalComponentConnection",
        ) -> "CylindricalComponentConnection":
            return self._parent

        def __getattr__(
            self: "CylindricalComponentConnection._Cast_CylindricalComponentConnection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalComponentConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measuring_position_for_component(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.MeasuringPositionForComponent

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @measuring_position_for_component.setter
    @enforce_parameter_types
    def measuring_position_for_component(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.MeasuringPositionForComponent = value

    @property
    def measuring_position_for_connected_component(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.MeasuringPositionForConnectedComponent

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @measuring_position_for_connected_component.setter
    @enforce_parameter_types
    def measuring_position_for_connected_component(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.MeasuringPositionForConnectedComponent = value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalComponentConnection._Cast_CylindricalComponentConnection":
        return self._Cast_CylindricalComponentConnection(self)
