"""AGMA6123SplineJointRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.detailed_rigid_connectors.splines.ratings import _1439
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA6123_SPLINE_JOINT_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings", "AGMA6123SplineJointRating"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.rating import _1443


__docformat__ = "restructuredtext en"
__all__ = ("AGMA6123SplineJointRating",)


Self = TypeVar("Self", bound="AGMA6123SplineJointRating")


class AGMA6123SplineJointRating(_1439.SplineJointRating):
    """AGMA6123SplineJointRating

    This is a mastapy class.
    """

    TYPE = _AGMA6123_SPLINE_JOINT_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMA6123SplineJointRating")

    class _Cast_AGMA6123SplineJointRating:
        """Special nested class for casting AGMA6123SplineJointRating to subclasses."""

        def __init__(
            self: "AGMA6123SplineJointRating._Cast_AGMA6123SplineJointRating",
            parent: "AGMA6123SplineJointRating",
        ):
            self._parent = parent

        @property
        def spline_joint_rating(
            self: "AGMA6123SplineJointRating._Cast_AGMA6123SplineJointRating",
        ) -> "_1439.SplineJointRating":
            return self._parent._cast(_1439.SplineJointRating)

        @property
        def shaft_hub_connection_rating(
            self: "AGMA6123SplineJointRating._Cast_AGMA6123SplineJointRating",
        ) -> "_1443.ShaftHubConnectionRating":
            from mastapy.detailed_rigid_connectors.rating import _1443

            return self._parent._cast(_1443.ShaftHubConnectionRating)

        @property
        def agma6123_spline_joint_rating(
            self: "AGMA6123SplineJointRating._Cast_AGMA6123SplineJointRating",
        ) -> "AGMA6123SplineJointRating":
            return self._parent

        def __getattr__(
            self: "AGMA6123SplineJointRating._Cast_AGMA6123SplineJointRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMA6123SplineJointRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_ring_bursting_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableRingBurstingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_stress_for_shearing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStressForShearing

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_torque_for_torsional_failure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableTorqueForTorsionalFailure

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_torque_for_wear_and_fretting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableTorqueForWearAndFretting

        if temp is None:
            return 0.0

        return temp

    @property
    def bursting_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BurstingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def centrifugal_hoop_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentrifugalHoopStress

        if temp is None:
            return 0.0

        return temp

    @property
    def diameter_at_half_the_working_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterAtHalfTheWorkingDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @load_distribution_factor.setter
    @enforce_parameter_types
    def load_distribution_factor(self: Self, value: "float"):
        self.wrapped.LoadDistributionFactor = float(value) if value is not None else 0.0

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
    def safety_factor_for_ring_bursting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForRingBursting

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_shearing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForShearing

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_torsional_failure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForTorsionalFailure

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_wear_and_fretting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForWearAndFretting

        if temp is None:
            return 0.0

        return temp

    @property
    def tensile_tooth_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TensileToothBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def total_tensile_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalTensileStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "AGMA6123SplineJointRating._Cast_AGMA6123SplineJointRating":
        return self._Cast_AGMA6123SplineJointRating(self)
