"""CylindricalGearPairCreationOptions"""

from __future__ import annotations

from typing import TypeVar, Any, Union, Tuple
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.creation_options import _1153
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PAIR_CREATION_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.CreationOptions",
    "CylindricalGearPairCreationOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearPairCreationOptions",)


Self = TypeVar("Self", bound="CylindricalGearPairCreationOptions")


class CylindricalGearPairCreationOptions(
    _1153.GearSetCreationOptions["_1032.CylindricalGearSetDesign"]
):
    """CylindricalGearPairCreationOptions

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PAIR_CREATION_OPTIONS

    class DerivedParameterOption(Enum):
        """DerivedParameterOption is a nested enum."""

        @classmethod
        def type_(cls):
            return _CYLINDRICAL_GEAR_PAIR_CREATION_OPTIONS.DerivedParameterOption

        CENTRE_DISTANCE = 0
        NORMAL_MODULE = 1
        HELIX_ANGLE = 2

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    DerivedParameterOption.__setattr__ = __enum_setattr
    DerivedParameterOption.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearPairCreationOptions")

    class _Cast_CylindricalGearPairCreationOptions:
        """Special nested class for casting CylindricalGearPairCreationOptions to subclasses."""

        def __init__(
            self: "CylindricalGearPairCreationOptions._Cast_CylindricalGearPairCreationOptions",
            parent: "CylindricalGearPairCreationOptions",
        ):
            self._parent = parent

        @property
        def gear_set_creation_options(
            self: "CylindricalGearPairCreationOptions._Cast_CylindricalGearPairCreationOptions",
        ) -> "_1153.GearSetCreationOptions":
            return self._parent._cast(_1153.GearSetCreationOptions)

        @property
        def cylindrical_gear_pair_creation_options(
            self: "CylindricalGearPairCreationOptions._Cast_CylindricalGearPairCreationOptions",
        ) -> "CylindricalGearPairCreationOptions":
            return self._parent

        def __getattr__(
            self: "CylindricalGearPairCreationOptions._Cast_CylindricalGearPairCreationOptions",
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
        self: Self, instance_to_wrap: "CylindricalGearPairCreationOptions.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @centre_distance.setter
    @enforce_parameter_types
    def centre_distance(self: Self, value: "float"):
        self.wrapped.CentreDistance = float(value) if value is not None else 0.0

    @property
    def centre_distance_target(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentreDistanceTarget

        if temp is None:
            return 0.0

        return temp

    @centre_distance_target.setter
    @enforce_parameter_types
    def centre_distance_target(self: Self, value: "float"):
        self.wrapped.CentreDistanceTarget = float(value) if value is not None else 0.0

    @property
    def derived_parameter(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions.DerivedParameterOption]"""
        temp = self.wrapped.DerivedParameter

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @derived_parameter.setter
    @enforce_parameter_types
    def derived_parameter(
        self: Self, value: "CylindricalGearPairCreationOptions.DerivedParameterOption"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DerivedParameter = value

    @property
    def diametral_pitch(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiametralPitch

        if temp is None:
            return 0.0

        return temp

    @diametral_pitch.setter
    @enforce_parameter_types
    def diametral_pitch(self: Self, value: "float"):
        self.wrapped.DiametralPitch = float(value) if value is not None else 0.0

    @property
    def diametral_pitch_target(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiametralPitchTarget

        if temp is None:
            return 0.0

        return temp

    @diametral_pitch_target.setter
    @enforce_parameter_types
    def diametral_pitch_target(self: Self, value: "float"):
        self.wrapped.DiametralPitchTarget = float(value) if value is not None else 0.0

    @property
    def helix_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @helix_angle.setter
    @enforce_parameter_types
    def helix_angle(self: Self, value: "float"):
        self.wrapped.HelixAngle = float(value) if value is not None else 0.0

    @property
    def helix_angle_target(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngleTarget

        if temp is None:
            return 0.0

        return temp

    @helix_angle_target.setter
    @enforce_parameter_types
    def helix_angle_target(self: Self, value: "float"):
        self.wrapped.HelixAngleTarget = float(value) if value is not None else 0.0

    @property
    def normal_module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @normal_module.setter
    @enforce_parameter_types
    def normal_module(self: Self, value: "float"):
        self.wrapped.NormalModule = float(value) if value is not None else 0.0

    @property
    def normal_module_target(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalModuleTarget

        if temp is None:
            return 0.0

        return temp

    @normal_module_target.setter
    @enforce_parameter_types
    def normal_module_target(self: Self, value: "float"):
        self.wrapped.NormalModuleTarget = float(value) if value is not None else 0.0

    @property
    def normal_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle.setter
    @enforce_parameter_types
    def normal_pressure_angle(self: Self, value: "float"):
        self.wrapped.NormalPressureAngle = float(value) if value is not None else 0.0

    @property
    def pinion_face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionFaceWidth

        if temp is None:
            return 0.0

        return temp

    @pinion_face_width.setter
    @enforce_parameter_types
    def pinion_face_width(self: Self, value: "float"):
        self.wrapped.PinionFaceWidth = float(value) if value is not None else 0.0

    @property
    def pinion_number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PinionNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @pinion_number_of_teeth.setter
    @enforce_parameter_types
    def pinion_number_of_teeth(self: Self, value: "int"):
        self.wrapped.PinionNumberOfTeeth = int(value) if value is not None else 0

    @property
    def ratio_guide(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RatioGuide

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @ratio_guide.setter
    @enforce_parameter_types
    def ratio_guide(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RatioGuide = value

    @property
    def wheel_face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelFaceWidth

        if temp is None:
            return 0.0

        return temp

    @wheel_face_width.setter
    @enforce_parameter_types
    def wheel_face_width(self: Self, value: "float"):
        self.wrapped.WheelFaceWidth = float(value) if value is not None else 0.0

    @property
    def wheel_number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.WheelNumberOfTeeth

        if temp is None:
            return 0

        return temp

    @wheel_number_of_teeth.setter
    @enforce_parameter_types
    def wheel_number_of_teeth(self: Self, value: "int"):
        self.wrapped.WheelNumberOfTeeth = int(value) if value is not None else 0

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearPairCreationOptions._Cast_CylindricalGearPairCreationOptions":
        return self._Cast_CylindricalGearPairCreationOptions(self)
