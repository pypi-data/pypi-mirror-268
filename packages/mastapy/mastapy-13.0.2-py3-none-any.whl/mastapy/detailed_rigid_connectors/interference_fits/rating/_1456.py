"""InterferenceFitRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.detailed_rigid_connectors.rating import _1443
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_FIT_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits.Rating",
    "InterferenceFitRating",
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.keyed_joints.rating import _1449


__docformat__ = "restructuredtext en"
__all__ = ("InterferenceFitRating",)


Self = TypeVar("Self", bound="InterferenceFitRating")


class InterferenceFitRating(_1443.ShaftHubConnectionRating):
    """InterferenceFitRating

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_FIT_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterferenceFitRating")

    class _Cast_InterferenceFitRating:
        """Special nested class for casting InterferenceFitRating to subclasses."""

        def __init__(
            self: "InterferenceFitRating._Cast_InterferenceFitRating",
            parent: "InterferenceFitRating",
        ):
            self._parent = parent

        @property
        def shaft_hub_connection_rating(
            self: "InterferenceFitRating._Cast_InterferenceFitRating",
        ) -> "_1443.ShaftHubConnectionRating":
            return self._parent._cast(_1443.ShaftHubConnectionRating)

        @property
        def keyway_rating(
            self: "InterferenceFitRating._Cast_InterferenceFitRating",
        ) -> "_1449.KeywayRating":
            from mastapy.detailed_rigid_connectors.keyed_joints.rating import _1449

            return self._parent._cast(_1449.KeywayRating)

        @property
        def interference_fit_rating(
            self: "InterferenceFitRating._Cast_InterferenceFitRating",
        ) -> "InterferenceFitRating":
            return self._parent

        def __getattr__(
            self: "InterferenceFitRating._Cast_InterferenceFitRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InterferenceFitRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_axial_force_stationary(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableAxialForceStationary

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_axial_force_at_operating_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableAxialForceAtOperatingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_torque_stationary(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableTorqueStationary

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_torque_at_operating_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableTorqueAtOperatingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialForce

        if temp is None:
            return 0.0

        return temp

    @axial_force.setter
    @enforce_parameter_types
    def axial_force(self: Self, value: "float"):
        self.wrapped.AxialForce = float(value) if value is not None else 0.0

    @property
    def diameter_of_joint(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterOfJoint

        if temp is None:
            return 0.0

        return temp

    @property
    def joint_pressure_at_operating_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.JointPressureAtOperatingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_joint(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfJoint

        if temp is None:
            return 0.0

        return temp

    @property
    def moment(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Moment

        if temp is None:
            return 0.0

        return temp

    @moment.setter
    @enforce_parameter_types
    def moment(self: Self, value: "float"):
        self.wrapped.Moment = float(value) if value is not None else 0.0

    @property
    def peripheral_speed_of_outer_part(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeripheralSpeedOfOuterPart

        if temp is None:
            return 0.0

        return temp

    @property
    def peripheral_speed_of_outer_part_causing_loss_of_interference(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeripheralSpeedOfOuterPartCausingLossOfInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_axial_force_stationary(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleAxialForceStationary

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_axial_force_at_operating_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleAxialForceAtOperatingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_torque_stationary(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleTorqueStationary

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_torque_at_operating_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleTorqueAtOperatingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialForce

        if temp is None:
            return 0.0

        return temp

    @radial_force.setter
    @enforce_parameter_types
    def radial_force(self: Self, value: "float"):
        self.wrapped.RadialForce = float(value) if value is not None else 0.0

    @property
    def required_fit_for_avoidance_of_fretting_wear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RequiredFitForAvoidanceOfFrettingWear

        if temp is None:
            return 0.0

        return temp

    @property
    def rotational_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationalSpeed

        if temp is None:
            return 0.0

        return temp

    @rotational_speed.setter
    @enforce_parameter_types
    def rotational_speed(self: Self, value: "float"):
        self.wrapped.RotationalSpeed = float(value) if value is not None else 0.0

    @property
    def safety_factor_for_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_axial_force_stationary(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForAxialForceStationary

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_torque_stationary(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForTorqueStationary

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @torque.setter
    @enforce_parameter_types
    def torque(self: Self, value: "float"):
        self.wrapped.Torque = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "InterferenceFitRating._Cast_InterferenceFitRating":
        return self._Cast_InterferenceFitRating(self)
