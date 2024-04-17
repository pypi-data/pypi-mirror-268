"""PlainOilFedJournalBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.fluid_film import _2198
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLAIN_OIL_FED_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "PlainOilFedJournalBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1894
    from mastapy.bearings.bearing_designs.fluid_film import _2189, _2190, _2191
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("PlainOilFedJournalBearing",)


Self = TypeVar("Self", bound="PlainOilFedJournalBearing")


class PlainOilFedJournalBearing(_2198.PlainJournalBearing):
    """PlainOilFedJournalBearing

    This is a mastapy class.
    """

    TYPE = _PLAIN_OIL_FED_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlainOilFedJournalBearing")

    class _Cast_PlainOilFedJournalBearing:
        """Special nested class for casting PlainOilFedJournalBearing to subclasses."""

        def __init__(
            self: "PlainOilFedJournalBearing._Cast_PlainOilFedJournalBearing",
            parent: "PlainOilFedJournalBearing",
        ):
            self._parent = parent

        @property
        def plain_journal_bearing(
            self: "PlainOilFedJournalBearing._Cast_PlainOilFedJournalBearing",
        ) -> "_2198.PlainJournalBearing":
            return self._parent._cast(_2198.PlainJournalBearing)

        @property
        def detailed_bearing(
            self: "PlainOilFedJournalBearing._Cast_PlainOilFedJournalBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "PlainOilFedJournalBearing._Cast_PlainOilFedJournalBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "PlainOilFedJournalBearing._Cast_PlainOilFedJournalBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def plain_oil_fed_journal_bearing(
            self: "PlainOilFedJournalBearing._Cast_PlainOilFedJournalBearing",
        ) -> "PlainOilFedJournalBearing":
            return self._parent

        def __getattr__(
            self: "PlainOilFedJournalBearing._Cast_PlainOilFedJournalBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlainOilFedJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def feed_type(self: Self) -> "_1894.JournalOilFeedType":
        """mastapy.bearings.JournalOilFeedType"""
        temp = self.wrapped.FeedType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.JournalOilFeedType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1894", "JournalOilFeedType"
        )(value)

    @feed_type.setter
    @enforce_parameter_types
    def feed_type(self: Self, value: "_1894.JournalOilFeedType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.JournalOilFeedType"
        )
        self.wrapped.FeedType = value

    @property
    def land_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LandWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_axial_points_for_pressure_distribution(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfAxialPointsForPressureDistribution

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_axial_points_for_pressure_distribution.setter
    @enforce_parameter_types
    def number_of_axial_points_for_pressure_distribution(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfAxialPointsForPressureDistribution = value

    @property
    def number_of_circumferential_points_for_pressure_distribution(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfCircumferentialPointsForPressureDistribution

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_circumferential_points_for_pressure_distribution.setter
    @enforce_parameter_types
    def number_of_circumferential_points_for_pressure_distribution(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfCircumferentialPointsForPressureDistribution = value

    @property
    def axial_groove_oil_feed(self: Self) -> "_2189.AxialGrooveJournalBearing":
        """mastapy.bearings.bearing_designs.fluid_film.AxialGrooveJournalBearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialGrooveOilFeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def axial_hole_oil_feed(self: Self) -> "_2190.AxialHoleJournalBearing":
        """mastapy.bearings.bearing_designs.fluid_film.AxialHoleJournalBearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialHoleOilFeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def circumferential_groove_oil_feed(
        self: Self,
    ) -> "_2191.CircumferentialFeedJournalBearing":
        """mastapy.bearings.bearing_designs.fluid_film.CircumferentialFeedJournalBearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CircumferentialGrooveOilFeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlainOilFedJournalBearing._Cast_PlainOilFedJournalBearing":
        return self._Cast_PlainOilFedJournalBearing(self)
