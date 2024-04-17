"""SAESplineJointRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.detailed_rigid_connectors.splines.ratings import _1439
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAE_SPLINE_JOINT_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings", "SAESplineJointRating"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.rating import _1443


__docformat__ = "restructuredtext en"
__all__ = ("SAESplineJointRating",)


Self = TypeVar("Self", bound="SAESplineJointRating")


class SAESplineJointRating(_1439.SplineJointRating):
    """SAESplineJointRating

    This is a mastapy class.
    """

    TYPE = _SAE_SPLINE_JOINT_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SAESplineJointRating")

    class _Cast_SAESplineJointRating:
        """Special nested class for casting SAESplineJointRating to subclasses."""

        def __init__(
            self: "SAESplineJointRating._Cast_SAESplineJointRating",
            parent: "SAESplineJointRating",
        ):
            self._parent = parent

        @property
        def spline_joint_rating(
            self: "SAESplineJointRating._Cast_SAESplineJointRating",
        ) -> "_1439.SplineJointRating":
            return self._parent._cast(_1439.SplineJointRating)

        @property
        def shaft_hub_connection_rating(
            self: "SAESplineJointRating._Cast_SAESplineJointRating",
        ) -> "_1443.ShaftHubConnectionRating":
            from mastapy.detailed_rigid_connectors.rating import _1443

            return self._parent._cast(_1443.ShaftHubConnectionRating)

        @property
        def sae_spline_joint_rating(
            self: "SAESplineJointRating._Cast_SAESplineJointRating",
        ) -> "SAESplineJointRating":
            return self._parent

        def __getattr__(
            self: "SAESplineJointRating._Cast_SAESplineJointRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SAESplineJointRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_contact_height(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveContactHeight

        if temp is None:
            return 0.0

        return temp

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
    def calculated_compressive_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_maximum_tooth_shearing_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedMaximumToothShearingStress

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
    def fatigue_life_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueLifeFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def internal_hoop_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InternalHoopStress

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def over_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverLoadFactor

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
    def wear_life_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WearLifeFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "SAESplineJointRating._Cast_SAESplineJointRating":
        return self._Cast_SAESplineJointRating(self)
