"""ParametricStudyToolOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import (
    enum_with_selected_value,
    overridable,
    list_with_selected_item,
)
from mastapy.system_model.analyses_and_results.static_loads import _6826
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_TOOL_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ParametricStudyToolOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6936
    from mastapy.system_model import _2216, _2210
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4399,
        _4400,
    )
    from mastapy.system_model.analyses_and_results import _2656
    from mastapy.math_utility.convergence import _1582


__docformat__ = "restructuredtext en"
__all__ = ("ParametricStudyToolOptions",)


Self = TypeVar("Self", bound="ParametricStudyToolOptions")


class ParametricStudyToolOptions(_0.APIBase):
    """ParametricStudyToolOptions

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_TOOL_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParametricStudyToolOptions")

    class _Cast_ParametricStudyToolOptions:
        """Special nested class for casting ParametricStudyToolOptions to subclasses."""

        def __init__(
            self: "ParametricStudyToolOptions._Cast_ParametricStudyToolOptions",
            parent: "ParametricStudyToolOptions",
        ):
            self._parent = parent

        @property
        def parametric_study_tool_options(
            self: "ParametricStudyToolOptions._Cast_ParametricStudyToolOptions",
        ) -> "ParametricStudyToolOptions":
            return self._parent

        def __getattr__(
            self: "ParametricStudyToolOptions._Cast_ParametricStudyToolOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParametricStudyToolOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_AnalysisType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.static_loads.AnalysisType]"""
        temp = self.wrapped.AnalysisType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_AnalysisType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @analysis_type.setter
    @enforce_parameter_types
    def analysis_type(self: Self, value: "_6826.AnalysisType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_AnalysisType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.AnalysisType = value

    @property
    def changing_design(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ChangingDesign

        if temp is None:
            return False

        return temp

    @changing_design.setter
    @enforce_parameter_types
    def changing_design(self: Self, value: "bool"):
        self.wrapped.ChangingDesign = bool(value) if value is not None else False

    @property
    def folder_path_for_saved_files(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FolderPathForSavedFiles

        if temp is None:
            return ""

        return temp

    @property
    def is_logging_data(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsLoggingData

        if temp is None:
            return False

        return temp

    @is_logging_data.setter
    @enforce_parameter_types
    def is_logging_data(self: Self, value: "bool"):
        self.wrapped.IsLoggingData = bool(value) if value is not None else False

    @property
    def log_report(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LogReport

        if temp is None:
            return False

        return temp

    @log_report.setter
    @enforce_parameter_types
    def log_report(self: Self, value: "bool"):
        self.wrapped.LogReport = bool(value) if value is not None else False

    @property
    def maximum_number_of_design_copies_to_use(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.MaximumNumberOfDesignCopiesToUse

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @maximum_number_of_design_copies_to_use.setter
    @enforce_parameter_types
    def maximum_number_of_design_copies_to_use(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.MaximumNumberOfDesignCopiesToUse = value

    @property
    def number_of_analysis_dimensions(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfAnalysisDimensions

        if temp is None:
            return 0

        return temp

    @number_of_analysis_dimensions.setter
    @enforce_parameter_types
    def number_of_analysis_dimensions(self: Self, value: "int"):
        self.wrapped.NumberOfAnalysisDimensions = int(value) if value is not None else 0

    @property
    def number_of_steps(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfSteps

        if temp is None:
            return 0

        return temp

    @property
    def parametric_study_type(self: Self) -> "_6936.ParametricStudyType":
        """mastapy.system_model.analyses_and_results.static_loads.ParametricStudyType"""
        temp = self.wrapped.ParametricStudyType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.ParametricStudyType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.static_loads._6936",
            "ParametricStudyType",
        )(value)

    @parametric_study_type.setter
    @enforce_parameter_types
    def parametric_study_type(self: Self, value: "_6936.ParametricStudyType"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.ParametricStudyType",
        )
        self.wrapped.ParametricStudyType = value

    @property
    def perform_system_optimisation_pst_post_analysis(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.PerformSystemOptimisationPSTPostAnalysis

        if temp is None:
            return False

        return temp

    @perform_system_optimisation_pst_post_analysis.setter
    @enforce_parameter_types
    def perform_system_optimisation_pst_post_analysis(self: Self, value: "bool"):
        self.wrapped.PerformSystemOptimisationPSTPostAnalysis = (
            bool(value) if value is not None else False
        )

    @property
    def put_newly_added_numerical_variables_into(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.PutNewlyAddedNumericalVariablesInto

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @put_newly_added_numerical_variables_into.setter
    @enforce_parameter_types
    def put_newly_added_numerical_variables_into(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.PutNewlyAddedNumericalVariablesInto = value

    @property
    def save_design_at_each_step(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SaveDesignAtEachStep

        if temp is None:
            return False

        return temp

    @save_design_at_each_step.setter
    @enforce_parameter_types
    def save_design_at_each_step(self: Self, value: "bool"):
        self.wrapped.SaveDesignAtEachStep = bool(value) if value is not None else False

    @property
    def steps_for_statistical_study(self: Self) -> "int":
        """int"""
        temp = self.wrapped.StepsForStatisticalStudy

        if temp is None:
            return 0

        return temp

    @steps_for_statistical_study.setter
    @enforce_parameter_types
    def steps_for_statistical_study(self: Self, value: "int"):
        self.wrapped.StepsForStatisticalStudy = int(value) if value is not None else 0

    @property
    def steps_in_dimension_1(self: Self) -> "int":
        """int"""
        temp = self.wrapped.StepsInDimension1

        if temp is None:
            return 0

        return temp

    @steps_in_dimension_1.setter
    @enforce_parameter_types
    def steps_in_dimension_1(self: Self, value: "int"):
        self.wrapped.StepsInDimension1 = int(value) if value is not None else 0

    @property
    def steps_in_dimension_2(self: Self) -> "int":
        """int"""
        temp = self.wrapped.StepsInDimension2

        if temp is None:
            return 0

        return temp

    @steps_in_dimension_2.setter
    @enforce_parameter_types
    def steps_in_dimension_2(self: Self, value: "int"):
        self.wrapped.StepsInDimension2 = int(value) if value is not None else 0

    @property
    def use_multiple_designs(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.UseMultipleDesigns

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @use_multiple_designs.setter
    @enforce_parameter_types
    def use_multiple_designs(self: Self, value: "Union[bool, Tuple[bool, bool]]"):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.UseMultipleDesigns = value

    @property
    def external_full_fe_loader(self: Self) -> "_2216.ExternalFullFELoader":
        """mastapy.system_model.ExternalFullFELoader

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExternalFullFELoader

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def step_results(self: Self) -> "List[_4399.ParametricStudyToolStepResult]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyToolStepResult]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StepResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def study_variables(self: Self) -> "List[_4400.ParametricStudyVariable]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyVariable]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StudyVariables

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def parametric_study_logging_variables(
        self: Self,
    ) -> "List[_2656.AnalysisCaseVariable]":
        """List[mastapy.system_model.analyses_and_results.AnalysisCaseVariable]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyLoggingVariables

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

    def edit_folder_path(self: Self):
        """Method does not return."""
        self.wrapped.EditFolderPath()

    @enforce_parameter_types
    def add_logging_variable(
        self: Self, design_entity: "_2210.DesignEntity", path: "List[str]"
    ) -> "_2656.AnalysisCaseVariable":
        """mastapy.system_model.analyses_and_results.AnalysisCaseVariable

        Args:
            design_entity (mastapy.system_model.DesignEntity)
            path (List[str])
        """
        path = conversion.to_list_any(path)
        method_result = self.wrapped.AddLoggingVariable(
            design_entity.wrapped if design_entity else None, path
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def add_study_variable(
        self: Self, design_entity: "_2210.DesignEntity", path: "List[str]"
    ) -> "_4400.ParametricStudyVariable":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyVariable

        Args:
            design_entity (mastapy.system_model.DesignEntity)
            path (List[str])
        """
        path = conversion.to_list_any(path)
        method_result = self.wrapped.AddStudyVariable(
            design_entity.wrapped if design_entity else None, path
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def data_logger_for(
        self: Self, design_entity: "_2210.DesignEntity"
    ) -> "_1582.DataLogger":
        """mastapy.math_utility.convergence.DataLogger

        Args:
            design_entity (mastapy.system_model.DesignEntity)
        """
        method_result = self.wrapped.DataLoggerFor(
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def move_study_variable_down(
        self: Self, study_variable: "_4400.ParametricStudyVariable"
    ):
        """Method does not return.

        Args:
            study_variable (mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyVariable)
        """
        self.wrapped.MoveStudyVariableDown(
            study_variable.wrapped if study_variable else None
        )

    @enforce_parameter_types
    def move_study_variable_up(
        self: Self, study_variable: "_4400.ParametricStudyVariable"
    ):
        """Method does not return.

        Args:
            study_variable (mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyVariable)
        """
        self.wrapped.MoveStudyVariableUp(
            study_variable.wrapped if study_variable else None
        )

    @enforce_parameter_types
    def remove_logging_variable(
        self: Self, analysis_variable: "_2656.AnalysisCaseVariable"
    ):
        """Method does not return.

        Args:
            analysis_variable (mastapy.system_model.analyses_and_results.AnalysisCaseVariable)
        """
        self.wrapped.RemoveLoggingVariable(
            analysis_variable.wrapped if analysis_variable else None
        )

    @enforce_parameter_types
    def remove_study_variable(
        self: Self, study_variable: "_4400.ParametricStudyVariable"
    ):
        """Method does not return.

        Args:
            study_variable (mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyVariable)
        """
        self.wrapped.RemoveStudyVariable(
            study_variable.wrapped if study_variable else None
        )

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
    ) -> "ParametricStudyToolOptions._Cast_ParametricStudyToolOptions":
        return self._Cast_ParametricStudyToolOptions(self)
