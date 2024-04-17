"""WhineWaterfallSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, Union, Tuple, List
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.system_model.analyses_and_results.modal_analyses import _4634, _4635
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.math_utility import _1502, _1534
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WHINE_WATERFALL_SETTINGS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "WhineWaterfallSettings",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.results import (
        _5852,
        _5860,
        _5855,
        _5861,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4617,
        _4667,
        _4716,
        _4669,
        _4715,
    )
    from mastapy.math_utility import _1541, _1527
    from mastapy.math_utility.measured_data_scaling import _1576
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5760,
        _5774,
        _5819,
    )
    from mastapy.system_model.drawing.options import _2270, _2268
    from mastapy.utility.property import _1850


__docformat__ = "restructuredtext en"
__all__ = ("WhineWaterfallSettings",)


Self = TypeVar("Self", bound="WhineWaterfallSettings")


class WhineWaterfallSettings(_0.APIBase):
    """WhineWaterfallSettings

    This is a mastapy class.
    """

    TYPE = _WHINE_WATERFALL_SETTINGS

    class SpeedBoundaryHandling(Enum):
        """SpeedBoundaryHandling is a nested enum."""

        @classmethod
        def type_(cls):
            return _WHINE_WATERFALL_SETTINGS.SpeedBoundaryHandling

        SHOW_DISCONTINUITY = 0
        SHOW_VERTICAL_LINE = 1
        TAKE_MAXIMUM = 2
        TAKE_AVERAGE = 3

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    SpeedBoundaryHandling.__setattr__ = __enum_setattr
    SpeedBoundaryHandling.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WhineWaterfallSettings")

    class _Cast_WhineWaterfallSettings:
        """Special nested class for casting WhineWaterfallSettings to subclasses."""

        def __init__(
            self: "WhineWaterfallSettings._Cast_WhineWaterfallSettings",
            parent: "WhineWaterfallSettings",
        ):
            self._parent = parent

        @property
        def whine_waterfall_settings(
            self: "WhineWaterfallSettings._Cast_WhineWaterfallSettings",
        ) -> "WhineWaterfallSettings":
            return self._parent

        def __getattr__(
            self: "WhineWaterfallSettings._Cast_WhineWaterfallSettings", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WhineWaterfallSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def boundary_handling(self: Self) -> "WhineWaterfallSettings.SpeedBoundaryHandling":
        """mastapy.system_model.analyses_and_results.modal_analyses.WhineWaterfallSettings.SpeedBoundaryHandling"""
        temp = self.wrapped.BoundaryHandling

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.WhineWaterfallSettings+SpeedBoundaryHandling",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.modal_analyses.WhineWaterfallSettings.WhineWaterfallSettings",
            "SpeedBoundaryHandling",
        )(value)

    @boundary_handling.setter
    @enforce_parameter_types
    def boundary_handling(
        self: Self, value: "WhineWaterfallSettings.SpeedBoundaryHandling"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.WhineWaterfallSettings+SpeedBoundaryHandling",
        )
        self.wrapped.BoundaryHandling = value

    @property
    def chart_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DynamicsResponse3DChartType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.modal_analyses.DynamicsResponse3DChartType]"""
        temp = self.wrapped.ChartType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DynamicsResponse3DChartType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @chart_type.setter
    @enforce_parameter_types
    def chart_type(self: Self, value: "_4634.DynamicsResponse3DChartType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DynamicsResponse3DChartType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ChartType = value

    @property
    def complex_component(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ComplexPartDisplayOption":
        """EnumWithSelectedValue[mastapy.math_utility.ComplexPartDisplayOption]"""
        temp = self.wrapped.ComplexComponent

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ComplexPartDisplayOption.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @complex_component.setter
    @enforce_parameter_types
    def complex_component(self: Self, value: "_1502.ComplexPartDisplayOption"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ComplexPartDisplayOption.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ComplexComponent = value

    @property
    def connected_component_type(self: Self) -> "_5852.ConnectedComponentType":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.results.ConnectedComponentType"""
        temp = self.wrapped.ConnectedComponentType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ConnectedComponentType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.harmonic_analyses.results._5852",
            "ConnectedComponentType",
        )(value)

    @connected_component_type.setter
    @enforce_parameter_types
    def connected_component_type(self: Self, value: "_5852.ConnectedComponentType"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ConnectedComponentType",
        )
        self.wrapped.ConnectedComponentType = value

    @property
    def coordinate_system(self: Self) -> "_4617.CoordinateSystemForWhine":
        """mastapy.system_model.analyses_and_results.modal_analyses.CoordinateSystemForWhine"""
        temp = self.wrapped.CoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.CoordinateSystemForWhine",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.modal_analyses._4617",
            "CoordinateSystemForWhine",
        )(value)

    @coordinate_system.setter
    @enforce_parameter_types
    def coordinate_system(self: Self, value: "_4617.CoordinateSystemForWhine"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.CoordinateSystemForWhine",
        )
        self.wrapped.CoordinateSystem = value

    @property
    def extend_torque_map_at_edges(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ExtendTorqueMapAtEdges

        if temp is None:
            return False

        return temp

    @extend_torque_map_at_edges.setter
    @enforce_parameter_types
    def extend_torque_map_at_edges(self: Self, value: "bool"):
        self.wrapped.ExtendTorqueMapAtEdges = (
            bool(value) if value is not None else False
        )

    @property
    def limit_to_max_under_torque_speed_curve(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LimitToMaxUnderTorqueSpeedCurve

        if temp is None:
            return False

        return temp

    @limit_to_max_under_torque_speed_curve.setter
    @enforce_parameter_types
    def limit_to_max_under_torque_speed_curve(self: Self, value: "bool"):
        self.wrapped.LimitToMaxUnderTorqueSpeedCurve = (
            bool(value) if value is not None else False
        )

    @property
    def max_harmonic(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.MaxHarmonic

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @max_harmonic.setter
    @enforce_parameter_types
    def max_harmonic(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.MaxHarmonic = value

    @property
    def maximum_order(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumOrder

        if temp is None:
            return 0.0

        return temp

    @maximum_order.setter
    @enforce_parameter_types
    def maximum_order(self: Self, value: "float"):
        self.wrapped.MaximumOrder = float(value) if value is not None else 0.0

    @property
    def minimum_order(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumOrder

        if temp is None:
            return 0.0

        return temp

    @minimum_order.setter
    @enforce_parameter_types
    def minimum_order(self: Self, value: "float"):
        self.wrapped.MinimumOrder = float(value) if value is not None else 0.0

    @property
    def number_of_additional_points_either_side_of_order_line(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfAdditionalPointsEitherSideOfOrderLine

        if temp is None:
            return 0

        return temp

    @number_of_additional_points_either_side_of_order_line.setter
    @enforce_parameter_types
    def number_of_additional_points_either_side_of_order_line(self: Self, value: "int"):
        self.wrapped.NumberOfAdditionalPointsEitherSideOfOrderLine = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_points_per_step(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfPointsPerStep

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_points_per_step.setter
    @enforce_parameter_types
    def number_of_points_per_step(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfPointsPerStep = value

    @property
    def overlay_torque_speed_curve(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverlayTorqueSpeedCurve

        if temp is None:
            return False

        return temp

    @overlay_torque_speed_curve.setter
    @enforce_parameter_types
    def overlay_torque_speed_curve(self: Self, value: "bool"):
        self.wrapped.OverlayTorqueSpeedCurve = (
            bool(value) if value is not None else False
        )

    @property
    def reduce_number_of_result_points(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ReduceNumberOfResultPoints

        if temp is None:
            return False

        return temp

    @reduce_number_of_result_points.setter
    @enforce_parameter_types
    def reduce_number_of_result_points(self: Self, value: "bool"):
        self.wrapped.ReduceNumberOfResultPoints = (
            bool(value) if value is not None else False
        )

    @property
    def replace_speed_axis_with_frequency(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ReplaceSpeedAxisWithFrequency

        if temp is None:
            return False

        return temp

    @replace_speed_axis_with_frequency.setter
    @enforce_parameter_types
    def replace_speed_axis_with_frequency(self: Self, value: "bool"):
        self.wrapped.ReplaceSpeedAxisWithFrequency = (
            bool(value) if value is not None else False
        )

    @property
    def response_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.modal_analyses.DynamicsResponseType]"""
        temp = self.wrapped.ResponseType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @response_type.setter
    @enforce_parameter_types
    def response_type(self: Self, value: "_4635.DynamicsResponseType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ResponseType = value

    @property
    def show_amplitudes_of_gear_excitations(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAmplitudesOfGearExcitations

        if temp is None:
            return False

        return temp

    @show_amplitudes_of_gear_excitations.setter
    @enforce_parameter_types
    def show_amplitudes_of_gear_excitations(self: Self, value: "bool"):
        self.wrapped.ShowAmplitudesOfGearExcitations = (
            bool(value) if value is not None else False
        )

    @property
    def show_boundaries_of_stiffness_steps(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowBoundariesOfStiffnessSteps

        if temp is None:
            return False

        return temp

    @show_boundaries_of_stiffness_steps.setter
    @enforce_parameter_types
    def show_boundaries_of_stiffness_steps(self: Self, value: "bool"):
        self.wrapped.ShowBoundariesOfStiffnessSteps = (
            bool(value) if value is not None else False
        )

    @property
    def show_coupled_modes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowCoupledModes

        if temp is None:
            return False

        return temp

    @show_coupled_modes.setter
    @enforce_parameter_types
    def show_coupled_modes(self: Self, value: "bool"):
        self.wrapped.ShowCoupledModes = bool(value) if value is not None else False

    @property
    def show_torques_at_stiffness_steps(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowTorquesAtStiffnessSteps

        if temp is None:
            return False

        return temp

    @show_torques_at_stiffness_steps.setter
    @enforce_parameter_types
    def show_torques_at_stiffness_steps(self: Self, value: "bool"):
        self.wrapped.ShowTorquesAtStiffnessSteps = (
            bool(value) if value is not None else False
        )

    @property
    def show_total_response_for_multiple_excitations(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowTotalResponseForMultipleExcitations

        if temp is None:
            return False

        return temp

    @show_total_response_for_multiple_excitations.setter
    @enforce_parameter_types
    def show_total_response_for_multiple_excitations(self: Self, value: "bool"):
        self.wrapped.ShowTotalResponseForMultipleExcitations = (
            bool(value) if value is not None else False
        )

    @property
    def show_total_response_for_multiple_surfaces(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowTotalResponseForMultipleSurfaces

        if temp is None:
            return False

        return temp

    @show_total_response_for_multiple_surfaces.setter
    @enforce_parameter_types
    def show_total_response_for_multiple_surfaces(self: Self, value: "bool"):
        self.wrapped.ShowTotalResponseForMultipleSurfaces = (
            bool(value) if value is not None else False
        )

    @property
    def speed_range_for_combining_excitations(
        self: Self,
    ) -> "_4667.MultipleExcitationsSpeedRangeOption":
        """mastapy.system_model.analyses_and_results.modal_analyses.MultipleExcitationsSpeedRangeOption"""
        temp = self.wrapped.SpeedRangeForCombiningExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.MultipleExcitationsSpeedRangeOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.modal_analyses._4667",
            "MultipleExcitationsSpeedRangeOption",
        )(value)

    @speed_range_for_combining_excitations.setter
    @enforce_parameter_types
    def speed_range_for_combining_excitations(
        self: Self, value: "_4667.MultipleExcitationsSpeedRangeOption"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.MultipleExcitationsSpeedRangeOption",
        )
        self.wrapped.SpeedRangeForCombiningExcitations = value

    @property
    def translation_or_rotation(self: Self) -> "_1541.TranslationRotation":
        """mastapy.math_utility.TranslationRotation"""
        temp = self.wrapped.TranslationOrRotation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.TranslationRotation"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1541", "TranslationRotation"
        )(value)

    @translation_or_rotation.setter
    @enforce_parameter_types
    def translation_or_rotation(self: Self, value: "_1541.TranslationRotation"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.TranslationRotation"
        )
        self.wrapped.TranslationOrRotation = value

    @property
    def vector_magnitude_method(self: Self) -> "_1527.ComplexMagnitudeMethod":
        """mastapy.math_utility.ComplexMagnitudeMethod"""
        temp = self.wrapped.VectorMagnitudeMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.ComplexMagnitudeMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1527", "ComplexMagnitudeMethod"
        )(value)

    @vector_magnitude_method.setter
    @enforce_parameter_types
    def vector_magnitude_method(self: Self, value: "_1527.ComplexMagnitudeMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.ComplexMagnitudeMethod"
        )
        self.wrapped.VectorMagnitudeMethod = value

    @property
    def whine_waterfall_export_option(self: Self) -> "_4716.WhineWaterfallExportOption":
        """mastapy.system_model.analyses_and_results.modal_analyses.WhineWaterfallExportOption"""
        temp = self.wrapped.WhineWaterfallExportOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.WhineWaterfallExportOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.modal_analyses._4716",
            "WhineWaterfallExportOption",
        )(value)

    @whine_waterfall_export_option.setter
    @enforce_parameter_types
    def whine_waterfall_export_option(
        self: Self, value: "_4716.WhineWaterfallExportOption"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.WhineWaterfallExportOption",
        )
        self.wrapped.WhineWaterfallExportOption = value

    @property
    def data_scaling(self: Self) -> "_1576.DataScalingOptions":
        """mastapy.math_utility.measured_data_scaling.DataScalingOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataScaling

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def frequency_options(
        self: Self,
    ) -> "_5760.FrequencyOptionsForHarmonicAnalysisResults":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FrequencyOptionsForHarmonicAnalysisResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_options(self: Self) -> "_5774.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_contribution_view_options(
        self: Self,
    ) -> "_2270.ModalContributionViewOptions":
        """mastapy.system_model.drawing.options.ModalContributionViewOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalContributionViewOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mode_view_options(
        self: Self,
    ) -> "_2268.AdvancedTimeSteppingAnalysisForModulationModeViewOptions":
        """mastapy.system_model.drawing.options.AdvancedTimeSteppingAnalysisForModulationModeViewOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModeViewOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def order_cuts_chart_settings(self: Self) -> "_4669.OrderCutsChartSettings":
        """mastapy.system_model.analyses_and_results.modal_analyses.OrderCutsChartSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OrderCutsChartSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def reference_speed_options(
        self: Self,
    ) -> "_5819.SpeedOptionsForHarmonicAnalysisResults":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpeedOptionsForHarmonicAnalysisResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceSpeedOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def result_location_selection_groups(
        self: Self,
    ) -> "_5860.ResultLocationSelectionGroups":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.results.ResultLocationSelectionGroups

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultLocationSelectionGroups

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_excitations(self: Self) -> "_5855.ExcitationSourceSelectionGroup":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.results.ExcitationSourceSelectionGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedExcitations

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def waterfall_chart_settings(self: Self) -> "_4715.WaterfallChartSettings":
        """mastapy.system_model.analyses_and_results.modal_analyses.WaterfallChartSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WaterfallChartSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def active_result_locations(self: Self) -> "List[_5861.ResultNodeSelection]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.results.ResultNodeSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveResultLocations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def degrees_of_freedom(
        self: Self,
    ) -> "List[_1850.EnumWithBoolean[_1534.ResultOptionsFor3DVector]]":
        """List[mastapy.utility.property.EnumWithBoolean[mastapy.math_utility.ResultOptionsFor3DVector]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DegreesOfFreedom

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def calculate_results(self: Self):
        """Method does not return."""
        self.wrapped.CalculateResults()

    def clear_cached_results(self: Self):
        """Method does not return."""
        self.wrapped.ClearCachedResults()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "WhineWaterfallSettings._Cast_WhineWaterfallSettings":
        return self._Cast_WhineWaterfallSettings(self)
