"""TimeSeriesImporter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
    _7000,
)
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_SERIES_IMPORTER = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "TimeSeriesImporter",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.system_model.analyses_and_results.static_loads import _6917
    from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _6999,
        _7002,
        _7003,
        _7011,
        _6998,
        _7005,
        _7001,
        _7004,
        _7009,
        _7012,
    )
    from mastapy.utility.file_access_helpers import _1824


__docformat__ = "restructuredtext en"
__all__ = ("TimeSeriesImporter",)


Self = TypeVar("Self", bound="TimeSeriesImporter")


class TimeSeriesImporter(_0.APIBase):
    """TimeSeriesImporter

    This is a mastapy class.
    """

    TYPE = _TIME_SERIES_IMPORTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TimeSeriesImporter")

    class _Cast_TimeSeriesImporter:
        """Special nested class for casting TimeSeriesImporter to subclasses."""

        def __init__(
            self: "TimeSeriesImporter._Cast_TimeSeriesImporter",
            parent: "TimeSeriesImporter",
        ):
            self._parent = parent

        @property
        def time_series_importer(
            self: "TimeSeriesImporter._Cast_TimeSeriesImporter",
        ) -> "TimeSeriesImporter":
            return self._parent

        def __getattr__(self: "TimeSeriesImporter._Cast_TimeSeriesImporter", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TimeSeriesImporter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def boost_pressure_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoostPressureChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def create_load_cases_for_parametric_study_tool(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CreateLoadCasesForParametricStudyTool

        if temp is None:
            return False

        return temp

    @create_load_cases_for_parametric_study_tool.setter
    @enforce_parameter_types
    def create_load_cases_for_parametric_study_tool(self: Self, value: "bool"):
        self.wrapped.CreateLoadCasesForParametricStudyTool = (
            bool(value) if value is not None else False
        )

    @property
    def design_state_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DesignStateName

        if temp is None:
            return ""

        return temp

    @design_state_name.setter
    @enforce_parameter_types
    def design_state_name(self: Self, value: "str"):
        self.wrapped.DesignStateName = str(value) if value is not None else ""

    @property
    def destination_design_state_column(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DestinationDesignState":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.DestinationDesignState]"""
        temp = self.wrapped.DestinationDesignStateColumn

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DestinationDesignState.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @destination_design_state_column.setter
    @enforce_parameter_types
    def destination_design_state_column(
        self: Self, value: "_7000.DestinationDesignState"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DestinationDesignState.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DestinationDesignStateColumn = value

    @property
    def duty_cycle_duration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DutyCycleDuration

        if temp is None:
            return 0.0

        return temp

    @duty_cycle_duration.setter
    @enforce_parameter_types
    def duty_cycle_duration(self: Self, value: "float"):
        self.wrapped.DutyCycleDuration = float(value) if value is not None else 0.0

    @property
    def force_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratios(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatios

        if temp is None:
            return ""

        return temp

    @property
    def import_type(self: Self) -> "_6917.ImportType":
        """mastapy.system_model.analyses_and_results.static_loads.ImportType"""
        temp = self.wrapped.ImportType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.ImportType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.static_loads._6917", "ImportType"
        )(value)

    @import_type.setter
    @enforce_parameter_types
    def import_type(self: Self, value: "_6917.ImportType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.ImportType"
        )
        self.wrapped.ImportType = value

    @property
    def moment_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def number_of_boost_pressure_inputs(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfBoostPressureInputs

        if temp is None:
            return 0

        return temp

    @number_of_boost_pressure_inputs.setter
    @enforce_parameter_types
    def number_of_boost_pressure_inputs(self: Self, value: "int"):
        self.wrapped.NumberOfBoostPressureInputs = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_cycle_repeats(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfCycleRepeats

        if temp is None:
            return 0.0

        return temp

    @number_of_cycle_repeats.setter
    @enforce_parameter_types
    def number_of_cycle_repeats(self: Self, value: "float"):
        self.wrapped.NumberOfCycleRepeats = float(value) if value is not None else 0.0

    @property
    def number_of_data_files(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfDataFiles

        if temp is None:
            return 0

        return temp

    @number_of_data_files.setter
    @enforce_parameter_types
    def number_of_data_files(self: Self, value: "int"):
        self.wrapped.NumberOfDataFiles = int(value) if value is not None else 0

    @property
    def number_of_extra_points_for_ramp_sections(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfExtraPointsForRampSections

        if temp is None:
            return 0

        return temp

    @number_of_extra_points_for_ramp_sections.setter
    @enforce_parameter_types
    def number_of_extra_points_for_ramp_sections(self: Self, value: "int"):
        self.wrapped.NumberOfExtraPointsForRampSections = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_force_inputs(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfForceInputs

        if temp is None:
            return 0

        return temp

    @number_of_force_inputs.setter
    @enforce_parameter_types
    def number_of_force_inputs(self: Self, value: "int"):
        self.wrapped.NumberOfForceInputs = int(value) if value is not None else 0

    @property
    def number_of_moment_inputs(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfMomentInputs

        if temp is None:
            return 0

        return temp

    @number_of_moment_inputs.setter
    @enforce_parameter_types
    def number_of_moment_inputs(self: Self, value: "int"):
        self.wrapped.NumberOfMomentInputs = int(value) if value is not None else 0

    @property
    def number_of_speed_inputs(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSpeedInputs

        if temp is None:
            return 0

        return temp

    @number_of_speed_inputs.setter
    @enforce_parameter_types
    def number_of_speed_inputs(self: Self, value: "int"):
        self.wrapped.NumberOfSpeedInputs = int(value) if value is not None else 0

    @property
    def number_of_torque_inputs(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTorqueInputs

        if temp is None:
            return 0

        return temp

    @number_of_torque_inputs.setter
    @enforce_parameter_types
    def number_of_torque_inputs(self: Self, value: "int"):
        self.wrapped.NumberOfTorqueInputs = int(value) if value is not None else 0

    @property
    def specify_load_case_names(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyLoadCaseNames

        if temp is None:
            return False

        return temp

    @specify_load_case_names.setter
    @enforce_parameter_types
    def specify_load_case_names(self: Self, value: "bool"):
        self.wrapped.SpecifyLoadCaseNames = bool(value) if value is not None else False

    @property
    def speed_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def torque_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def design_state_options(self: Self) -> "_6999.DesignStateOptions":
        """mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.DesignStateOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignStateOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratio_options(self: Self) -> "_7002.GearRatioInputOptions":
        """mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.GearRatioInputOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatioOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_case_name_inputs(self: Self) -> "_7003.LoadCaseNameOptions":
        """mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.LoadCaseNameOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseNameInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_step_input(self: Self) -> "_7011.TimeStepInputOptions":
        """mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.TimeStepInputOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeStepInput

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def boost_pressure_inputs(
        self: Self,
    ) -> "List[_6998.BoostPressureLoadCaseInputOptions]":
        """List[mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.BoostPressureLoadCaseInputOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoostPressureInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def file_inputs(self: Self) -> "List[_7005.MultiTimeSeriesDataInputFileOptions]":
        """List[mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.MultiTimeSeriesDataInputFileOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FileInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def force_inputs(self: Self) -> "List[_7001.ForceInputOptions]":
        """List[mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.ForceInputOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def moment_inputs(self: Self) -> "List[_7004.MomentInputOptions]":
        """List[mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.MomentInputOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def speed_inputs(self: Self) -> "List[_7009.SpeedInputOptions]":
        """List[mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.SpeedInputOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def torque_inputs(self: Self) -> "List[_7012.TorqueInputOptions]":
        """List[mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition.TorqueInputOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueInputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def columns(self: Self) -> "List[_1824.ColumnTitle]":
        """List[mastapy.utility.file_access_helpers.ColumnTitle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Columns

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

    def create_load_cases(self: Self):
        """Method does not return."""
        self.wrapped.CreateLoadCases()

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
    def cast_to(self: Self) -> "TimeSeriesImporter._Cast_TimeSeriesImporter":
        return self._Cast_TimeSeriesImporter(self)
