"""VirtualCylindricalGearSetISO10300MethodB2"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _395
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_SET_ISO10300_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "VirtualCylindricalGearSetISO10300MethodB2",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _383, _386


__docformat__ = "restructuredtext en"
__all__ = ("VirtualCylindricalGearSetISO10300MethodB2",)


Self = TypeVar("Self", bound="VirtualCylindricalGearSetISO10300MethodB2")


class VirtualCylindricalGearSetISO10300MethodB2(
    _395.VirtualCylindricalGearSet["_394.VirtualCylindricalGearISO10300MethodB2"]
):
    """VirtualCylindricalGearSetISO10300MethodB2

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_SET_ISO10300_METHOD_B2
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualCylindricalGearSetISO10300MethodB2"
    )

    class _Cast_VirtualCylindricalGearSetISO10300MethodB2:
        """Special nested class for casting VirtualCylindricalGearSetISO10300MethodB2 to subclasses."""

        def __init__(
            self: "VirtualCylindricalGearSetISO10300MethodB2._Cast_VirtualCylindricalGearSetISO10300MethodB2",
            parent: "VirtualCylindricalGearSetISO10300MethodB2",
        ):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_set(
            self: "VirtualCylindricalGearSetISO10300MethodB2._Cast_VirtualCylindricalGearSetISO10300MethodB2",
        ) -> "_395.VirtualCylindricalGearSet":
            return self._parent._cast(_395.VirtualCylindricalGearSet)

        @property
        def bevel_virtual_cylindrical_gear_set_iso10300_method_b2(
            self: "VirtualCylindricalGearSetISO10300MethodB2._Cast_VirtualCylindricalGearSetISO10300MethodB2",
        ) -> "_383.BevelVirtualCylindricalGearSetISO10300MethodB2":
            from mastapy.gears.rating.virtual_cylindrical_gears import _383

            return self._parent._cast(
                _383.BevelVirtualCylindricalGearSetISO10300MethodB2
            )

        @property
        def hypoid_virtual_cylindrical_gear_set_iso10300_method_b2(
            self: "VirtualCylindricalGearSetISO10300MethodB2._Cast_VirtualCylindricalGearSetISO10300MethodB2",
        ) -> "_386.HypoidVirtualCylindricalGearSetISO10300MethodB2":
            from mastapy.gears.rating.virtual_cylindrical_gears import _386

            return self._parent._cast(
                _386.HypoidVirtualCylindricalGearSetISO10300MethodB2
            )

        @property
        def virtual_cylindrical_gear_set_iso10300_method_b2(
            self: "VirtualCylindricalGearSetISO10300MethodB2._Cast_VirtualCylindricalGearSetISO10300MethodB2",
        ) -> "VirtualCylindricalGearSetISO10300MethodB2":
            return self._parent

        def __getattr__(
            self: "VirtualCylindricalGearSetISO10300MethodB2._Cast_VirtualCylindricalGearSetISO10300MethodB2",
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
        self: Self, instance_to_wrap: "VirtualCylindricalGearSetISO10300MethodB2.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_contact_direction_and_tooth_tangent_in_pitch_plane(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleBetweenContactDirectionAndToothTangentInPitchPlane

        if temp is None:
            return 0.0

        return temp

    @property
    def angle_between_projection_of_pinion_axis_and_direction_of_contact_in_pitch_plane(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AngleBetweenProjectionOfPinionAxisAndDirectionOfContactInPitchPlane
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def angle_between_projection_of_wheel_axis_and_direction_of_contact_in_pitch_plane(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AngleBetweenProjectionOfWheelAxisAndDirectionOfContactInPitchPlane
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def angle_of_contact_line_relative_to_root_cone(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleOfContactLineRelativeToRootCone

        if temp is None:
            return 0.0

        return temp

    @property
    def angular_pitch_of_virtual_cylindrical_wheel(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularPitchOfVirtualCylindricalWheel

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_shift_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactShiftFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_base_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanBaseSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def modified_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModifiedContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_base_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeBaseFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_length_of_action_in_normal_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeLengthOfActionInNormalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_mean_normal_base_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMeanNormalBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualCylindricalGearSetISO10300MethodB2._Cast_VirtualCylindricalGearSetISO10300MethodB2":
        return self._Cast_VirtualCylindricalGearSetISO10300MethodB2(self)
