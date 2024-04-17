"""ConicalGearDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _362, _357
    from mastapy.gears.rating.conical import _544, _543
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearDutyCycleRating",)


Self = TypeVar("Self", bound="ConicalGearDutyCycleRating")


class ConicalGearDutyCycleRating(_361.GearDutyCycleRating):
    """ConicalGearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearDutyCycleRating")

    class _Cast_ConicalGearDutyCycleRating:
        """Special nested class for casting ConicalGearDutyCycleRating to subclasses."""

        def __init__(
            self: "ConicalGearDutyCycleRating._Cast_ConicalGearDutyCycleRating",
            parent: "ConicalGearDutyCycleRating",
        ):
            self._parent = parent

        @property
        def gear_duty_cycle_rating(
            self: "ConicalGearDutyCycleRating._Cast_ConicalGearDutyCycleRating",
        ) -> "_361.GearDutyCycleRating":
            return self._parent._cast(_361.GearDutyCycleRating)

        @property
        def abstract_gear_rating(
            self: "ConicalGearDutyCycleRating._Cast_ConicalGearDutyCycleRating",
        ) -> "_357.AbstractGearRating":
            from mastapy.gears.rating import _357

            return self._parent._cast(_357.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearDutyCycleRating._Cast_ConicalGearDutyCycleRating",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def conical_gear_duty_cycle_rating(
            self: "ConicalGearDutyCycleRating._Cast_ConicalGearDutyCycleRating",
        ) -> "ConicalGearDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "ConicalGearDutyCycleRating._Cast_ConicalGearDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concave_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConcaveFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_design_duty_cycle(self: Self) -> "_544.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_set_design_duty_cycle(
        self: Self,
    ) -> "_544.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesignDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def convex_flank_rating(self: Self) -> "_362.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConvexFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratings(self: Self) -> "List[_543.ConicalGearRating]":
        """List[mastapy.gears.rating.conical.ConicalGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_gear_ratings(self: Self) -> "List[_543.ConicalGearRating]":
        """List[mastapy.gears.rating.conical.ConicalGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearDutyCycleRating._Cast_ConicalGearDutyCycleRating":
        return self._Cast_ConicalGearDutyCycleRating(self)
