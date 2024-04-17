"""TiltingPadJournalBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.fluid_film import _2194
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TILTING_PAD_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "TiltingPadJournalBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("TiltingPadJournalBearing",)


Self = TypeVar("Self", bound="TiltingPadJournalBearing")


class TiltingPadJournalBearing(_2194.PadFluidFilmBearing):
    """TiltingPadJournalBearing

    This is a mastapy class.
    """

    TYPE = _TILTING_PAD_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TiltingPadJournalBearing")

    class _Cast_TiltingPadJournalBearing:
        """Special nested class for casting TiltingPadJournalBearing to subclasses."""

        def __init__(
            self: "TiltingPadJournalBearing._Cast_TiltingPadJournalBearing",
            parent: "TiltingPadJournalBearing",
        ):
            self._parent = parent

        @property
        def pad_fluid_film_bearing(
            self: "TiltingPadJournalBearing._Cast_TiltingPadJournalBearing",
        ) -> "_2194.PadFluidFilmBearing":
            return self._parent._cast(_2194.PadFluidFilmBearing)

        @property
        def detailed_bearing(
            self: "TiltingPadJournalBearing._Cast_TiltingPadJournalBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "TiltingPadJournalBearing._Cast_TiltingPadJournalBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "TiltingPadJournalBearing._Cast_TiltingPadJournalBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def tilting_pad_journal_bearing(
            self: "TiltingPadJournalBearing._Cast_TiltingPadJournalBearing",
        ) -> "TiltingPadJournalBearing":
            return self._parent

        def __getattr__(
            self: "TiltingPadJournalBearing._Cast_TiltingPadJournalBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TiltingPadJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bearing_aspect_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingAspectRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def difference_between_pad_contact_surface_radius_and_bearing_inner_radius(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DifferenceBetweenPadContactSurfaceRadiusAndBearingInnerRadius
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_contact_surface_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PadContactSurfaceRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pad_contact_surface_radius.setter
    @enforce_parameter_types
    def pad_contact_surface_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PadContactSurfaceRadius = value

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
    def cast_to(
        self: Self,
    ) -> "TiltingPadJournalBearing._Cast_TiltingPadJournalBearing":
        return self._Cast_TiltingPadJournalBearing(self)
