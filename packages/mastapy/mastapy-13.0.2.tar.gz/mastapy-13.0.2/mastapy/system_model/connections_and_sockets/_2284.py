"""DatumMeasurement"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2278
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_MEASUREMENT = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "DatumMeasurement"
)


__docformat__ = "restructuredtext en"
__all__ = ("DatumMeasurement",)


Self = TypeVar("Self", bound="DatumMeasurement")


class DatumMeasurement(_2278.ComponentMeasurer):
    """DatumMeasurement

    This is a mastapy class.
    """

    TYPE = _DATUM_MEASUREMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumMeasurement")

    class _Cast_DatumMeasurement:
        """Special nested class for casting DatumMeasurement to subclasses."""

        def __init__(
            self: "DatumMeasurement._Cast_DatumMeasurement", parent: "DatumMeasurement"
        ):
            self._parent = parent

        @property
        def component_measurer(
            self: "DatumMeasurement._Cast_DatumMeasurement",
        ) -> "_2278.ComponentMeasurer":
            return self._parent._cast(_2278.ComponentMeasurer)

        @property
        def datum_measurement(
            self: "DatumMeasurement._Cast_DatumMeasurement",
        ) -> "DatumMeasurement":
            return self._parent

        def __getattr__(self: "DatumMeasurement._Cast_DatumMeasurement", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatumMeasurement.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measuring_position(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.MeasuringPosition

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @measuring_position.setter
    @enforce_parameter_types
    def measuring_position(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.MeasuringPosition = value

    @property
    def cast_to(self: Self) -> "DatumMeasurement._Cast_DatumMeasurement":
        return self._Cast_DatumMeasurement(self)
