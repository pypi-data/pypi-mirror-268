"""CylindricalGearManufactureError"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6900
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MANUFACTURE_ERROR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearManufactureError",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearManufactureError",)


Self = TypeVar("Self", bound="CylindricalGearManufactureError")


class CylindricalGearManufactureError(_6900.GearManufactureError):
    """CylindricalGearManufactureError

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MANUFACTURE_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearManufactureError")

    class _Cast_CylindricalGearManufactureError:
        """Special nested class for casting CylindricalGearManufactureError to subclasses."""

        def __init__(
            self: "CylindricalGearManufactureError._Cast_CylindricalGearManufactureError",
            parent: "CylindricalGearManufactureError",
        ):
            self._parent = parent

        @property
        def gear_manufacture_error(
            self: "CylindricalGearManufactureError._Cast_CylindricalGearManufactureError",
        ) -> "_6900.GearManufactureError":
            return self._parent._cast(_6900.GearManufactureError)

        @property
        def cylindrical_gear_manufacture_error(
            self: "CylindricalGearManufactureError._Cast_CylindricalGearManufactureError",
        ) -> "CylindricalGearManufactureError":
            return self._parent

        def __getattr__(
            self: "CylindricalGearManufactureError._Cast_CylindricalGearManufactureError",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearManufactureError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clocking_angle_error(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ClockingAngleError

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @clocking_angle_error.setter
    @enforce_parameter_types
    def clocking_angle_error(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ClockingAngleError = value

    @property
    def extra_backlash(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ExtraBacklash

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @extra_backlash.setter
    @enforce_parameter_types
    def extra_backlash(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ExtraBacklash = value

    @property
    def pitch_error_measurement_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PitchErrorMeasurementDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pitch_error_measurement_diameter.setter
    @enforce_parameter_types
    def pitch_error_measurement_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PitchErrorMeasurementDiameter = value

    @property
    def pitch_error_measurement_face_width(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PitchErrorMeasurementFaceWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pitch_error_measurement_face_width.setter
    @enforce_parameter_types
    def pitch_error_measurement_face_width(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PitchErrorMeasurementFaceWidth = value

    @property
    def pitch_error_phase_shift_on_left_flank(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PitchErrorPhaseShiftOnLeftFlank

        if temp is None:
            return 0.0

        return temp

    @pitch_error_phase_shift_on_left_flank.setter
    @enforce_parameter_types
    def pitch_error_phase_shift_on_left_flank(self: Self, value: "float"):
        self.wrapped.PitchErrorPhaseShiftOnLeftFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def pitch_error_phase_shift_on_right_flank(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PitchErrorPhaseShiftOnRightFlank

        if temp is None:
            return 0.0

        return temp

    @pitch_error_phase_shift_on_right_flank.setter
    @enforce_parameter_types
    def pitch_error_phase_shift_on_right_flank(self: Self, value: "float"):
        self.wrapped.PitchErrorPhaseShiftOnRightFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def pitch_errors_left_flank(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.PitchErrorsLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @pitch_errors_left_flank.setter
    @enforce_parameter_types
    def pitch_errors_left_flank(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.PitchErrorsLeftFlank = value.wrapped

    @property
    def pitch_errors_right_flank(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.PitchErrorsRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @pitch_errors_right_flank.setter
    @enforce_parameter_types
    def pitch_errors_right_flank(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.PitchErrorsRightFlank = value.wrapped

    @property
    def runout(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Runout

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @runout.setter
    @enforce_parameter_types
    def runout(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Runout = value

    @property
    def runout_reference_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RunoutReferenceAngle

        if temp is None:
            return 0.0

        return temp

    @runout_reference_angle.setter
    @enforce_parameter_types
    def runout_reference_angle(self: Self, value: "float"):
        self.wrapped.RunoutReferenceAngle = float(value) if value is not None else 0.0

    @property
    def separation_on_left_flank(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SeparationOnLeftFlank

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @separation_on_left_flank.setter
    @enforce_parameter_types
    def separation_on_left_flank(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SeparationOnLeftFlank = value

    @property
    def separation_on_right_flank(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SeparationOnRightFlank

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @separation_on_right_flank.setter
    @enforce_parameter_types
    def separation_on_right_flank(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SeparationOnRightFlank = value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearManufactureError._Cast_CylindricalGearManufactureError":
        return self._Cast_CylindricalGearManufactureError(self)
