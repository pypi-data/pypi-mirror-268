"""BevelGearSetDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.bevel import _1196
from mastapy.gears.gear_designs.agma_gleason_conical import _1201
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Bevel", "BevelGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1157, _1162
    from mastapy.math_utility import _1526
    from mastapy.gears.gear_designs.bevel import _1197, _1195
    from mastapy.gears import _350
    from mastapy.gears.gear_designs.zerol_bevel import _958
    from mastapy.gears.gear_designs.straight_bevel import _967
    from mastapy.gears.gear_designs.straight_bevel_diff import _971
    from mastapy.gears.gear_designs.spiral_bevel import _975
    from mastapy.gears.gear_designs import _954, _952


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetDesign",)


Self = TypeVar("Self", bound="BevelGearSetDesign")


class BevelGearSetDesign(_1201.AGMAGleasonConicalGearSetDesign):
    """BevelGearSetDesign

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetDesign")

    class _Cast_BevelGearSetDesign:
        """Special nested class for casting BevelGearSetDesign to subclasses."""

        def __init__(
            self: "BevelGearSetDesign._Cast_BevelGearSetDesign",
            parent: "BevelGearSetDesign",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_design(
            self: "BevelGearSetDesign._Cast_BevelGearSetDesign",
        ) -> "_1201.AGMAGleasonConicalGearSetDesign":
            return self._parent._cast(_1201.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(
            self: "BevelGearSetDesign._Cast_BevelGearSetDesign",
        ) -> "_1162.ConicalGearSetDesign":
            from mastapy.gears.gear_designs.conical import _1162

            return self._parent._cast(_1162.ConicalGearSetDesign)

        @property
        def gear_set_design(
            self: "BevelGearSetDesign._Cast_BevelGearSetDesign",
        ) -> "_954.GearSetDesign":
            from mastapy.gears.gear_designs import _954

            return self._parent._cast(_954.GearSetDesign)

        @property
        def gear_design_component(
            self: "BevelGearSetDesign._Cast_BevelGearSetDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_gear_set_design(
            self: "BevelGearSetDesign._Cast_BevelGearSetDesign",
        ) -> "_958.ZerolBevelGearSetDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _958

            return self._parent._cast(_958.ZerolBevelGearSetDesign)

        @property
        def straight_bevel_gear_set_design(
            self: "BevelGearSetDesign._Cast_BevelGearSetDesign",
        ) -> "_967.StraightBevelGearSetDesign":
            from mastapy.gears.gear_designs.straight_bevel import _967

            return self._parent._cast(_967.StraightBevelGearSetDesign)

        @property
        def straight_bevel_diff_gear_set_design(
            self: "BevelGearSetDesign._Cast_BevelGearSetDesign",
        ) -> "_971.StraightBevelDiffGearSetDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _971

            return self._parent._cast(_971.StraightBevelDiffGearSetDesign)

        @property
        def spiral_bevel_gear_set_design(
            self: "BevelGearSetDesign._Cast_BevelGearSetDesign",
        ) -> "_975.SpiralBevelGearSetDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _975

            return self._parent._cast(_975.SpiralBevelGearSetDesign)

        @property
        def bevel_gear_set_design(
            self: "BevelGearSetDesign._Cast_BevelGearSetDesign",
        ) -> "BevelGearSetDesign":
            return self._parent

        def __getattr__(self: "BevelGearSetDesign._Cast_BevelGearSetDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_scoring_index(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AllowableScoringIndex

        if temp is None:
            return 0.0

        return temp

    @allowable_scoring_index.setter
    @enforce_parameter_types
    def allowable_scoring_index(self: Self, value: "float"):
        self.wrapped.AllowableScoringIndex = float(value) if value is not None else 0.0

    @property
    def backlash_distribution_rule(self: Self) -> "_1157.BacklashDistributionRule":
        """mastapy.gears.gear_designs.conical.BacklashDistributionRule"""
        temp = self.wrapped.BacklashDistributionRule

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.BacklashDistributionRule"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1157", "BacklashDistributionRule"
        )(value)

    @backlash_distribution_rule.setter
    @enforce_parameter_types
    def backlash_distribution_rule(self: Self, value: "_1157.BacklashDistributionRule"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.BacklashDistributionRule"
        )
        self.wrapped.BacklashDistributionRule = value

    @property
    def backlash_used_for_tooth_thickness_calculation(self: Self) -> "_1526.MaxMinMean":
        """mastapy.math_utility.MaxMinMean"""
        temp = self.wrapped.BacklashUsedForToothThicknessCalculation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.MathUtility.MaxMinMean")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.math_utility._1526", "MaxMinMean")(
            value
        )

    @backlash_used_for_tooth_thickness_calculation.setter
    @enforce_parameter_types
    def backlash_used_for_tooth_thickness_calculation(
        self: Self, value: "_1526.MaxMinMean"
    ):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.MathUtility.MaxMinMean")
        self.wrapped.BacklashUsedForToothThicknessCalculation = value

    @property
    def basic_crown_gear_addendum_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicCrownGearAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_crown_gear_dedendum_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicCrownGearDedendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def circular_thickness_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CircularThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @circular_thickness_factor.setter
    @enforce_parameter_types
    def circular_thickness_factor(self: Self, value: "float"):
        self.wrapped.CircularThicknessFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Clearance

        if temp is None:
            return 0.0

        return temp

    @property
    def diametral_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiametralPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def factor_of_safety_for_scoring(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FactorOfSafetyForScoring

        if temp is None:
            return 0.0

        return temp

    @factor_of_safety_for_scoring.setter
    @enforce_parameter_types
    def factor_of_safety_for_scoring(self: Self, value: "float"):
        self.wrapped.FactorOfSafetyForScoring = (
            float(value) if value is not None else 0.0
        )

    @property
    def ideal_circular_thickness_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.IdealCircularThicknessFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @ideal_circular_thickness_factor.setter
    @enforce_parameter_types
    def ideal_circular_thickness_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.IdealCircularThicknessFactor = value

    @property
    def ideal_pinion_mean_transverse_circular_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.IdealPinionMeanTransverseCircularThickness

        if temp is None:
            return 0.0

        return temp

    @ideal_pinion_mean_transverse_circular_thickness.setter
    @enforce_parameter_types
    def ideal_pinion_mean_transverse_circular_thickness(self: Self, value: "float"):
        self.wrapped.IdealPinionMeanTransverseCircularThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def ideal_pinion_outer_transverse_circular_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.IdealPinionOuterTransverseCircularThickness

        if temp is None:
            return 0.0

        return temp

    @ideal_pinion_outer_transverse_circular_thickness.setter
    @enforce_parameter_types
    def ideal_pinion_outer_transverse_circular_thickness(self: Self, value: "float"):
        self.wrapped.IdealPinionOuterTransverseCircularThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def ideal_wheel_finish_cutter_point_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.IdealWheelFinishCutterPointWidth

        if temp is None:
            return 0.0

        return temp

    @ideal_wheel_finish_cutter_point_width.setter
    @enforce_parameter_types
    def ideal_wheel_finish_cutter_point_width(self: Self, value: "float"):
        self.wrapped.IdealWheelFinishCutterPointWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def ideal_wheel_mean_slot_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.IdealWheelMeanSlotWidth

        if temp is None:
            return 0.0

        return temp

    @ideal_wheel_mean_slot_width.setter
    @enforce_parameter_types
    def ideal_wheel_mean_slot_width(self: Self, value: "float"):
        self.wrapped.IdealWheelMeanSlotWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def mean_addendum_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @mean_addendum_factor.setter
    @enforce_parameter_types
    def mean_addendum_factor(self: Self, value: "float"):
        self.wrapped.MeanAddendumFactor = float(value) if value is not None else 0.0

    @property
    def mean_circular_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanCircularPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_clearance_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanClearanceFactor

        if temp is None:
            return 0.0

        return temp

    @mean_clearance_factor.setter
    @enforce_parameter_types
    def mean_clearance_factor(self: Self, value: "float"):
        self.wrapped.MeanClearanceFactor = float(value) if value is not None else 0.0

    @property
    def mean_depth_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanDepthFactor

        if temp is None:
            return 0.0

        return temp

    @mean_depth_factor.setter
    @enforce_parameter_types
    def mean_depth_factor(self: Self, value: "float"):
        self.wrapped.MeanDepthFactor = float(value) if value is not None else 0.0

    @property
    def mean_diametral_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanDiametralPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_whole_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanWholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_working_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanWorkingDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_number_of_teeth_for_recommended_tooth_proportions(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumNumberOfTeethForRecommendedToothProportions

        if temp is None:
            return 0

        return temp

    @property
    def outer_wheel_addendum(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterWheelAddendum

        if temp is None:
            return 0.0

        return temp

    @outer_wheel_addendum.setter
    @enforce_parameter_types
    def outer_wheel_addendum(self: Self, value: "float"):
        self.wrapped.OuterWheelAddendum = float(value) if value is not None else 0.0

    @property
    def outer_whole_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterWholeDepth

        if temp is None:
            return 0.0

        return temp

    @outer_whole_depth.setter
    @enforce_parameter_types
    def outer_whole_depth(self: Self, value: "float"):
        self.wrapped.OuterWholeDepth = float(value) if value is not None else 0.0

    @property
    def outer_working_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterWorkingDepth

        if temp is None:
            return 0.0

        return temp

    @outer_working_depth.setter
    @enforce_parameter_types
    def outer_working_depth(self: Self, value: "float"):
        self.wrapped.OuterWorkingDepth = float(value) if value is not None else 0.0

    @property
    def pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureAngle

        if temp is None:
            return 0.0

        return temp

    @pressure_angle.setter
    @enforce_parameter_types
    def pressure_angle(self: Self, value: "float"):
        self.wrapped.PressureAngle = float(value) if value is not None else 0.0

    @property
    def profile_shift_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def round_cutter_specifications(
        self: Self,
    ) -> "_1197.WheelFinishCutterPointWidthRestrictionMethod":
        """mastapy.gears.gear_designs.bevel.WheelFinishCutterPointWidthRestrictionMethod"""
        temp = self.wrapped.RoundCutterSpecifications

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.WheelFinishCutterPointWidthRestrictionMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.bevel._1197",
            "WheelFinishCutterPointWidthRestrictionMethod",
        )(value)

    @round_cutter_specifications.setter
    @enforce_parameter_types
    def round_cutter_specifications(
        self: Self, value: "_1197.WheelFinishCutterPointWidthRestrictionMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Bevel.WheelFinishCutterPointWidthRestrictionMethod",
        )
        self.wrapped.RoundCutterSpecifications = value

    @property
    def specified_pinion_dedendum_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedPinionDedendumAngle

        if temp is None:
            return 0.0

        return temp

    @specified_pinion_dedendum_angle.setter
    @enforce_parameter_types
    def specified_pinion_dedendum_angle(self: Self, value: "float"):
        self.wrapped.SpecifiedPinionDedendumAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def specified_wheel_dedendum_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedWheelDedendumAngle

        if temp is None:
            return 0.0

        return temp

    @specified_wheel_dedendum_angle.setter
    @enforce_parameter_types
    def specified_wheel_dedendum_angle(self: Self, value: "float"):
        self.wrapped.SpecifiedWheelDedendumAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def strength_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StrengthFactor

        if temp is None:
            return 0.0

        return temp

    @strength_factor.setter
    @enforce_parameter_types
    def strength_factor(self: Self, value: "float"):
        self.wrapped.StrengthFactor = float(value) if value is not None else 0.0

    @property
    def thickness_modification_coefficient_theoretical(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThicknessModificationCoefficientTheoretical

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_proportions_input_method(
        self: Self,
    ) -> "_1195.ToothProportionsInputMethod":
        """mastapy.gears.gear_designs.bevel.ToothProportionsInputMethod"""
        temp = self.wrapped.ToothProportionsInputMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Bevel.ToothProportionsInputMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.bevel._1195", "ToothProportionsInputMethod"
        )(value)

    @tooth_proportions_input_method.setter
    @enforce_parameter_types
    def tooth_proportions_input_method(
        self: Self, value: "_1195.ToothProportionsInputMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Bevel.ToothProportionsInputMethod"
        )
        self.wrapped.ToothProportionsInputMethod = value

    @property
    def tooth_taper_root_line_tilt_method(self: Self) -> "_350.SpiralBevelRootLineTilt":
        """mastapy.gears.SpiralBevelRootLineTilt"""
        temp = self.wrapped.ToothTaperRootLineTiltMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.SpiralBevelRootLineTilt"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._350", "SpiralBevelRootLineTilt"
        )(value)

    @tooth_taper_root_line_tilt_method.setter
    @enforce_parameter_types
    def tooth_taper_root_line_tilt_method(
        self: Self, value: "_350.SpiralBevelRootLineTilt"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.SpiralBevelRootLineTilt"
        )
        self.wrapped.ToothTaperRootLineTiltMethod = value

    @property
    def tooth_thickness_specification_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ToothThicknessSpecificationMethod":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.bevel.ToothThicknessSpecificationMethod]"""
        temp = self.wrapped.ToothThicknessSpecificationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ToothThicknessSpecificationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @tooth_thickness_specification_method.setter
    @enforce_parameter_types
    def tooth_thickness_specification_method(
        self: Self, value: "_1196.ToothThicknessSpecificationMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ToothThicknessSpecificationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ToothThicknessSpecificationMethod = value

    @property
    def use_recommended_tooth_proportions(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseRecommendedToothProportions

        if temp is None:
            return False

        return temp

    @use_recommended_tooth_proportions.setter
    @enforce_parameter_types
    def use_recommended_tooth_proportions(self: Self, value: "bool"):
        self.wrapped.UseRecommendedToothProportions = (
            bool(value) if value is not None else False
        )

    @property
    def wheel_addendum_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_addendum_multiplier(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelAddendumMultiplier

        if temp is None:
            return 0.0

        return temp

    @wheel_addendum_multiplier.setter
    @enforce_parameter_types
    def wheel_addendum_multiplier(self: Self, value: "float"):
        self.wrapped.WheelAddendumMultiplier = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_finish_cutter_point_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelFinishCutterPointWidth

        if temp is None:
            return 0.0

        return temp

    @wheel_finish_cutter_point_width.setter
    @enforce_parameter_types
    def wheel_finish_cutter_point_width(self: Self, value: "float"):
        self.wrapped.WheelFinishCutterPointWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_inner_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInnerSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def whole_depth_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WholeDepthFactor

        if temp is None:
            return 0.0

        return temp

    @whole_depth_factor.setter
    @enforce_parameter_types
    def whole_depth_factor(self: Self, value: "float"):
        self.wrapped.WholeDepthFactor = float(value) if value is not None else 0.0

    @property
    def working_depth_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WorkingDepthFactor

        if temp is None:
            return 0.0

        return temp

    @working_depth_factor.setter
    @enforce_parameter_types
    def working_depth_factor(self: Self, value: "float"):
        self.wrapped.WorkingDepthFactor = float(value) if value is not None else 0.0

    @property
    def mean_spiral_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @mean_spiral_angle.setter
    @enforce_parameter_types
    def mean_spiral_angle(self: Self, value: "float"):
        self.wrapped.MeanSpiralAngle = float(value) if value is not None else 0.0

    @property
    def transverse_circular_thickness_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TransverseCircularThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @transverse_circular_thickness_factor.setter
    @enforce_parameter_types
    def transverse_circular_thickness_factor(self: Self, value: "float"):
        self.wrapped.TransverseCircularThicknessFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "BevelGearSetDesign._Cast_BevelGearSetDesign":
        return self._Cast_BevelGearSetDesign(self)
