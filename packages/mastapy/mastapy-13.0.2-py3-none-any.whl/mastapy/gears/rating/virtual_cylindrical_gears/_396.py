"""VirtualCylindricalGearSetISO10300MethodB1"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _395
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_SET_ISO10300_METHOD_B1 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "VirtualCylindricalGearSetISO10300MethodB1",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _382, _385


__docformat__ = "restructuredtext en"
__all__ = ("VirtualCylindricalGearSetISO10300MethodB1",)


Self = TypeVar("Self", bound="VirtualCylindricalGearSetISO10300MethodB1")


class VirtualCylindricalGearSetISO10300MethodB1(
    _395.VirtualCylindricalGearSet["_393.VirtualCylindricalGearISO10300MethodB1"]
):
    """VirtualCylindricalGearSetISO10300MethodB1

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_SET_ISO10300_METHOD_B1
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualCylindricalGearSetISO10300MethodB1"
    )

    class _Cast_VirtualCylindricalGearSetISO10300MethodB1:
        """Special nested class for casting VirtualCylindricalGearSetISO10300MethodB1 to subclasses."""

        def __init__(
            self: "VirtualCylindricalGearSetISO10300MethodB1._Cast_VirtualCylindricalGearSetISO10300MethodB1",
            parent: "VirtualCylindricalGearSetISO10300MethodB1",
        ):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_set(
            self: "VirtualCylindricalGearSetISO10300MethodB1._Cast_VirtualCylindricalGearSetISO10300MethodB1",
        ) -> "_395.VirtualCylindricalGearSet":
            return self._parent._cast(_395.VirtualCylindricalGearSet)

        @property
        def bevel_virtual_cylindrical_gear_set_iso10300_method_b1(
            self: "VirtualCylindricalGearSetISO10300MethodB1._Cast_VirtualCylindricalGearSetISO10300MethodB1",
        ) -> "_382.BevelVirtualCylindricalGearSetISO10300MethodB1":
            from mastapy.gears.rating.virtual_cylindrical_gears import _382

            return self._parent._cast(
                _382.BevelVirtualCylindricalGearSetISO10300MethodB1
            )

        @property
        def hypoid_virtual_cylindrical_gear_set_iso10300_method_b1(
            self: "VirtualCylindricalGearSetISO10300MethodB1._Cast_VirtualCylindricalGearSetISO10300MethodB1",
        ) -> "_385.HypoidVirtualCylindricalGearSetISO10300MethodB1":
            from mastapy.gears.rating.virtual_cylindrical_gears import _385

            return self._parent._cast(
                _385.HypoidVirtualCylindricalGearSetISO10300MethodB1
            )

        @property
        def virtual_cylindrical_gear_set_iso10300_method_b1(
            self: "VirtualCylindricalGearSetISO10300MethodB1._Cast_VirtualCylindricalGearSetISO10300MethodB1",
        ) -> "VirtualCylindricalGearSetISO10300MethodB1":
            return self._parent

        def __getattr__(
            self: "VirtualCylindricalGearSetISO10300MethodB1._Cast_VirtualCylindricalGearSetISO10300MethodB1",
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
        self: Self, instance_to_wrap: "VirtualCylindricalGearSetISO10300MethodB1.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def auxiliary_angle_for_virtual_face_width_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryAngleForVirtualFaceWidthMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def correction_factor_for_theoretical_length_of_middle_contact_line_for_surface_durability(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.CorrectionFactorForTheoreticalLengthOfMiddleContactLineForSurfaceDurability
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_of_the_middle_contact_line_in_the_zone_of_action_for_surface_durability(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DistanceOfTheMiddleContactLineInTheZoneOfActionForSurfaceDurability
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_of_the_middle_contact_line_in_the_zone_of_action_for_tooth_root_strength(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DistanceOfTheMiddleContactLineInTheZoneOfActionForToothRootStrength
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_of_the_root_contact_line_in_the_zone_of_action_for_surface_durability(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DistanceOfTheRootContactLineInTheZoneOfActionForSurfaceDurability
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_of_the_root_contact_line_in_the_zone_of_action_for_tooth_root_strength(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DistanceOfTheRootContactLineInTheZoneOfActionForToothRootStrength
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_of_the_tip_contact_line_in_the_zone_of_action_for_surface_durability(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DistanceOfTheTipContactLineInTheZoneOfActionForSurfaceDurability
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_of_the_tip_contact_line_in_the_zone_of_action_for_tooth_root_strength(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DistanceOfTheTipContactLineInTheZoneOfActionForToothRootStrength
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def inclination_angle_of_contact_line(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InclinationAngleOfContactLine

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_middle_contact_line_for_surface_durability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfMiddleContactLineForSurfaceDurability

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_middle_contact_line_for_tooth_root_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfMiddleContactLineForToothRootStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_path_of_contact_of_virtual_cylindrical_gear_in_transverse_section(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LengthOfPathOfContactOfVirtualCylindricalGearInTransverseSection
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_root_contact_line_for_surface_durability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfRootContactLineForSurfaceDurability

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_root_contact_line_for_tooth_root_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfRootContactLineForToothRootStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_tip_contact_line_for_surface_durability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfTipContactLineForSurfaceDurability

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_tip_contact_line_for_tooth_root_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfTipContactLineForToothRootStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_distance_from_middle_contact_line(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumDistanceFromMiddleContactLine

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_distance_from_middle_contact_line_at_left_side_of_contact_pattern(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MaximumDistanceFromMiddleContactLineAtLeftSideOfContactPattern
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_distance_from_middle_contact_line_at_right_side_of_contact_pattern(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MaximumDistanceFromMiddleContactLineAtRightSideOfContactPattern
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def projected_auxiliary_angle_for_length_of_contact_line(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProjectedAuxiliaryAngleForLengthOfContactLine

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_of_relative_curvature_in_normal_section_at_the_mean_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusOfRelativeCurvatureInNormalSectionAtTheMeanPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_of_relative_curvature_vertical_to_the_contact_line(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusOfRelativeCurvatureVerticalToTheContactLine

        if temp is None:
            return 0.0

        return temp

    @property
    def tan_auxiliary_angle_for_length_of_contact_line_calculation(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TanAuxiliaryAngleForLengthOfContactLineCalculation

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_effective_face_width_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelEffectiveFaceWidthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualCylindricalGearSetISO10300MethodB1._Cast_VirtualCylindricalGearSetISO10300MethodB1":
        return self._Cast_VirtualCylindricalGearSetISO10300MethodB1(self)
