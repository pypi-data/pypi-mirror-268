"""ANSIABMAResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2112
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANSIABMA_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.ABMA", "ANSIABMAResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.abma import _2122, _2123


__docformat__ = "restructuredtext en"
__all__ = ("ANSIABMAResults",)


Self = TypeVar("Self", bound="ANSIABMAResults")


class ANSIABMAResults(_2112.ISOResults):
    """ANSIABMAResults

    This is a mastapy class.
    """

    TYPE = _ANSIABMA_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ANSIABMAResults")

    class _Cast_ANSIABMAResults:
        """Special nested class for casting ANSIABMAResults to subclasses."""

        def __init__(
            self: "ANSIABMAResults._Cast_ANSIABMAResults", parent: "ANSIABMAResults"
        ):
            self._parent = parent

        @property
        def iso_results(
            self: "ANSIABMAResults._Cast_ANSIABMAResults",
        ) -> "_2112.ISOResults":
            return self._parent._cast(_2112.ISOResults)

        @property
        def ansiabma112014_results(
            self: "ANSIABMAResults._Cast_ANSIABMAResults",
        ) -> "_2122.ANSIABMA112014Results":
            from mastapy.bearings.bearing_results.rolling.abma import _2122

            return self._parent._cast(_2122.ANSIABMA112014Results)

        @property
        def ansiabma92015_results(
            self: "ANSIABMAResults._Cast_ANSIABMAResults",
        ) -> "_2123.ANSIABMA92015Results":
            from mastapy.bearings.bearing_results.rolling.abma import _2123

            return self._parent._cast(_2123.ANSIABMA92015Results)

        @property
        def ansiabma_results(
            self: "ANSIABMAResults._Cast_ANSIABMAResults",
        ) -> "ANSIABMAResults":
            return self._parent

        def __getattr__(self: "ANSIABMAResults._Cast_ANSIABMAResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ANSIABMAResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def e_limiting_value_for_dynamic_equivalent_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ELimitingValueForDynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedRatingLifeCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_damage_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_to_radial_load_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialToRadialLoadRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRatingLifeCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_damage_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def bearing_life_adjustment_factor_for_operating_conditions(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingLifeAdjustmentFactorForOperatingConditions

        if temp is None:
            return 0.0

        return temp

    @property
    def bearing_life_adjustment_factor_for_special_bearing_properties(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingLifeAdjustmentFactorForSpecialBearingProperties

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_axial_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicAxialLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_radial_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicRadialLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def static_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ANSIABMAResults._Cast_ANSIABMAResults":
        return self._Cast_ANSIABMAResults(self)
