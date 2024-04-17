"""ISO2812007Results"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2112
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO2812007_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults", "ISO2812007Results"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2108, _2114


__docformat__ = "restructuredtext en"
__all__ = ("ISO2812007Results",)


Self = TypeVar("Self", bound="ISO2812007Results")


class ISO2812007Results(_2112.ISOResults):
    """ISO2812007Results

    This is a mastapy class.
    """

    TYPE = _ISO2812007_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO2812007Results")

    class _Cast_ISO2812007Results:
        """Special nested class for casting ISO2812007Results to subclasses."""

        def __init__(
            self: "ISO2812007Results._Cast_ISO2812007Results",
            parent: "ISO2812007Results",
        ):
            self._parent = parent

        @property
        def iso_results(
            self: "ISO2812007Results._Cast_ISO2812007Results",
        ) -> "_2112.ISOResults":
            return self._parent._cast(_2112.ISOResults)

        @property
        def ball_iso2812007_results(
            self: "ISO2812007Results._Cast_ISO2812007Results",
        ) -> "_2108.BallISO2812007Results":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2108,
            )

            return self._parent._cast(_2108.BallISO2812007Results)

        @property
        def roller_iso2812007_results(
            self: "ISO2812007Results._Cast_ISO2812007Results",
        ) -> "_2114.RollerISO2812007Results":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2114,
            )

            return self._parent._cast(_2114.RollerISO2812007Results)

        @property
        def iso2812007_results(
            self: "ISO2812007Results._Cast_ISO2812007Results",
        ) -> "ISO2812007Results":
            return self._parent

        def __getattr__(self: "ISO2812007Results._Cast_ISO2812007Results", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO2812007Results.TYPE"):
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
    def axial_to_radial_load_ratio_exceeds_iso2812007e_limiting_value_for_dynamic_equivalent_load(
        self: Self,
    ) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AxialToRadialLoadRatioExceedsISO2812007ELimitingValueForDynamicEquivalentLoad
        )

        if temp is None:
            return False

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
    def calculated_viscosity_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedViscosityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def contamination_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContaminationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def contamination_factor_from_calculated_viscosity_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContaminationFactorFromCalculatedViscosityRatio

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
    def life_modification_factor_for_systems_approach_with_calculated_viscosity_ratio(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LifeModificationFactorForSystemsApproachWithCalculatedViscosityRatio
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_rating_life_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedRatingLifeCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_rating_life_damage_rate(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_rating_life_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_kinematic_viscosity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceKinematicViscosity

        if temp is None:
            return 0.0

        return temp

    @property
    def viscosity_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ViscosityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ISO2812007Results._Cast_ISO2812007Results":
        return self._Cast_ISO2812007Results(self)
