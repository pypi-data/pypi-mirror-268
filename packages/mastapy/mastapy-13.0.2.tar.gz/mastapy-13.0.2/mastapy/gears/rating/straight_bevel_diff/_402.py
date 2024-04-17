"""StraightBevelDiffGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.conical import _543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.StraightBevelDiff", "StraightBevelDiffGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _969
    from mastapy.gears.rating import _364, _357
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearRating",)


Self = TypeVar("Self", bound="StraightBevelDiffGearRating")


class StraightBevelDiffGearRating(_543.ConicalGearRating):
    """StraightBevelDiffGearRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearRating")

    class _Cast_StraightBevelDiffGearRating:
        """Special nested class for casting StraightBevelDiffGearRating to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearRating._Cast_StraightBevelDiffGearRating",
            parent: "StraightBevelDiffGearRating",
        ):
            self._parent = parent

        @property
        def conical_gear_rating(
            self: "StraightBevelDiffGearRating._Cast_StraightBevelDiffGearRating",
        ) -> "_543.ConicalGearRating":
            return self._parent._cast(_543.ConicalGearRating)

        @property
        def gear_rating(
            self: "StraightBevelDiffGearRating._Cast_StraightBevelDiffGearRating",
        ) -> "_364.GearRating":
            from mastapy.gears.rating import _364

            return self._parent._cast(_364.GearRating)

        @property
        def abstract_gear_rating(
            self: "StraightBevelDiffGearRating._Cast_StraightBevelDiffGearRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "StraightBevelDiffGearRating._Cast_StraightBevelDiffGearRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def straight_bevel_diff_gear_rating(
            self: "StraightBevelDiffGearRating._Cast_StraightBevelDiffGearRating",
        ) -> "StraightBevelDiffGearRating":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearRating._Cast_StraightBevelDiffGearRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cycles_to_fail(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFailContact

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFailContact

        if temp is None:
            return 0.0

        return temp

    @property
    def straight_bevel_diff_gear(self: Self) -> "_969.StraightBevelDiffGearDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearRating._Cast_StraightBevelDiffGearRating":
        return self._Cast_StraightBevelDiffGearRating(self)
