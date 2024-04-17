"""AGMA6123SplineHalfRating"""

from __future__ import annotations

from typing import TypeVar

from mastapy.detailed_rigid_connectors.splines.ratings import _1438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA6123_SPLINE_HALF_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings", "AGMA6123SplineHalfRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMA6123SplineHalfRating",)


Self = TypeVar("Self", bound="AGMA6123SplineHalfRating")


class AGMA6123SplineHalfRating(_1438.SplineHalfRating):
    """AGMA6123SplineHalfRating

    This is a mastapy class.
    """

    TYPE = _AGMA6123_SPLINE_HALF_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMA6123SplineHalfRating")

    class _Cast_AGMA6123SplineHalfRating:
        """Special nested class for casting AGMA6123SplineHalfRating to subclasses."""

        def __init__(
            self: "AGMA6123SplineHalfRating._Cast_AGMA6123SplineHalfRating",
            parent: "AGMA6123SplineHalfRating",
        ):
            self._parent = parent

        @property
        def spline_half_rating(
            self: "AGMA6123SplineHalfRating._Cast_AGMA6123SplineHalfRating",
        ) -> "_1438.SplineHalfRating":
            return self._parent._cast(_1438.SplineHalfRating)

        @property
        def agma6123_spline_half_rating(
            self: "AGMA6123SplineHalfRating._Cast_AGMA6123SplineHalfRating",
        ) -> "AGMA6123SplineHalfRating":
            return self._parent

        def __getattr__(
            self: "AGMA6123SplineHalfRating._Cast_AGMA6123SplineHalfRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMA6123SplineHalfRating.TYPE"):
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
    def allowable_stress_for_bursting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStressForBursting

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
    def allowable_torque_for_shearing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableTorqueForShearing

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
    ) -> "AGMA6123SplineHalfRating._Cast_AGMA6123SplineHalfRating":
        return self._Cast_AGMA6123SplineHalfRating(self)
