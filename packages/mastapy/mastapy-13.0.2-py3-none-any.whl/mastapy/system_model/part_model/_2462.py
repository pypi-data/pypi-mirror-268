"""GuideDxfModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.utility.units_and_measurements import _1617
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2451
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "GuideDxfModel"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModel",)


Self = TypeVar("Self", bound="GuideDxfModel")


class GuideDxfModel(_2451.Component):
    """GuideDxfModel

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModel")

    class _Cast_GuideDxfModel:
        """Special nested class for casting GuideDxfModel to subclasses."""

        def __init__(
            self: "GuideDxfModel._Cast_GuideDxfModel", parent: "GuideDxfModel"
        ):
            self._parent = parent

        @property
        def component(self: "GuideDxfModel._Cast_GuideDxfModel") -> "_2451.Component":
            return self._parent._cast(_2451.Component)

        @property
        def part(self: "GuideDxfModel._Cast_GuideDxfModel") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "GuideDxfModel._Cast_GuideDxfModel",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def guide_dxf_model(
            self: "GuideDxfModel._Cast_GuideDxfModel",
        ) -> "GuideDxfModel":
            return self._parent

        def __getattr__(self: "GuideDxfModel._Cast_GuideDxfModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideDxfModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length_unit(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.LengthUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @length_unit.setter
    @enforce_parameter_types
    def length_unit(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.LengthUnit = value

    @property
    def memory_usage(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MemoryUsage

        if temp is None:
            return 0

        return temp

    @property
    def scale_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ScaleFactor

        if temp is None:
            return 0.0

        return temp

    @scale_factor.setter
    @enforce_parameter_types
    def scale_factor(self: Self, value: "float"):
        self.wrapped.ScaleFactor = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "GuideDxfModel._Cast_GuideDxfModel":
        return self._Cast_GuideDxfModel(self)
