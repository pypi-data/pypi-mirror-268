"""FaceGearWheelDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.face import _993
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_WHEEL_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Face", "FaceGearWheelDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _994
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearWheelDesign",)


Self = TypeVar("Self", bound="FaceGearWheelDesign")


class FaceGearWheelDesign(_993.FaceGearDesign):
    """FaceGearWheelDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_WHEEL_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearWheelDesign")

    class _Cast_FaceGearWheelDesign:
        """Special nested class for casting FaceGearWheelDesign to subclasses."""

        def __init__(
            self: "FaceGearWheelDesign._Cast_FaceGearWheelDesign",
            parent: "FaceGearWheelDesign",
        ):
            self._parent = parent

        @property
        def face_gear_design(
            self: "FaceGearWheelDesign._Cast_FaceGearWheelDesign",
        ) -> "_993.FaceGearDesign":
            return self._parent._cast(_993.FaceGearDesign)

        @property
        def gear_design(
            self: "FaceGearWheelDesign._Cast_FaceGearWheelDesign",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "FaceGearWheelDesign._Cast_FaceGearWheelDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def face_gear_wheel_design(
            self: "FaceGearWheelDesign._Cast_FaceGearWheelDesign",
        ) -> "FaceGearWheelDesign":
            return self._parent

        def __getattr__(
            self: "FaceGearWheelDesign._Cast_FaceGearWheelDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearWheelDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @addendum.setter
    @enforce_parameter_types
    def addendum(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Addendum = value

    @property
    def addendum_from_pitch_line_at_inner_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumFromPitchLineAtInnerEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def addendum_from_pitch_line_at_mid_face(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumFromPitchLineAtMidFace

        if temp is None:
            return 0.0

        return temp

    @property
    def addendum_from_pitch_line_at_outer_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumFromPitchLineAtOuterEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Dedendum

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @dedendum.setter
    @enforce_parameter_types
    def dedendum(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Dedendum = value

    @property
    def dedendum_from_pitch_line_at_inner_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DedendumFromPitchLineAtInnerEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum_from_pitch_line_at_mid_face(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DedendumFromPitchLineAtMidFace

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum_from_pitch_line_at_outer_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DedendumFromPitchLineAtOuterEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidthOffset

        if temp is None:
            return 0.0

        return temp

    @face_width_offset.setter
    @enforce_parameter_types
    def face_width_offset(self: Self, value: "float"):
        self.wrapped.FaceWidthOffset = float(value) if value is not None else 0.0

    @property
    def face_width_and_diameters_specification_method(
        self: Self,
    ) -> "_994.FaceGearDiameterFaceWidthSpecificationMethod":
        """mastapy.gears.gear_designs.face.FaceGearDiameterFaceWidthSpecificationMethod"""
        temp = self.wrapped.FaceWidthAndDiametersSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Face.FaceGearDiameterFaceWidthSpecificationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.face._994",
            "FaceGearDiameterFaceWidthSpecificationMethod",
        )(value)

    @face_width_and_diameters_specification_method.setter
    @enforce_parameter_types
    def face_width_and_diameters_specification_method(
        self: Self, value: "_994.FaceGearDiameterFaceWidthSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Face.FaceGearDiameterFaceWidthSpecificationMethod",
        )
        self.wrapped.FaceWidthAndDiametersSpecificationMethod = value

    @property
    def fillet_radius_at_reference_section(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FilletRadiusAtReferenceSection

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @fillet_radius_at_reference_section.setter
    @enforce_parameter_types
    def fillet_radius_at_reference_section(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FilletRadiusAtReferenceSection = value

    @property
    def inner_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return temp

    @inner_diameter.setter
    @enforce_parameter_types
    def inner_diameter(self: Self, value: "float"):
        self.wrapped.InnerDiameter = float(value) if value is not None else 0.0

    @property
    def mean_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_pitch_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanPitchRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle_at_inner_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPressureAngleAtInnerEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle_at_mid_face(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPressureAngleAtMidFace

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle_at_outer_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPressureAngleAtOuterEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_thickness_at_reference_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalThicknessAtReferenceSection

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "float"):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def profile_shift_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_at_inner_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusAtInnerEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_at_mid_face(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusAtMidFace

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_at_outer_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusAtOuterEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_pitch_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferencePitchRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def rim_thickness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RimThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rim_thickness.setter
    @enforce_parameter_types
    def rim_thickness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RimThickness = value

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
    def cast_to(self: Self) -> "FaceGearWheelDesign._Cast_FaceGearWheelDesign":
        return self._Cast_FaceGearWheelDesign(self)
