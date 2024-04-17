"""GBT17855SplineHalfRating"""

from __future__ import annotations

from typing import TypeVar

from mastapy.detailed_rigid_connectors.splines.ratings import _1438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GBT17855_SPLINE_HALF_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings", "GBT17855SplineHalfRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("GBT17855SplineHalfRating",)


Self = TypeVar("Self", bound="GBT17855SplineHalfRating")


class GBT17855SplineHalfRating(_1438.SplineHalfRating):
    """GBT17855SplineHalfRating

    This is a mastapy class.
    """

    TYPE = _GBT17855_SPLINE_HALF_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GBT17855SplineHalfRating")

    class _Cast_GBT17855SplineHalfRating:
        """Special nested class for casting GBT17855SplineHalfRating to subclasses."""

        def __init__(
            self: "GBT17855SplineHalfRating._Cast_GBT17855SplineHalfRating",
            parent: "GBT17855SplineHalfRating",
        ):
            self._parent = parent

        @property
        def spline_half_rating(
            self: "GBT17855SplineHalfRating._Cast_GBT17855SplineHalfRating",
        ) -> "_1438.SplineHalfRating":
            return self._parent._cast(_1438.SplineHalfRating)

        @property
        def gbt17855_spline_half_rating(
            self: "GBT17855SplineHalfRating._Cast_GBT17855SplineHalfRating",
        ) -> "GBT17855SplineHalfRating":
            return self._parent

        def __getattr__(
            self: "GBT17855SplineHalfRating._Cast_GBT17855SplineHalfRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GBT17855SplineHalfRating.TYPE"):
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
    def allowable_root_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_tooth_shearing_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableToothShearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_wearing_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableWearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_compressive_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_root_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_tooth_shearing_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleToothShearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_wearing_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleWearingStress

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
    def safety_factor_for_equivalent_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForEquivalentStress

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_root_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForRootBendingStress

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
    def safety_factor_for_wearing_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForWearingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "GBT17855SplineHalfRating._Cast_GBT17855SplineHalfRating":
        return self._Cast_GBT17855SplineHalfRating(self)
