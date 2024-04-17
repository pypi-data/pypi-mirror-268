"""LoadedBallBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2041
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedBallBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import (
        _2009,
        _2008,
        _1991,
        _1994,
        _2020,
        _2025,
        _2044,
        _2059,
        _2062,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBallBearingRow",)


Self = TypeVar("Self", bound="LoadedBallBearingRow")


class LoadedBallBearingRow(_2041.LoadedRollingBearingRow):
    """LoadedBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedBallBearingRow")

    class _Cast_LoadedBallBearingRow:
        """Special nested class for casting LoadedBallBearingRow to subclasses."""

        def __init__(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
            parent: "LoadedBallBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2041.LoadedRollingBearingRow":
            return self._parent._cast(_2041.LoadedRollingBearingRow)

        @property
        def loaded_angular_contact_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_1991.LoadedAngularContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _1991

            return self._parent._cast(_1991.LoadedAngularContactBallBearingRow)

        @property
        def loaded_angular_contact_thrust_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_1994.LoadedAngularContactThrustBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _1994

            return self._parent._cast(_1994.LoadedAngularContactThrustBallBearingRow)

        @property
        def loaded_deep_groove_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2020.LoadedDeepGrooveBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2020

            return self._parent._cast(_2020.LoadedDeepGrooveBallBearingRow)

        @property
        def loaded_four_point_contact_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2025.LoadedFourPointContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2025

            return self._parent._cast(_2025.LoadedFourPointContactBallBearingRow)

        @property
        def loaded_self_aligning_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2044.LoadedSelfAligningBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2044

            return self._parent._cast(_2044.LoadedSelfAligningBallBearingRow)

        @property
        def loaded_three_point_contact_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2059.LoadedThreePointContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2059

            return self._parent._cast(_2059.LoadedThreePointContactBallBearingRow)

        @property
        def loaded_thrust_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "_2062.LoadedThrustBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2062

            return self._parent._cast(_2062.LoadedThrustBallBearingRow)

        @property
        def loaded_ball_bearing_row(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow",
        ) -> "LoadedBallBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedBallBearingRow._Cast_LoadedBallBearingRow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedBallBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_ball_movement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialBallMovement

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_with_worst_track_truncation(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementWithWorstTrackTruncation

        if temp is None:
            return ""

        return temp

    @property
    def hertzian_semi_major_dimension_highest_load_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionHighestLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_highest_load_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionHighestLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_highest_load_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionHighestLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_highest_load_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionHighestLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def smallest_arc_distance_of_raceway_edge_to_hertzian_contact(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallestArcDistanceOfRacewayEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def track_truncation_occurring_beyond_permissible_limit(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TrackTruncationOccurringBeyondPermissibleLimit

        if temp is None:
            return False

        return temp

    @property
    def truncation_warning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TruncationWarning

        if temp is None:
            return ""

        return temp

    @property
    def worst_hertzian_ellipse_major_2b_track_truncation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstHertzianEllipseMajor2bTrackTruncation

        if temp is None:
            return 0.0

        return temp

    @property
    def loaded_bearing(self: Self) -> "_2009.LoadedBallBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedBallBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def race_results(self: Self) -> "List[_2008.LoadedBallBearingRaceResults]":
        """List[mastapy.bearings.bearing_results.rolling.LoadedBallBearingRaceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "LoadedBallBearingRow._Cast_LoadedBallBearingRow":
        return self._Cast_LoadedBallBearingRow(self)
