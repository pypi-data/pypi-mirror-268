"""VirtualCylindricalGearISO10300MethodB2"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.virtual_cylindrical_gears import _392
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears",
    "VirtualCylindricalGearISO10300MethodB2",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _381, _384


__docformat__ = "restructuredtext en"
__all__ = ("VirtualCylindricalGearISO10300MethodB2",)


Self = TypeVar("Self", bound="VirtualCylindricalGearISO10300MethodB2")


class VirtualCylindricalGearISO10300MethodB2(_392.VirtualCylindricalGearBasic):
    """VirtualCylindricalGearISO10300MethodB2

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B2
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualCylindricalGearISO10300MethodB2"
    )

    class _Cast_VirtualCylindricalGearISO10300MethodB2:
        """Special nested class for casting VirtualCylindricalGearISO10300MethodB2 to subclasses."""

        def __init__(
            self: "VirtualCylindricalGearISO10300MethodB2._Cast_VirtualCylindricalGearISO10300MethodB2",
            parent: "VirtualCylindricalGearISO10300MethodB2",
        ):
            self._parent = parent

        @property
        def virtual_cylindrical_gear_basic(
            self: "VirtualCylindricalGearISO10300MethodB2._Cast_VirtualCylindricalGearISO10300MethodB2",
        ) -> "_392.VirtualCylindricalGearBasic":
            return self._parent._cast(_392.VirtualCylindricalGearBasic)

        @property
        def bevel_virtual_cylindrical_gear_iso10300_method_b2(
            self: "VirtualCylindricalGearISO10300MethodB2._Cast_VirtualCylindricalGearISO10300MethodB2",
        ) -> "_381.BevelVirtualCylindricalGearISO10300MethodB2":
            from mastapy.gears.rating.virtual_cylindrical_gears import _381

            return self._parent._cast(_381.BevelVirtualCylindricalGearISO10300MethodB2)

        @property
        def hypoid_virtual_cylindrical_gear_iso10300_method_b2(
            self: "VirtualCylindricalGearISO10300MethodB2._Cast_VirtualCylindricalGearISO10300MethodB2",
        ) -> "_384.HypoidVirtualCylindricalGearISO10300MethodB2":
            from mastapy.gears.rating.virtual_cylindrical_gears import _384

            return self._parent._cast(_384.HypoidVirtualCylindricalGearISO10300MethodB2)

        @property
        def virtual_cylindrical_gear_iso10300_method_b2(
            self: "VirtualCylindricalGearISO10300MethodB2._Cast_VirtualCylindricalGearISO10300MethodB2",
        ) -> "VirtualCylindricalGearISO10300MethodB2":
            return self._parent

        def __getattr__(
            self: "VirtualCylindricalGearISO10300MethodB2._Cast_VirtualCylindricalGearISO10300MethodB2",
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
        self: Self, instance_to_wrap: "VirtualCylindricalGearISO10300MethodB2.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjusted_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_edge_radius_of_tool(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeEdgeRadiusOfTool

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_length_of_action_from_tip_to_pitch_circle_in_normal_section(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeLengthOfActionFromTipToPitchCircleInNormalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_mean_back_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMeanBackConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_mean_base_radius_of_virtual_cylindrical_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMeanBaseRadiusOfVirtualCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_mean_normal_pitch_for_virtual_cylindrical_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMeanNormalPitchForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_mean_virtual_dedendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMeanVirtualDedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_mean_virtual_pitch_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMeanVirtualPitchRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_mean_virtual_tip_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMeanVirtualTipRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_virtual_tooth_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeVirtualToothThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualCylindricalGearISO10300MethodB2._Cast_VirtualCylindricalGearISO10300MethodB2":
        return self._Cast_VirtualCylindricalGearISO10300MethodB2(self)
