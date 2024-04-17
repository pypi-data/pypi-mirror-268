"""ReadonlyToothThicknessSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1091
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_READONLY_TOOTH_THICKNESS_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ReadonlyToothThicknessSpecification"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1092


__docformat__ = "restructuredtext en"
__all__ = ("ReadonlyToothThicknessSpecification",)


Self = TypeVar("Self", bound="ReadonlyToothThicknessSpecification")


class ReadonlyToothThicknessSpecification(_1091.ToothThicknessSpecification):
    """ReadonlyToothThicknessSpecification

    This is a mastapy class.
    """

    TYPE = _READONLY_TOOTH_THICKNESS_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ReadonlyToothThicknessSpecification")

    class _Cast_ReadonlyToothThicknessSpecification:
        """Special nested class for casting ReadonlyToothThicknessSpecification to subclasses."""

        def __init__(
            self: "ReadonlyToothThicknessSpecification._Cast_ReadonlyToothThicknessSpecification",
            parent: "ReadonlyToothThicknessSpecification",
        ):
            self._parent = parent

        @property
        def tooth_thickness_specification(
            self: "ReadonlyToothThicknessSpecification._Cast_ReadonlyToothThicknessSpecification",
        ) -> "_1091.ToothThicknessSpecification":
            return self._parent._cast(_1091.ToothThicknessSpecification)

        @property
        def tooth_thickness_specification_base(
            self: "ReadonlyToothThicknessSpecification._Cast_ReadonlyToothThicknessSpecification",
        ) -> "_1092.ToothThicknessSpecificationBase":
            from mastapy.gears.gear_designs.cylindrical import _1092

            return self._parent._cast(_1092.ToothThicknessSpecificationBase)

        @property
        def readonly_tooth_thickness_specification(
            self: "ReadonlyToothThicknessSpecification._Cast_ReadonlyToothThicknessSpecification",
        ) -> "ReadonlyToothThicknessSpecification":
            return self._parent

        def __getattr__(
            self: "ReadonlyToothThicknessSpecification._Cast_ReadonlyToothThicknessSpecification",
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
        self: Self, instance_to_wrap: "ReadonlyToothThicknessSpecification.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ball_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BallDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @ball_diameter.setter
    @enforce_parameter_types
    def ball_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BallDiameter = value

    @property
    def diameter_at_thickness_measurement(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DiameterAtThicknessMeasurement

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter_at_thickness_measurement.setter
    @enforce_parameter_types
    def diameter_at_thickness_measurement(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DiameterAtThicknessMeasurement = value

    @property
    def number_of_teeth_for_chordal_span_test(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfTeethForChordalSpanTest

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_teeth_for_chordal_span_test.setter
    @enforce_parameter_types
    def number_of_teeth_for_chordal_span_test(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfTeethForChordalSpanTest = value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ReadonlyToothThicknessSpecification._Cast_ReadonlyToothThicknessSpecification"
    ):
        return self._Cast_ReadonlyToothThicknessSpecification(self)
