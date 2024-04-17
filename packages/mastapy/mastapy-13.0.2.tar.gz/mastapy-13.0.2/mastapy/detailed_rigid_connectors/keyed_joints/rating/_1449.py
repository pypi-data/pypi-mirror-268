"""KeywayRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.detailed_rigid_connectors.interference_fits.rating import _1456
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KEYWAY_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints.Rating", "KeywayRating"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.keyed_joints import _1444
    from mastapy.detailed_rigid_connectors.keyed_joints.rating import _1448
    from mastapy.detailed_rigid_connectors.rating import _1443


__docformat__ = "restructuredtext en"
__all__ = ("KeywayRating",)


Self = TypeVar("Self", bound="KeywayRating")


class KeywayRating(_1456.InterferenceFitRating):
    """KeywayRating

    This is a mastapy class.
    """

    TYPE = _KEYWAY_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KeywayRating")

    class _Cast_KeywayRating:
        """Special nested class for casting KeywayRating to subclasses."""

        def __init__(self: "KeywayRating._Cast_KeywayRating", parent: "KeywayRating"):
            self._parent = parent

        @property
        def interference_fit_rating(
            self: "KeywayRating._Cast_KeywayRating",
        ) -> "_1456.InterferenceFitRating":
            return self._parent._cast(_1456.InterferenceFitRating)

        @property
        def shaft_hub_connection_rating(
            self: "KeywayRating._Cast_KeywayRating",
        ) -> "_1443.ShaftHubConnectionRating":
            from mastapy.detailed_rigid_connectors.rating import _1443

            return self._parent._cast(_1443.ShaftHubConnectionRating)

        @property
        def keyway_rating(self: "KeywayRating._Cast_KeywayRating") -> "KeywayRating":
            return self._parent

        def __getattr__(self: "KeywayRating._Cast_KeywayRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "KeywayRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def application_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ApplicationFactor

        if temp is None:
            return 0.0

        return temp

    @application_factor.setter
    @enforce_parameter_types
    def application_factor(self: Self, value: "float"):
        self.wrapped.ApplicationFactor = float(value) if value is not None else 0.0

    @property
    def circumferential_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CircumferentialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def extreme_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExtremeForce

        if temp is None:
            return 0.0

        return temp

    @property
    def extreme_load_carrying_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExtremeLoadCarryingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_engagement_factor_extreme_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalEngagementFactorExtremeLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_engagement_factor_rated_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalEngagementFactorRatedLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def frictional_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionalTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_component_extreme_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerComponentExtremeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_component_rated_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerComponentRatedSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def key_extreme_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KeyExtremeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def key_rated_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KeyRatedSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_single_key(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LoadDistributionFactorSingleKey

        if temp is None:
            return 0.0

        return temp

    @load_distribution_factor_single_key.setter
    @enforce_parameter_types
    def load_distribution_factor_single_key(self: Self, value: "float"):
        self.wrapped.LoadDistributionFactorSingleKey = (
            float(value) if value is not None else 0.0
        )

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
    def number_of_torque_peaks(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfTorquePeaks

        if temp is None:
            return 0.0

        return temp

    @number_of_torque_peaks.setter
    @enforce_parameter_types
    def number_of_torque_peaks(self: Self, value: "float"):
        self.wrapped.NumberOfTorquePeaks = float(value) if value is not None else 0.0

    @property
    def number_of_torque_reversals(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfTorqueReversals

        if temp is None:
            return 0.0

        return temp

    @number_of_torque_reversals.setter
    @enforce_parameter_types
    def number_of_torque_reversals(self: Self, value: "float"):
        self.wrapped.NumberOfTorqueReversals = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_component_extreme_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterComponentExtremeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_component_rated_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterComponentRatedSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def rated_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatedForce

        if temp is None:
            return 0.0

        return temp

    @property
    def rated_load_carrying_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatedLoadCarryingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_peak_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorquePeakFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_reversal_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueReversalFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def keyed_joint_design(self: Self) -> "_1444.KeyedJointDesign":
        """mastapy.detailed_rigid_connectors.keyed_joints.KeyedJointDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KeyedJointDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def keyway_half_ratings(self: Self) -> "List[_1448.KeywayHalfRating]":
        """List[mastapy.detailed_rigid_connectors.keyed_joints.rating.KeywayHalfRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KeywayHalfRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "KeywayRating._Cast_KeywayRating":
        return self._Cast_KeywayRating(self)
