"""CylindricalMisalignmentCalculator"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal import conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MISALIGNMENT_CALCULATOR = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "CylindricalMisalignmentCalculator"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMisalignmentCalculator",)


Self = TypeVar("Self", bound="CylindricalMisalignmentCalculator")


class CylindricalMisalignmentCalculator(_0.APIBase):
    """CylindricalMisalignmentCalculator

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MISALIGNMENT_CALCULATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalMisalignmentCalculator")

    class _Cast_CylindricalMisalignmentCalculator:
        """Special nested class for casting CylindricalMisalignmentCalculator to subclasses."""

        def __init__(
            self: "CylindricalMisalignmentCalculator._Cast_CylindricalMisalignmentCalculator",
            parent: "CylindricalMisalignmentCalculator",
        ):
            self._parent = parent

        @property
        def cylindrical_misalignment_calculator(
            self: "CylindricalMisalignmentCalculator._Cast_CylindricalMisalignmentCalculator",
        ) -> "CylindricalMisalignmentCalculator":
            return self._parent

        def __getattr__(
            self: "CylindricalMisalignmentCalculator._Cast_CylindricalMisalignmentCalculator",
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
        self: Self, instance_to_wrap: "CylindricalMisalignmentCalculator.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_equivalent_misalignment_for_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAEquivalentMisalignmentForRating

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_line_fit_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearALineFitMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_line_fit_misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearALineFitMisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_radial_angular_component_of_rigid_body_misalignment(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearARadialAngularComponentOfRigidBodyMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_rigid_body_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearARigidBodyMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_rigid_body_misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearARigidBodyMisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_rigid_body_out_of_plane_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearARigidBodyOutOfPlaneMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_rigid_body_out_of_plane_misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearARigidBodyOutOfPlaneMisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_single_node_misalignment_angle_due_to_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearASingleNodeMisalignmentAngleDueToTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_single_node_misalignment_due_to_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearASingleNodeMisalignmentDueToTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_single_node_misalignment_due_to_twist(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearASingleNodeMisalignmentDueToTwist

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_tangential_angular_component_of_rigid_body_misalignment(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearATangentialAngularComponentOfRigidBodyMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_transverse_separations(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearATransverseSeparations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def gear_b_equivalent_misalignment_for_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBEquivalentMisalignmentForRating

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_line_fit_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBLineFitMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_line_fit_misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBLineFitMisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_radial_angular_component_of_rigid_body_misalignment(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBRadialAngularComponentOfRigidBodyMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_rigid_body_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBRigidBodyMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_rigid_body_misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBRigidBodyMisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_rigid_body_out_of_plane_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBRigidBodyOutOfPlaneMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_rigid_body_out_of_plane_misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBRigidBodyOutOfPlaneMisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_single_node_misalignment_angle_due_to_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBSingleNodeMisalignmentAngleDueToTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_single_node_misalignment_due_to_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBSingleNodeMisalignmentDueToTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_single_node_misalignment_due_to_twist(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBSingleNodeMisalignmentDueToTwist

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_tangential_angular_component_of_rigid_body_misalignment(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBTangentialAngularComponentOfRigidBodyMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_transverse_separations(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBTransverseSeparations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def total_equivalent_misalignment_for_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalEquivalentMisalignmentForRating

        if temp is None:
            return 0.0

        return temp

    @property
    def total_line_fit_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalLineFitMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def total_line_fit_misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalLineFitMisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def total_radial_angular_component_of_rigid_body_misalignment(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalRadialAngularComponentOfRigidBodyMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def total_rigid_body_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalRigidBodyMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def total_rigid_body_misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalRigidBodyMisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def total_rigid_body_out_of_plane_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalRigidBodyOutOfPlaneMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def total_rigid_body_out_of_plane_misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalRigidBodyOutOfPlaneMisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def total_single_node_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalSingleNodeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def total_single_node_misalignment_angle_due_to_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalSingleNodeMisalignmentAngleDueToTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def total_single_node_misalignment_due_to_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalSingleNodeMisalignmentDueToTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def total_single_node_misalignment_due_to_twist(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalSingleNodeMisalignmentDueToTwist

        if temp is None:
            return 0.0

        return temp

    @property
    def total_tangential_angular_component_of_rigid_body_misalignment(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalTangentialAngularComponentOfRigidBodyMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def rigid_body_coordinate_system_x_axis(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidBodyCoordinateSystemXAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def rigid_body_coordinate_system_y_axis(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidBodyCoordinateSystemYAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalMisalignmentCalculator._Cast_CylindricalMisalignmentCalculator":
        return self._Cast_CylindricalMisalignmentCalculator(self)
