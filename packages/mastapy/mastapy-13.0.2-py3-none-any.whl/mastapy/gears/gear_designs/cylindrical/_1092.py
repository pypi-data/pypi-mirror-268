"""ToothThicknessSpecificationBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.utility.units_and_measurements.measurements import _1674, _1695
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_THICKNESS_SPECIFICATION_BASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ToothThicknessSpecificationBase"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1040, _1050, _1071, _1091


__docformat__ = "restructuredtext en"
__all__ = ("ToothThicknessSpecificationBase",)


Self = TypeVar("Self", bound="ToothThicknessSpecificationBase")


class ToothThicknessSpecificationBase(_0.APIBase):
    """ToothThicknessSpecificationBase

    This is a mastapy class.
    """

    TYPE = _TOOTH_THICKNESS_SPECIFICATION_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToothThicknessSpecificationBase")

    class _Cast_ToothThicknessSpecificationBase:
        """Special nested class for casting ToothThicknessSpecificationBase to subclasses."""

        def __init__(
            self: "ToothThicknessSpecificationBase._Cast_ToothThicknessSpecificationBase",
            parent: "ToothThicknessSpecificationBase",
        ):
            self._parent = parent

        @property
        def finish_tooth_thickness_design_specification(
            self: "ToothThicknessSpecificationBase._Cast_ToothThicknessSpecificationBase",
        ) -> "_1050.FinishToothThicknessDesignSpecification":
            from mastapy.gears.gear_designs.cylindrical import _1050

            return self._parent._cast(_1050.FinishToothThicknessDesignSpecification)

        @property
        def readonly_tooth_thickness_specification(
            self: "ToothThicknessSpecificationBase._Cast_ToothThicknessSpecificationBase",
        ) -> "_1071.ReadonlyToothThicknessSpecification":
            from mastapy.gears.gear_designs.cylindrical import _1071

            return self._parent._cast(_1071.ReadonlyToothThicknessSpecification)

        @property
        def tooth_thickness_specification(
            self: "ToothThicknessSpecificationBase._Cast_ToothThicknessSpecificationBase",
        ) -> "_1091.ToothThicknessSpecification":
            from mastapy.gears.gear_designs.cylindrical import _1091

            return self._parent._cast(_1091.ToothThicknessSpecification)

        @property
        def tooth_thickness_specification_base(
            self: "ToothThicknessSpecificationBase._Cast_ToothThicknessSpecificationBase",
        ) -> "ToothThicknessSpecificationBase":
            return self._parent

        def __getattr__(
            self: "ToothThicknessSpecificationBase._Cast_ToothThicknessSpecificationBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ToothThicknessSpecificationBase.TYPE"):
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
    def ball_diameter_at_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BallDiameterAtFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def ball_diameter_at_tip_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BallDiameterAtTipFormDiameter

        if temp is None:
            return 0.0

        return temp

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
    def maximum_number_of_teeth_for_chordal_span_test(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNumberOfTeethForChordalSpanTest

        if temp is None:
            return 0

        return temp

    @property
    def minimum_number_of_teeth_for_chordal_span_test(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumNumberOfTeethForChordalSpanTest

        if temp is None:
            return 0

        return temp

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
    def chordal_span(
        self: Self,
    ) -> "_1040.CylindricalGearToothThicknessSpecification[_1674.LengthShort]":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChordalSpan

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1674.LengthShort](temp)

    @property
    def normal_thickness(
        self: Self,
    ) -> "_1040.CylindricalGearToothThicknessSpecification[_1674.LengthShort]":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1674.LengthShort](temp)

    @property
    def normal_thickness_at_specified_diameter(
        self: Self,
    ) -> "_1040.CylindricalGearToothThicknessSpecification[_1674.LengthShort]":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalThicknessAtSpecifiedDiameter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1674.LengthShort](temp)

    @property
    def over_balls(
        self: Self,
    ) -> "_1040.CylindricalGearToothThicknessSpecification[_1674.LengthShort]":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverBalls

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1674.LengthShort](temp)

    @property
    def over_two_pins_free_pin_method(
        self: Self,
    ) -> "_1040.CylindricalGearToothThicknessSpecification[_1674.LengthShort]":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverTwoPinsFreePinMethod

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1674.LengthShort](temp)

    @property
    def over_two_pins_transverse_method(
        self: Self,
    ) -> "_1040.CylindricalGearToothThicknessSpecification[_1674.LengthShort]":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverTwoPinsTransverseMethod

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1674.LengthShort](temp)

    @property
    def profile_shift(
        self: Self,
    ) -> "_1040.CylindricalGearToothThicknessSpecification[_1674.LengthShort]":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileShift

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1674.LengthShort](temp)

    @property
    def profile_shift_coefficient(
        self: Self,
    ) -> "_1040.CylindricalGearToothThicknessSpecification[_1695.Number]":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.Number]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileShiftCoefficient

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1695.Number](temp)

    @property
    def transverse_thickness(
        self: Self,
    ) -> "_1040.CylindricalGearToothThicknessSpecification[_1674.LengthShort]":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1674.LengthShort](temp)

    @property
    def transverse_thickness_at_specified_diameter(
        self: Self,
    ) -> "_1040.CylindricalGearToothThicknessSpecification[_1674.LengthShort]":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseThicknessAtSpecifiedDiameter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1674.LengthShort](temp)

    @property
    def tooth_thickness(
        self: Self,
    ) -> "List[_1040.CylindricalGearToothThicknessSpecification[_1674.LengthShort]]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearToothThicknessSpecification[mastapy.utility.units_and_measurements.measurements.LengthShort]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothThickness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ToothThicknessSpecificationBase._Cast_ToothThicknessSpecificationBase":
        return self._Cast_ToothThicknessSpecificationBase(self)
