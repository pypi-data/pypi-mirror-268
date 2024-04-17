"""FaceGearPinionDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.face import _993
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_PINION_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Face", "FaceGearPinionDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearPinionDesign",)


Self = TypeVar("Self", bound="FaceGearPinionDesign")


class FaceGearPinionDesign(_993.FaceGearDesign):
    """FaceGearPinionDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_PINION_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearPinionDesign")

    class _Cast_FaceGearPinionDesign:
        """Special nested class for casting FaceGearPinionDesign to subclasses."""

        def __init__(
            self: "FaceGearPinionDesign._Cast_FaceGearPinionDesign",
            parent: "FaceGearPinionDesign",
        ):
            self._parent = parent

        @property
        def face_gear_design(
            self: "FaceGearPinionDesign._Cast_FaceGearPinionDesign",
        ) -> "_993.FaceGearDesign":
            return self._parent._cast(_993.FaceGearDesign)

        @property
        def gear_design(
            self: "FaceGearPinionDesign._Cast_FaceGearPinionDesign",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "FaceGearPinionDesign._Cast_FaceGearPinionDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def face_gear_pinion_design(
            self: "FaceGearPinionDesign._Cast_FaceGearPinionDesign",
        ) -> "FaceGearPinionDesign":
            return self._parent

        def __getattr__(
            self: "FaceGearPinionDesign._Cast_FaceGearPinionDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearPinionDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def base_thickness_half_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseThicknessHalfAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def fillet_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FilletRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @fillet_radius.setter
    @enforce_parameter_types
    def fillet_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FilletRadius = value

    @property
    def normal_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_cone_angle_with_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchConeAngleWithGear

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_shift_coefficient(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @profile_shift_coefficient.setter
    @enforce_parameter_types
    def profile_shift_coefficient(self: Self, value: "float"):
        self.wrapped.ProfileShiftCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def root_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @root_diameter.setter
    @enforce_parameter_types
    def root_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RootDiameter = value

    @property
    def tip_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tip_diameter.setter
    @enforce_parameter_types
    def tip_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TipDiameter = value

    @property
    def whole_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "FaceGearPinionDesign._Cast_FaceGearPinionDesign":
        return self._Cast_FaceGearPinionDesign(self)
