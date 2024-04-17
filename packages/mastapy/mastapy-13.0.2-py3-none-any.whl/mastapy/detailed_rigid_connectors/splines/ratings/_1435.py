"""GBT17855SplineJointRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.detailed_rigid_connectors.splines.ratings import _1439
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GBT17855_SPLINE_JOINT_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings", "GBT17855SplineJointRating"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.rating import _1443


__docformat__ = "restructuredtext en"
__all__ = ("GBT17855SplineJointRating",)


Self = TypeVar("Self", bound="GBT17855SplineJointRating")


class GBT17855SplineJointRating(_1439.SplineJointRating):
    """GBT17855SplineJointRating

    This is a mastapy class.
    """

    TYPE = _GBT17855_SPLINE_JOINT_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GBT17855SplineJointRating")

    class _Cast_GBT17855SplineJointRating:
        """Special nested class for casting GBT17855SplineJointRating to subclasses."""

        def __init__(
            self: "GBT17855SplineJointRating._Cast_GBT17855SplineJointRating",
            parent: "GBT17855SplineJointRating",
        ):
            self._parent = parent

        @property
        def spline_joint_rating(
            self: "GBT17855SplineJointRating._Cast_GBT17855SplineJointRating",
        ) -> "_1439.SplineJointRating":
            return self._parent._cast(_1439.SplineJointRating)

        @property
        def shaft_hub_connection_rating(
            self: "GBT17855SplineJointRating._Cast_GBT17855SplineJointRating",
        ) -> "_1443.ShaftHubConnectionRating":
            from mastapy.detailed_rigid_connectors.rating import _1443

            return self._parent._cast(_1443.ShaftHubConnectionRating)

        @property
        def gbt17855_spline_joint_rating(
            self: "GBT17855SplineJointRating._Cast_GBT17855SplineJointRating",
        ) -> "GBT17855SplineJointRating":
            return self._parent

        def __getattr__(
            self: "GBT17855SplineJointRating._Cast_GBT17855SplineJointRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GBT17855SplineJointRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def application_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApplicationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def backlash_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BacklashFactor

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
    def calculated_root_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def distribution_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DistributionFactor

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
    def face_load_distribution_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceLoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def k_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KFactor

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
    ) -> "GBT17855SplineJointRating._Cast_GBT17855SplineJointRating":
        return self._Cast_GBT17855SplineJointRating(self)
