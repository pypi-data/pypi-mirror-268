"""ISOTS162812008Results"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2112
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISOTS162812008_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults",
    "ISOTS162812008Results",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2109, _2115


__docformat__ = "restructuredtext en"
__all__ = ("ISOTS162812008Results",)


Self = TypeVar("Self", bound="ISOTS162812008Results")


class ISOTS162812008Results(_2112.ISOResults):
    """ISOTS162812008Results

    This is a mastapy class.
    """

    TYPE = _ISOTS162812008_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISOTS162812008Results")

    class _Cast_ISOTS162812008Results:
        """Special nested class for casting ISOTS162812008Results to subclasses."""

        def __init__(
            self: "ISOTS162812008Results._Cast_ISOTS162812008Results",
            parent: "ISOTS162812008Results",
        ):
            self._parent = parent

        @property
        def iso_results(
            self: "ISOTS162812008Results._Cast_ISOTS162812008Results",
        ) -> "_2112.ISOResults":
            return self._parent._cast(_2112.ISOResults)

        @property
        def ball_isots162812008_results(
            self: "ISOTS162812008Results._Cast_ISOTS162812008Results",
        ) -> "_2109.BallISOTS162812008Results":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2109,
            )

            return self._parent._cast(_2109.BallISOTS162812008Results)

        @property
        def roller_isots162812008_results(
            self: "ISOTS162812008Results._Cast_ISOTS162812008Results",
        ) -> "_2115.RollerISOTS162812008Results":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2115,
            )

            return self._parent._cast(_2115.RollerISOTS162812008Results)

        @property
        def isots162812008_results(
            self: "ISOTS162812008Results._Cast_ISOTS162812008Results",
        ) -> "ISOTS162812008Results":
            return self._parent

        def __getattr__(
            self: "ISOTS162812008Results._Cast_ISOTS162812008Results", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISOTS162812008Results.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_reference_rating_life_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicReferenceRatingLifeCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_reference_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicReferenceRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_reference_rating_life_damage_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicReferenceRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_reference_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicReferenceRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_reference_rating_life_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicReferenceRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_reference_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicReferenceRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_reference_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicReferenceRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load_dynamic_capacity_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoadDynamicCapacityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_reference_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentReferenceLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def life_modification_factor_for_systems_approach(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeModificationFactorForSystemsApproach

        if temp is None:
            return 0.0

        return temp

    @property
    def load_for_the_basic_dynamic_load_rating_of_the_inner_ring_or_shaft_washer(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadForTheBasicDynamicLoadRatingOfTheInnerRingOrShaftWasher

        if temp is None:
            return 0.0

        return temp

    @property
    def load_for_the_basic_dynamic_load_rating_of_the_outer_ring_or_housing_washer(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LoadForTheBasicDynamicLoadRatingOfTheOuterRingOrHousingWasher
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_reference_rating_life_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedReferenceRatingLifeCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_reference_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedReferenceRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_reference_rating_life_damage_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedReferenceRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_reference_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedReferenceRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_reference_rating_life_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedReferenceRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_reference_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedReferenceRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_reference_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedReferenceRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ISOTS162812008Results._Cast_ISOTS162812008Results":
        return self._Cast_ISOTS162812008Results(self)
