"""MutableCommon"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.manufacturing.cylindrical import _612
from mastapy.gears.manufacturing.cylindrical.cutters import _706
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MUTABLE_COMMON = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "MutableCommon"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _723, _724


__docformat__ = "restructuredtext en"
__all__ = ("MutableCommon",)


Self = TypeVar("Self", bound="MutableCommon")


class MutableCommon(_706.CurveInLinkedList):
    """MutableCommon

    This is a mastapy class.
    """

    TYPE = _MUTABLE_COMMON
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MutableCommon")

    class _Cast_MutableCommon:
        """Special nested class for casting MutableCommon to subclasses."""

        def __init__(
            self: "MutableCommon._Cast_MutableCommon", parent: "MutableCommon"
        ):
            self._parent = parent

        @property
        def curve_in_linked_list(
            self: "MutableCommon._Cast_MutableCommon",
        ) -> "_706.CurveInLinkedList":
            return self._parent._cast(_706.CurveInLinkedList)

        @property
        def mutable_curve(
            self: "MutableCommon._Cast_MutableCommon",
        ) -> "_723.MutableCurve":
            from mastapy.gears.manufacturing.cylindrical.cutters import _723

            return self._parent._cast(_723.MutableCurve)

        @property
        def mutable_fillet(
            self: "MutableCommon._Cast_MutableCommon",
        ) -> "_724.MutableFillet":
            from mastapy.gears.manufacturing.cylindrical.cutters import _724

            return self._parent._cast(_724.MutableFillet)

        @property
        def mutable_common(
            self: "MutableCommon._Cast_MutableCommon",
        ) -> "MutableCommon":
            return self._parent

        def __getattr__(self: "MutableCommon._Cast_MutableCommon", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MutableCommon.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def protuberance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Protuberance

        if temp is None:
            return 0.0

        return temp

    @protuberance.setter
    @enforce_parameter_types
    def protuberance(self: Self, value: "float"):
        self.wrapped.Protuberance = float(value) if value is not None else 0.0

    @property
    def radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: Self, value: "float"):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def section(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections":
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.CutterFlankSections]"""
        temp = self.wrapped.Section

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @section.setter
    @enforce_parameter_types
    def section(self: Self, value: "_612.CutterFlankSections"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CutterFlankSections.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Section = value

    def remove(self: Self):
        """Method does not return."""
        self.wrapped.Remove()

    def split(self: Self):
        """Method does not return."""
        self.wrapped.Split()

    @property
    def cast_to(self: Self) -> "MutableCommon._Cast_MutableCommon":
        return self._Cast_MutableCommon(self)
