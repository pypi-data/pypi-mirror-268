"""StiffnessOptionsForHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, List
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5777
from mastapy.system_model.analyses_and_results.analysis_cases import _7544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STIFFNESS_OPTIONS_FOR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "StiffnessOptionsForHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.math_utility import _1542


__docformat__ = "restructuredtext en"
__all__ = ("StiffnessOptionsForHarmonicAnalysis",)


Self = TypeVar("Self", bound="StiffnessOptionsForHarmonicAnalysis")


class StiffnessOptionsForHarmonicAnalysis(
    _7544.AbstractAnalysisOptions["_6813.StaticLoadCase"]
):
    """StiffnessOptionsForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STIFFNESS_OPTIONS_FOR_HARMONIC_ANALYSIS

    class StepCreation(Enum):
        """StepCreation is a nested enum."""

        @classmethod
        def type_(cls):
            return _STIFFNESS_OPTIONS_FOR_HARMONIC_ANALYSIS.StepCreation

        GENERATE_STEPS_DISTRIBUTED_IN_TORQUE = 0
        GENERATE_STEPS_DISTRIBUTED_IN_SPEED = 1
        USE_POINTS_OF_TORQUE_SPEED_CURVE = 2
        USERSPECIFIED_TORQUES = 3
        USERSPECIFIED_SPEEDS = 4

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    StepCreation.__setattr__ = __enum_setattr
    StepCreation.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StiffnessOptionsForHarmonicAnalysis")

    class _Cast_StiffnessOptionsForHarmonicAnalysis:
        """Special nested class for casting StiffnessOptionsForHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StiffnessOptionsForHarmonicAnalysis._Cast_StiffnessOptionsForHarmonicAnalysis",
            parent: "StiffnessOptionsForHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_analysis_options(
            self: "StiffnessOptionsForHarmonicAnalysis._Cast_StiffnessOptionsForHarmonicAnalysis",
        ) -> "_7544.AbstractAnalysisOptions":
            return self._parent._cast(_7544.AbstractAnalysisOptions)

        @property
        def stiffness_options_for_harmonic_analysis(
            self: "StiffnessOptionsForHarmonicAnalysis._Cast_StiffnessOptionsForHarmonicAnalysis",
        ) -> "StiffnessOptionsForHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StiffnessOptionsForHarmonicAnalysis._Cast_StiffnessOptionsForHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "StiffnessOptionsForHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def curve_with_stiffness_steps(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurveWithStiffnessSteps

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def number_of_stiffness_steps(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfStiffnessSteps

        if temp is None:
            return 0

        return temp

    @number_of_stiffness_steps.setter
    @enforce_parameter_types
    def number_of_stiffness_steps(self: Self, value: "int"):
        self.wrapped.NumberOfStiffnessSteps = int(value) if value is not None else 0

    @property
    def step_creation_option(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.harmonic_analyses.StiffnessOptionsForHarmonicAnalysis.StepCreation]"""
        temp = self.wrapped.StepCreationOption

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @step_creation_option.setter
    @enforce_parameter_types
    def step_creation_option(
        self: Self, value: "StiffnessOptionsForHarmonicAnalysis.StepCreation"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_StiffnessOptionsForHarmonicAnalysis_StepCreation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.StepCreationOption = value

    @property
    def torque_input_type(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_HarmonicAnalysisTorqueInputType"
    ):
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisTorqueInputType]"""
        temp = self.wrapped.TorqueInputType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicAnalysisTorqueInputType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @torque_input_type.setter
    @enforce_parameter_types
    def torque_input_type(self: Self, value: "_5777.HarmonicAnalysisTorqueInputType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicAnalysisTorqueInputType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TorqueInputType = value

    @property
    def torque_speed_curve(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.TorqueSpeedCurve

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @torque_speed_curve.setter
    @enforce_parameter_types
    def torque_speed_curve(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.TorqueSpeedCurve = value.wrapped

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

    def create_load_cases_from_steps(self: Self):
        """Method does not return."""
        self.wrapped.CreateLoadCasesFromSteps()

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
    def cast_to(
        self: Self,
    ) -> (
        "StiffnessOptionsForHarmonicAnalysis._Cast_StiffnessOptionsForHarmonicAnalysis"
    ):
        return self._Cast_StiffnessOptionsForHarmonicAnalysis(self)
