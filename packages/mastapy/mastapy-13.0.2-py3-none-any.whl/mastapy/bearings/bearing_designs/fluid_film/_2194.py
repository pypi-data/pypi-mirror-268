"""PadFluidFilmBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings import _1904
from mastapy.bearings.bearing_designs import _2138
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PAD_FLUID_FILM_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "PadFluidFilmBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.fluid_film import _2201, _2202
    from mastapy.bearings.bearing_designs import _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("PadFluidFilmBearing",)


Self = TypeVar("Self", bound="PadFluidFilmBearing")


class PadFluidFilmBearing(_2138.DetailedBearing):
    """PadFluidFilmBearing

    This is a mastapy class.
    """

    TYPE = _PAD_FLUID_FILM_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PadFluidFilmBearing")

    class _Cast_PadFluidFilmBearing:
        """Special nested class for casting PadFluidFilmBearing to subclasses."""

        def __init__(
            self: "PadFluidFilmBearing._Cast_PadFluidFilmBearing",
            parent: "PadFluidFilmBearing",
        ):
            self._parent = parent

        @property
        def detailed_bearing(
            self: "PadFluidFilmBearing._Cast_PadFluidFilmBearing",
        ) -> "_2138.DetailedBearing":
            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "PadFluidFilmBearing._Cast_PadFluidFilmBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "PadFluidFilmBearing._Cast_PadFluidFilmBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def tilting_pad_journal_bearing(
            self: "PadFluidFilmBearing._Cast_PadFluidFilmBearing",
        ) -> "_2201.TiltingPadJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2201

            return self._parent._cast(_2201.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(
            self: "PadFluidFilmBearing._Cast_PadFluidFilmBearing",
        ) -> "_2202.TiltingPadThrustBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2202

            return self._parent._cast(_2202.TiltingPadThrustBearing)

        @property
        def pad_fluid_film_bearing(
            self: "PadFluidFilmBearing._Cast_PadFluidFilmBearing",
        ) -> "PadFluidFilmBearing":
            return self._parent

        def __getattr__(
            self: "PadFluidFilmBearing._Cast_PadFluidFilmBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PadFluidFilmBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def collar_surface_roughness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CollarSurfaceRoughness

        if temp is None:
            return 0.0

        return temp

    @collar_surface_roughness.setter
    @enforce_parameter_types
    def collar_surface_roughness(self: Self, value: "float"):
        self.wrapped.CollarSurfaceRoughness = float(value) if value is not None else 0.0

    @property
    def limiting_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitingFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_pads(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfPads

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_pads.setter
    @enforce_parameter_types
    def number_of_pads(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfPads = value

    @property
    def pad_angular_extent(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PadAngularExtent

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pad_angular_extent.setter
    @enforce_parameter_types
    def pad_angular_extent(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PadAngularExtent = value

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
    def rotational_direction(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_RotationalDirections":
        """EnumWithSelectedValue[mastapy.bearings.RotationalDirections]"""
        temp = self.wrapped.RotationalDirection

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RotationalDirections.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @rotational_direction.setter
    @enforce_parameter_types
    def rotational_direction(self: Self, value: "_1904.RotationalDirections"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RotationalDirections.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RotationalDirection = value

    @property
    def cast_to(self: Self) -> "PadFluidFilmBearing._Cast_PadFluidFilmBearing":
        return self._Cast_PadFluidFilmBearing(self)
