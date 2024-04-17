"""MutableCurve"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.geometry.two_d.curves import _316
from mastapy.gears.manufacturing.cylindrical.cutters import _722
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MUTABLE_CURVE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters", "MutableCurve"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _706


__docformat__ = "restructuredtext en"
__all__ = ("MutableCurve",)


Self = TypeVar("Self", bound="MutableCurve")


class MutableCurve(_722.MutableCommon):
    """MutableCurve

    This is a mastapy class.
    """

    TYPE = _MUTABLE_CURVE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MutableCurve")

    class _Cast_MutableCurve:
        """Special nested class for casting MutableCurve to subclasses."""

        def __init__(self: "MutableCurve._Cast_MutableCurve", parent: "MutableCurve"):
            self._parent = parent

        @property
        def mutable_common(
            self: "MutableCurve._Cast_MutableCurve",
        ) -> "_722.MutableCommon":
            return self._parent._cast(_722.MutableCommon)

        @property
        def curve_in_linked_list(
            self: "MutableCurve._Cast_MutableCurve",
        ) -> "_706.CurveInLinkedList":
            from mastapy.gears.manufacturing.cylindrical.cutters import _706

            return self._parent._cast(_706.CurveInLinkedList)

        @property
        def mutable_curve(self: "MutableCurve._Cast_MutableCurve") -> "MutableCurve":
            return self._parent

        def __getattr__(self: "MutableCurve._Cast_MutableCurve", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MutableCurve.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Crowning

        if temp is None:
            return 0.0

        return temp

    @crowning.setter
    @enforce_parameter_types
    def crowning(self: Self, value: "float"):
        self.wrapped.Crowning = float(value) if value is not None else 0.0

    @property
    def curve_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes":
        """EnumWithSelectedValue[mastapy.geometry.two_d.curves.BasicCurveTypes]"""
        temp = self.wrapped.CurveType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @curve_type.setter
    @enforce_parameter_types
    def curve_type(self: Self, value: "_316.BasicCurveTypes"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.CurveType = value

    @property
    def height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Height

        if temp is None:
            return 0.0

        return temp

    @height.setter
    @enforce_parameter_types
    def height(self: Self, value: "float"):
        self.wrapped.Height = float(value) if value is not None else 0.0

    @property
    def height_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def linear_modification(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearModification

        if temp is None:
            return 0.0

        return temp

    @linear_modification.setter
    @enforce_parameter_types
    def linear_modification(self: Self, value: "float"):
        self.wrapped.LinearModification = float(value) if value is not None else 0.0

    @property
    def nominal_section_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NominalSectionPressureAngle

        if temp is None:
            return 0.0

        return temp

    @nominal_section_pressure_angle.setter
    @enforce_parameter_types
    def nominal_section_pressure_angle(self: Self, value: "float"):
        self.wrapped.NominalSectionPressureAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def pressure_angle_modification(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureAngleModification

        if temp is None:
            return 0.0

        return temp

    @pressure_angle_modification.setter
    @enforce_parameter_types
    def pressure_angle_modification(self: Self, value: "float"):
        self.wrapped.PressureAngleModification = (
            float(value) if value is not None else 0.0
        )

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
    def cast_to(self: Self) -> "MutableCurve._Cast_MutableCurve":
        return self._Cast_MutableCurve(self)
