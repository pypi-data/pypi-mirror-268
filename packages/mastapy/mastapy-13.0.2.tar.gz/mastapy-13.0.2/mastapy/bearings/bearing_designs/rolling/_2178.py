"""TaperRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.rolling import _2168
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TAPER_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "TaperRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1883
    from mastapy.bearings.bearing_designs.rolling import _2169, _2172
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("TaperRollerBearing",)


Self = TypeVar("Self", bound="TaperRollerBearing")


class TaperRollerBearing(_2168.NonBarrelRollerBearing):
    """TaperRollerBearing

    This is a mastapy class.
    """

    TYPE = _TAPER_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TaperRollerBearing")

    class _Cast_TaperRollerBearing:
        """Special nested class for casting TaperRollerBearing to subclasses."""

        def __init__(
            self: "TaperRollerBearing._Cast_TaperRollerBearing",
            parent: "TaperRollerBearing",
        ):
            self._parent = parent

        @property
        def non_barrel_roller_bearing(
            self: "TaperRollerBearing._Cast_TaperRollerBearing",
        ) -> "_2168.NonBarrelRollerBearing":
            return self._parent._cast(_2168.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "TaperRollerBearing._Cast_TaperRollerBearing",
        ) -> "_2169.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.RollerBearing)

        @property
        def rolling_bearing(
            self: "TaperRollerBearing._Cast_TaperRollerBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def detailed_bearing(
            self: "TaperRollerBearing._Cast_TaperRollerBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "TaperRollerBearing._Cast_TaperRollerBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "TaperRollerBearing._Cast_TaperRollerBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def taper_roller_bearing(
            self: "TaperRollerBearing._Cast_TaperRollerBearing",
        ) -> "TaperRollerBearing":
            return self._parent

        def __getattr__(self: "TaperRollerBearing._Cast_TaperRollerBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TaperRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembled_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AssembledWidth

        if temp is None:
            return 0.0

        return temp

    @assembled_width.setter
    @enforce_parameter_types
    def assembled_width(self: Self, value: "float"):
        self.wrapped.AssembledWidth = float(value) if value is not None else 0.0

    @property
    def bearing_measurement_type(self: Self) -> "_1883.BearingMeasurementType":
        """mastapy.bearings.BearingMeasurementType"""
        temp = self.wrapped.BearingMeasurementType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingMeasurementType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1883", "BearingMeasurementType"
        )(value)

    @bearing_measurement_type.setter
    @enforce_parameter_types
    def bearing_measurement_type(self: Self, value: "_1883.BearingMeasurementType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingMeasurementType"
        )
        self.wrapped.BearingMeasurementType = value

    @property
    def cone_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ConeAngle

        if temp is None:
            return 0.0

        return temp

    @cone_angle.setter
    @enforce_parameter_types
    def cone_angle(self: Self, value: "float"):
        self.wrapped.ConeAngle = float(value) if value is not None else 0.0

    @property
    def cup_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CupAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cup_angle.setter
    @enforce_parameter_types
    def cup_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CupAngle = value

    @property
    def effective_centre_from_front_face(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EffectiveCentreFromFrontFace

        if temp is None:
            return 0.0

        return temp

    @effective_centre_from_front_face.setter
    @enforce_parameter_types
    def effective_centre_from_front_face(self: Self, value: "float"):
        self.wrapped.EffectiveCentreFromFrontFace = (
            float(value) if value is not None else 0.0
        )

    @property
    def effective_centre_to_front_face_set_by_changing_outer_ring_offset(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.EffectiveCentreToFrontFaceSetByChangingOuterRingOffset

        if temp is None:
            return 0.0

        return temp

    @effective_centre_to_front_face_set_by_changing_outer_ring_offset.setter
    @enforce_parameter_types
    def effective_centre_to_front_face_set_by_changing_outer_ring_offset(
        self: Self, value: "float"
    ):
        self.wrapped.EffectiveCentreToFrontFaceSetByChangingOuterRingOffset = (
            float(value) if value is not None else 0.0
        )

    @property
    def element_taper_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementTaperAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_taper_angle.setter
    @enforce_parameter_types
    def element_taper_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementTaperAngle = value

    @property
    def inner_ring_back_face_corner_radius(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRingBackFaceCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_ring_back_face_corner_radius.setter
    @enforce_parameter_types
    def inner_ring_back_face_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRingBackFaceCornerRadius = value

    @property
    def inner_ring_front_face_corner_radius(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRingFrontFaceCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_ring_front_face_corner_radius.setter
    @enforce_parameter_types
    def inner_ring_front_face_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRingFrontFaceCornerRadius = value

    @property
    def left_element_corner_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LeftElementCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @left_element_corner_radius.setter
    @enforce_parameter_types
    def left_element_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LeftElementCornerRadius = value

    @property
    def mean_inner_race_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanInnerRaceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_outer_race_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanOuterRaceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_ring_back_face_corner_radius(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRingBackFaceCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_ring_back_face_corner_radius.setter
    @enforce_parameter_types
    def outer_ring_back_face_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRingBackFaceCornerRadius = value

    @property
    def outer_ring_front_face_corner_radius(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRingFrontFaceCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_ring_front_face_corner_radius.setter
    @enforce_parameter_types
    def outer_ring_front_face_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRingFrontFaceCornerRadius = value

    @property
    def right_element_corner_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RightElementCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @right_element_corner_radius.setter
    @enforce_parameter_types
    def right_element_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RightElementCornerRadius = value

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def width_setting_inner_and_outer_ring_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WidthSettingInnerAndOuterRingWidth

        if temp is None:
            return 0.0

        return temp

    @width_setting_inner_and_outer_ring_width.setter
    @enforce_parameter_types
    def width_setting_inner_and_outer_ring_width(self: Self, value: "float"):
        self.wrapped.WidthSettingInnerAndOuterRingWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "TaperRollerBearing._Cast_TaperRollerBearing":
        return self._Cast_TaperRollerBearing(self)
