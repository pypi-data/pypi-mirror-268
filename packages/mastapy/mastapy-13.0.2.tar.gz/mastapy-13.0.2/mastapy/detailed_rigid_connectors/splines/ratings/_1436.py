"""SAESplineHalfRating"""

from __future__ import annotations

from typing import TypeVar

from mastapy.detailed_rigid_connectors.splines.ratings import _1438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAE_SPLINE_HALF_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings", "SAESplineHalfRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("SAESplineHalfRating",)


Self = TypeVar("Self", bound="SAESplineHalfRating")


class SAESplineHalfRating(_1438.SplineHalfRating):
    """SAESplineHalfRating

    This is a mastapy class.
    """

    TYPE = _SAE_SPLINE_HALF_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SAESplineHalfRating")

    class _Cast_SAESplineHalfRating:
        """Special nested class for casting SAESplineHalfRating to subclasses."""

        def __init__(
            self: "SAESplineHalfRating._Cast_SAESplineHalfRating",
            parent: "SAESplineHalfRating",
        ):
            self._parent = parent

        @property
        def spline_half_rating(
            self: "SAESplineHalfRating._Cast_SAESplineHalfRating",
        ) -> "_1438.SplineHalfRating":
            return self._parent._cast(_1438.SplineHalfRating)

        @property
        def sae_spline_half_rating(
            self: "SAESplineHalfRating._Cast_SAESplineHalfRating",
        ) -> "SAESplineHalfRating":
            return self._parent

        def __getattr__(
            self: "SAESplineHalfRating._Cast_SAESplineHalfRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SAESplineHalfRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_compressive_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_shear_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_tensile_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableTensileStress

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentStress

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_damage_for_compressive_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueDamageForCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_damage_for_equivalent_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueDamageForEquivalentRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_damage_for_tooth_shearing_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueDamageForToothShearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_allowable_compressive_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumAllowableCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_allowable_shear_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumAllowableShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def root_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_compressive_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_equivalent_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForEquivalentRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_tooth_shearing_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForToothShearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_concentration_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressConcentrationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_shear_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorsionalShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "SAESplineHalfRating._Cast_SAESplineHalfRating":
        return self._Cast_SAESplineHalfRating(self)
