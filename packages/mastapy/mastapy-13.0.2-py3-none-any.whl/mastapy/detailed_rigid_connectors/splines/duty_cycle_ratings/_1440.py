"""AGMA6123SplineJointDutyCycleRating"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA6123_SPLINE_JOINT_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.DutyCycleRatings",
    "AGMA6123SplineJointDutyCycleRating",
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMA6123SplineJointDutyCycleRating",)


Self = TypeVar("Self", bound="AGMA6123SplineJointDutyCycleRating")


class AGMA6123SplineJointDutyCycleRating(_0.APIBase):
    """AGMA6123SplineJointDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _AGMA6123_SPLINE_JOINT_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMA6123SplineJointDutyCycleRating")

    class _Cast_AGMA6123SplineJointDutyCycleRating:
        """Special nested class for casting AGMA6123SplineJointDutyCycleRating to subclasses."""

        def __init__(
            self: "AGMA6123SplineJointDutyCycleRating._Cast_AGMA6123SplineJointDutyCycleRating",
            parent: "AGMA6123SplineJointDutyCycleRating",
        ):
            self._parent = parent

        @property
        def agma6123_spline_joint_duty_cycle_rating(
            self: "AGMA6123SplineJointDutyCycleRating._Cast_AGMA6123SplineJointDutyCycleRating",
        ) -> "AGMA6123SplineJointDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "AGMA6123SplineJointDutyCycleRating._Cast_AGMA6123SplineJointDutyCycleRating",
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
        self: Self, instance_to_wrap: "AGMA6123SplineJointDutyCycleRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "AGMA6123SplineJointDutyCycleRating._Cast_AGMA6123SplineJointDutyCycleRating":
        return self._Cast_AGMA6123SplineJointDutyCycleRating(self)
