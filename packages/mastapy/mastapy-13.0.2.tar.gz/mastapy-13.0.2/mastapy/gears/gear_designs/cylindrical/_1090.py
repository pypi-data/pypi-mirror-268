"""ToothFlankFractureAnalysisSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.gear_designs.cylindrical import _1074
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ToothFlankFractureAnalysisSettings"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542
    from mastapy.gears.gear_designs.cylindrical import _1068


__docformat__ = "restructuredtext en"
__all__ = ("ToothFlankFractureAnalysisSettings",)


Self = TypeVar("Self", bound="ToothFlankFractureAnalysisSettings")


class ToothFlankFractureAnalysisSettings(
    _1593.IndependentReportablePropertiesBase["ToothFlankFractureAnalysisSettings"]
):
    """ToothFlankFractureAnalysisSettings

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToothFlankFractureAnalysisSettings")

    class _Cast_ToothFlankFractureAnalysisSettings:
        """Special nested class for casting ToothFlankFractureAnalysisSettings to subclasses."""

        def __init__(
            self: "ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings",
            parent: "ToothFlankFractureAnalysisSettings",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def tooth_flank_fracture_analysis_settings(
            self: "ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings",
        ) -> "ToothFlankFractureAnalysisSettings":
            return self._parent

        def __getattr__(
            self: "ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings",
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
        self: Self, instance_to_wrap: "ToothFlankFractureAnalysisSettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_analysis_according_to_the_french_proposal_n1457(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeAnalysisAccordingToTheFrenchProposalN1457

        if temp is None:
            return False

        return temp

    @include_analysis_according_to_the_french_proposal_n1457.setter
    @enforce_parameter_types
    def include_analysis_according_to_the_french_proposal_n1457(
        self: Self, value: "bool"
    ):
        self.wrapped.IncludeAnalysisAccordingToTheFrenchProposalN1457 = (
            bool(value) if value is not None else False
        )

    @property
    def measured_residual_stress_profile_property(
        self: Self,
    ) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.MeasuredResidualStressProfileProperty

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @measured_residual_stress_profile_property.setter
    @enforce_parameter_types
    def measured_residual_stress_profile_property(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.MeasuredResidualStressProfileProperty = value.wrapped

    @property
    def residual_stress_calculation_method(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_ResidualStressCalculationMethod"
    ):
        """EnumWithSelectedValue[mastapy.gears.gear_designs.cylindrical.ResidualStressCalculationMethod]"""
        temp = self.wrapped.ResidualStressCalculationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ResidualStressCalculationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @residual_stress_calculation_method.setter
    @enforce_parameter_types
    def residual_stress_calculation_method(
        self: Self, value: "_1074.ResidualStressCalculationMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ResidualStressCalculationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ResidualStressCalculationMethod = value

    @property
    def use_enhanced_calculation_with_residual_stress_sensitivity(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseEnhancedCalculationWithResidualStressSensitivity

        if temp is None:
            return False

        return temp

    @use_enhanced_calculation_with_residual_stress_sensitivity.setter
    @enforce_parameter_types
    def use_enhanced_calculation_with_residual_stress_sensitivity(
        self: Self, value: "bool"
    ):
        self.wrapped.UseEnhancedCalculationWithResidualStressSensitivity = (
            bool(value) if value is not None else False
        )

    @property
    def muller_residual_stress_calculator(
        self: Self,
    ) -> "_1068.MullerResidualStressDefinition":
        """mastapy.gears.gear_designs.cylindrical.MullerResidualStressDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MullerResidualStressCalculator

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ToothFlankFractureAnalysisSettings._Cast_ToothFlankFractureAnalysisSettings":
        return self._Cast_ToothFlankFractureAnalysisSettings(self)
