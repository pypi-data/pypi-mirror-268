"""TiltingPadThrustBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_designs.fluid_film import _2194
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TILTING_PAD_THRUST_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "TiltingPadThrustBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1907
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("TiltingPadThrustBearing",)


Self = TypeVar("Self", bound="TiltingPadThrustBearing")


class TiltingPadThrustBearing(_2194.PadFluidFilmBearing):
    """TiltingPadThrustBearing

    This is a mastapy class.
    """

    TYPE = _TILTING_PAD_THRUST_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TiltingPadThrustBearing")

    class _Cast_TiltingPadThrustBearing:
        """Special nested class for casting TiltingPadThrustBearing to subclasses."""

        def __init__(
            self: "TiltingPadThrustBearing._Cast_TiltingPadThrustBearing",
            parent: "TiltingPadThrustBearing",
        ):
            self._parent = parent

        @property
        def pad_fluid_film_bearing(
            self: "TiltingPadThrustBearing._Cast_TiltingPadThrustBearing",
        ) -> "_2194.PadFluidFilmBearing":
            return self._parent._cast(_2194.PadFluidFilmBearing)

        @property
        def detailed_bearing(
            self: "TiltingPadThrustBearing._Cast_TiltingPadThrustBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "TiltingPadThrustBearing._Cast_TiltingPadThrustBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "TiltingPadThrustBearing._Cast_TiltingPadThrustBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def tilting_pad_thrust_bearing(
            self: "TiltingPadThrustBearing._Cast_TiltingPadThrustBearing",
        ) -> "TiltingPadThrustBearing":
            return self._parent

        def __getattr__(
            self: "TiltingPadThrustBearing._Cast_TiltingPadThrustBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TiltingPadThrustBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def non_dimensional_friction(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonDimensionalFriction

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_dimensional_friction.setter
    @enforce_parameter_types
    def non_dimensional_friction(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonDimensionalFriction = value

    @property
    def non_dimensional_inlet_flow(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonDimensionalInletFlow

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_dimensional_inlet_flow.setter
    @enforce_parameter_types
    def non_dimensional_inlet_flow(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonDimensionalInletFlow = value

    @property
    def non_dimensional_load(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonDimensionalLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_dimensional_load.setter
    @enforce_parameter_types
    def non_dimensional_load(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonDimensionalLoad = value

    @property
    def non_dimensional_minimum_film_thickness(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonDimensionalMinimumFilmThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_dimensional_minimum_film_thickness.setter
    @enforce_parameter_types
    def non_dimensional_minimum_film_thickness(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonDimensionalMinimumFilmThickness = value

    @property
    def non_dimensional_side_flow(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonDimensionalSideFlow

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_dimensional_side_flow.setter
    @enforce_parameter_types
    def non_dimensional_side_flow(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonDimensionalSideFlow = value

    @property
    def pad_circumferential_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PadCircumferentialWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_height(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PadHeight

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_height_aspect_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PadHeightAspectRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_inner_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PadInnerDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pad_inner_diameter.setter
    @enforce_parameter_types
    def pad_inner_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PadInnerDiameter = value

    @property
    def pad_outer_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PadOuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pad_outer_diameter.setter
    @enforce_parameter_types
    def pad_outer_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PadOuterDiameter = value

    @property
    def pad_width_aspect_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PadWidthAspectRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def pivot_angular_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PivotAngularOffset

        if temp is None:
            return 0.0

        return temp

    @pivot_angular_offset.setter
    @enforce_parameter_types
    def pivot_angular_offset(self: Self, value: "float"):
        self.wrapped.PivotAngularOffset = float(value) if value is not None else 0.0

    @property
    def tilting_pad_type(self: Self) -> "_1907.TiltingPadTypes":
        """mastapy.bearings.TiltingPadTypes"""
        temp = self.wrapped.TiltingPadType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bearings.TiltingPadTypes")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1907", "TiltingPadTypes"
        )(value)

    @tilting_pad_type.setter
    @enforce_parameter_types
    def tilting_pad_type(self: Self, value: "_1907.TiltingPadTypes"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Bearings.TiltingPadTypes")
        self.wrapped.TiltingPadType = value

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
    def cast_to(self: Self) -> "TiltingPadThrustBearing._Cast_TiltingPadThrustBearing":
        return self._Cast_TiltingPadThrustBearing(self)
