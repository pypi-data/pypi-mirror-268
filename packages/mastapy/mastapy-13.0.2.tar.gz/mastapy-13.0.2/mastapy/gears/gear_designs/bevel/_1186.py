"""BevelGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.agma_gleason_conical import _1199
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Bevel", "BevelGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1192
    from mastapy.gears.gear_designs.zerol_bevel import _956
    from mastapy.gears.gear_designs.straight_bevel import _965
    from mastapy.gears.gear_designs.straight_bevel_diff import _969
    from mastapy.gears.gear_designs.spiral_bevel import _973
    from mastapy.gears.gear_designs.conical import _1160
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearDesign",)


Self = TypeVar("Self", bound="BevelGearDesign")


class BevelGearDesign(_1199.AGMAGleasonConicalGearDesign):
    """BevelGearDesign

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearDesign")

    class _Cast_BevelGearDesign:
        """Special nested class for casting BevelGearDesign to subclasses."""

        def __init__(
            self: "BevelGearDesign._Cast_BevelGearDesign", parent: "BevelGearDesign"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_design(
            self: "BevelGearDesign._Cast_BevelGearDesign",
        ) -> "_1199.AGMAGleasonConicalGearDesign":
            return self._parent._cast(_1199.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(
            self: "BevelGearDesign._Cast_BevelGearDesign",
        ) -> "_1160.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1160

            return self._parent._cast(_1160.ConicalGearDesign)

        @property
        def gear_design(
            self: "BevelGearDesign._Cast_BevelGearDesign",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "BevelGearDesign._Cast_BevelGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_gear_design(
            self: "BevelGearDesign._Cast_BevelGearDesign",
        ) -> "_956.ZerolBevelGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _956

            return self._parent._cast(_956.ZerolBevelGearDesign)

        @property
        def straight_bevel_gear_design(
            self: "BevelGearDesign._Cast_BevelGearDesign",
        ) -> "_965.StraightBevelGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _965

            return self._parent._cast(_965.StraightBevelGearDesign)

        @property
        def straight_bevel_diff_gear_design(
            self: "BevelGearDesign._Cast_BevelGearDesign",
        ) -> "_969.StraightBevelDiffGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _969

            return self._parent._cast(_969.StraightBevelDiffGearDesign)

        @property
        def spiral_bevel_gear_design(
            self: "BevelGearDesign._Cast_BevelGearDesign",
        ) -> "_973.SpiralBevelGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _973

            return self._parent._cast(_973.SpiralBevelGearDesign)

        @property
        def bevel_gear_design(
            self: "BevelGearDesign._Cast_BevelGearDesign",
        ) -> "BevelGearDesign":
            return self._parent

        def __getattr__(self: "BevelGearDesign._Cast_BevelGearDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @property
    def addendum_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AddendumAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def crown_to_cross_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrownToCrossPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Dedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DedendumAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def difference_from_ideal_pitch_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DifferenceFromIdealPitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def face_apex_to_cross_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceApexToCrossPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_as_percent_of_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidthAsPercentOfConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def finishing_method(self: Self) -> "_1192.FinishingMethods":
        """mastapy.gears.gear_designs.bevel.FinishingMethods"""
        temp = self.wrapped.FinishingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Bevel.FinishingMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.bevel._1192", "FinishingMethods"
        )(value)

    @finishing_method.setter
    @enforce_parameter_types
    def finishing_method(self: Self, value: "_1192.FinishingMethods"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Bevel.FinishingMethods"
        )
        self.wrapped.FinishingMethod = value

    @property
    def front_crown_to_cross_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrontCrownToCrossPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_slot_width_at_minimum_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSlotWidthAtMinimumBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_addendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanAddendum

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_chordal_addendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanChordalAddendum

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_dedendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanDedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_normal_circular_thickness_for_zero_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanNormalCircularThicknessForZeroBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_normal_circular_thickness_with_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanNormalCircularThicknessWithBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_slot_width_at_minimum_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanSlotWidthAtMinimumBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_transverse_circular_thickness_for_zero_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTransverseCircularThicknessForZeroBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_transverse_circular_thickness_with_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTransverseCircularThicknessWithBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_slot_width_at_minimum_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterSlotWidthAtMinimumBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_transverse_circular_thickness_for_zero_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterTransverseCircularThicknessForZeroBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_transverse_circular_thickness_with_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterTransverseCircularThicknessWithBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PitchAngle

        if temp is None:
            return 0.0

        return temp

    @pitch_angle.setter
    @enforce_parameter_types
    def pitch_angle(self: Self, value: "float"):
        self.wrapped.PitchAngle = float(value) if value is not None else 0.0

    @property
    def pitch_apex_to_boot(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchApexToBoot

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_apex_to_cross_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchApexToCrossPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_apex_to_crown(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchApexToCrown

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_apex_to_front_boot(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchApexToFrontBoot

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_apex_to_front_crown(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchApexToFrontCrown

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_diameter_at_wheel_outer_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchDiameterAtWheelOuterSection

        if temp is None:
            return 0.0

        return temp

    @property
    def root_apex_to_cross_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootApexToCrossPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def stock_allowance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StockAllowance

        if temp is None:
            return 0.0

        return temp

    @stock_allowance.setter
    @enforce_parameter_types
    def stock_allowance(self: Self, value: "float"):
        self.wrapped.StockAllowance = float(value) if value is not None else 0.0

    @property
    def surface_finish(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SurfaceFinish

        if temp is None:
            return 0.0

        return temp

    @surface_finish.setter
    @enforce_parameter_types
    def surface_finish(self: Self, value: "float"):
        self.wrapped.SurfaceFinish = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "BevelGearDesign._Cast_BevelGearDesign":
        return self._Cast_BevelGearDesign(self)
