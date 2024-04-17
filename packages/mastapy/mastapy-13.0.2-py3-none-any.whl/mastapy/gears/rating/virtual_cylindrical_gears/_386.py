"""HypoidVirtualCylindricalGearSetISO10300MethodB2"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _397
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_VIRTUAL_CYLINDRICAL_GEAR_SET_ISO10300_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "HypoidVirtualCylindricalGearSetISO10300MethodB2",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _395


__docformat__ = "restructuredtext en"
__all__ = ("HypoidVirtualCylindricalGearSetISO10300MethodB2",)


Self = TypeVar("Self", bound="HypoidVirtualCylindricalGearSetISO10300MethodB2")


class HypoidVirtualCylindricalGearSetISO10300MethodB2(
    _397.VirtualCylindricalGearSetISO10300MethodB2
):
    """HypoidVirtualCylindricalGearSetISO10300MethodB2

    This is a mastapy class.
    """

    TYPE = _HYPOID_VIRTUAL_CYLINDRICAL_GEAR_SET_ISO10300_METHOD_B2
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidVirtualCylindricalGearSetISO10300MethodB2"
    )

    class _Cast_HypoidVirtualCylindricalGearSetISO10300MethodB2:
        """Special nested class for casting HypoidVirtualCylindricalGearSetISO10300MethodB2 to subclasses."""

        def __init__(
            self: "HypoidVirtualCylindricalGearSetISO10300MethodB2._Cast_HypoidVirtualCylindricalGearSetISO10300MethodB2",
            parent: "HypoidVirtualCylindricalGearSetISO10300MethodB2",
        ):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_set_iso10300_method_b2(
            self: "HypoidVirtualCylindricalGearSetISO10300MethodB2._Cast_HypoidVirtualCylindricalGearSetISO10300MethodB2",
        ) -> "_397.VirtualCylindricalGearSetISO10300MethodB2":
            return self._parent._cast(_397.VirtualCylindricalGearSetISO10300MethodB2)

        @property
        def virtual_cylindrical_gear_set(
            self: "HypoidVirtualCylindricalGearSetISO10300MethodB2._Cast_HypoidVirtualCylindricalGearSetISO10300MethodB2",
        ) -> "_395.VirtualCylindricalGearSet":
            pass

            from mastapy.gears.rating.virtual_cylindrical_gears import _395

            return self._parent._cast(_395.VirtualCylindricalGearSet)

        @property
        def hypoid_virtual_cylindrical_gear_set_iso10300_method_b2(
            self: "HypoidVirtualCylindricalGearSetISO10300MethodB2._Cast_HypoidVirtualCylindricalGearSetISO10300MethodB2",
        ) -> "HypoidVirtualCylindricalGearSetISO10300MethodB2":
            return self._parent

        def __getattr__(
            self: "HypoidVirtualCylindricalGearSetISO10300MethodB2._Cast_HypoidVirtualCylindricalGearSetISO10300MethodB2",
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
        self: Self,
        instance_to_wrap: "HypoidVirtualCylindricalGearSetISO10300MethodB2.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_direction_of_contact_and_the_pitch_tangent(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleBetweenDirectionOfContactAndThePitchTangent

        if temp is None:
            return 0.0

        return temp

    @property
    def average_pressure_angle_unbalance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AveragePressureAngleUnbalance

        if temp is None:
            return 0.0

        return temp

    @property
    def coast_flank_pressure_angel_in_wheel_root_coordinates(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoastFlankPressureAngelInWheelRootCoordinates

        if temp is None:
            return 0.0

        return temp

    @property
    def drive_flank_pressure_angel_in_wheel_root_coordinates(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DriveFlankPressureAngelInWheelRootCoordinates

        if temp is None:
            return 0.0

        return temp

    @property
    def initial_value_for_the_wheel_angle_from_centreline_to_fillet_point_on_drive_flank(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.InitialValueForTheWheelAngleFromCentrelineToFilletPointOnDriveFlank
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_action_from_pinion_tip_to_pitch_circle_in_normal_section(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfActionFromPinionTipToPitchCircleInNormalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_action_from_wheel_tip_to_pitch_circle_in_normal_section(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfActionFromWheelTipToPitchCircleInNormalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def limit_pressure_angle_in_wheel_root_coordinates(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitPressureAngleInWheelRootCoordinates

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_contact_ratio_for_hypoid_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedContactRatioForHypoidGears

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_distance_from_blade_edge_to_centreline(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeDistanceFromBladeEdgeToCentreline

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_from_centreline_to_fillet_point_on_drive_flank(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAngleFromCentrelineToFilletPointOnDriveFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_from_centreline_to_pinion_tip_on_drive_side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAngleFromCentrelineToPinionTipOnDriveSide

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angle_from_centreline_to_tooth_surface_at_pitch_point_on_drive_side(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.WheelAngleFromCentrelineToToothSurfaceAtPitchPointOnDriveSide
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_mean_slot_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelMeanSlotWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def h(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.H

        if temp is None:
            return 0.0

        return temp

    @property
    def h1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.H1

        if temp is None:
            return 0.0

        return temp

    @property
    def h1o(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.H1o

        if temp is None:
            return 0.0

        return temp

    @property
    def h2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.H2

        if temp is None:
            return 0.0

        return temp

    @property
    def h2o(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.H2o

        if temp is None:
            return 0.0

        return temp

    @property
    def deltar(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Deltar

        if temp is None:
            return 0.0

        return temp

    @property
    def deltar_1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Deltar1

        if temp is None:
            return 0.0

        return temp

    @property
    def deltar_2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Deltar2

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidVirtualCylindricalGearSetISO10300MethodB2._Cast_HypoidVirtualCylindricalGearSetISO10300MethodB2":
        return self._Cast_HypoidVirtualCylindricalGearSetISO10300MethodB2(self)
