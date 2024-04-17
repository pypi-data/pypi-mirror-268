"""TrackTruncationSafetyFactorResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRACK_TRUNCATION_SAFETY_FACTOR_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "TrackTruncationSafetyFactorResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("TrackTruncationSafetyFactorResults",)


Self = TypeVar("Self", bound="TrackTruncationSafetyFactorResults")


class TrackTruncationSafetyFactorResults(_0.APIBase):
    """TrackTruncationSafetyFactorResults

    This is a mastapy class.
    """

    TYPE = _TRACK_TRUNCATION_SAFETY_FACTOR_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TrackTruncationSafetyFactorResults")

    class _Cast_TrackTruncationSafetyFactorResults:
        """Special nested class for casting TrackTruncationSafetyFactorResults to subclasses."""

        def __init__(
            self: "TrackTruncationSafetyFactorResults._Cast_TrackTruncationSafetyFactorResults",
            parent: "TrackTruncationSafetyFactorResults",
        ):
            self._parent = parent

        @property
        def track_truncation_safety_factor_results(
            self: "TrackTruncationSafetyFactorResults._Cast_TrackTruncationSafetyFactorResults",
        ) -> "TrackTruncationSafetyFactorResults":
            return self._parent

        def __getattr__(
            self: "TrackTruncationSafetyFactorResults._Cast_TrackTruncationSafetyFactorResults",
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
        self: Self, instance_to_wrap: "TrackTruncationSafetyFactorResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactor

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
    def worst_hertzian_ellipse_major_2b_track_truncation_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstHertzianEllipseMajor2bTrackTruncationInner

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_hertzian_ellipse_major_2b_track_truncation_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstHertzianEllipseMajor2bTrackTruncationOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "TrackTruncationSafetyFactorResults._Cast_TrackTruncationSafetyFactorResults":
        return self._Cast_TrackTruncationSafetyFactorResults(self)
