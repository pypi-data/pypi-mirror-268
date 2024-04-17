"""ElectricMachineLoadCaseGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "ElectricMachineLoadCaseGroup"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import (
        _1355,
        _1353,
        _1358,
        _1383,
        _1365,
        _1382,
        _1371,
        _1366,
    )
    from mastapy.electric_machines import _1273
    from mastapy.utility import _1597
    from mastapy import _7567


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineLoadCaseGroup",)


Self = TypeVar("Self", bound="ElectricMachineLoadCaseGroup")


class ElectricMachineLoadCaseGroup(_0.APIBase):
    """ElectricMachineLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineLoadCaseGroup")

    class _Cast_ElectricMachineLoadCaseGroup:
        """Special nested class for casting ElectricMachineLoadCaseGroup to subclasses."""

        def __init__(
            self: "ElectricMachineLoadCaseGroup._Cast_ElectricMachineLoadCaseGroup",
            parent: "ElectricMachineLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def electric_machine_load_case_group(
            self: "ElectricMachineLoadCaseGroup._Cast_ElectricMachineLoadCaseGroup",
        ) -> "ElectricMachineLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "ElectricMachineLoadCaseGroup._Cast_ElectricMachineLoadCaseGroup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineLoadCaseGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def dynamic_forces_load_cases(self: Self) -> "List[_1355.DynamicForceLoadCase]":
        """List[mastapy.electric_machines.load_cases_and_analyses.DynamicForceLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicForcesLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def dynamic_forces_load_cases_without_non_linear_dq_model(
        self: Self,
    ) -> "List[_1353.BasicDynamicForceLoadCase]":
        """List[mastapy.electric_machines.load_cases_and_analyses.BasicDynamicForceLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicForcesLoadCasesWithoutNonLinearDQModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def efficiency_map_load_cases(self: Self) -> "List[_1358.EfficiencyMapLoadCase]":
        """List[mastapy.electric_machines.load_cases_and_analyses.EfficiencyMapLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EfficiencyMapLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def single_operating_point_load_cases_with_non_linear_dq_model(
        self: Self,
    ) -> "List[_1383.SpeedTorqueLoadCase]":
        """List[mastapy.electric_machines.load_cases_and_analyses.SpeedTorqueLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleOperatingPointLoadCasesWithNonLinearDQModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def single_operating_point_load_cases_without_non_linear_dq_model(
        self: Self,
    ) -> "List[_1365.ElectricMachineLoadCase]":
        """List[mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleOperatingPointLoadCasesWithoutNonLinearDQModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def speed_torque_curve_load_cases(
        self: Self,
    ) -> "List[_1382.SpeedTorqueCurveLoadCase]":
        """List[mastapy.electric_machines.load_cases_and_analyses.SpeedTorqueCurveLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedTorqueCurveLoadCases

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

    @enforce_parameter_types
    def add_load_case(
        self: Self, load_case_type: "_1371.LoadCaseType"
    ) -> "_1366.ElectricMachineLoadCaseBase":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase

        Args:
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)
        """
        load_case_type = conversion.mp_to_pn_enum(
            load_case_type,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.LoadCaseType",
        )
        method_result = self.wrapped.AddLoadCase(load_case_type)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def add_load_case_named(
        self: Self, load_case_type: "_1371.LoadCaseType", name: "str"
    ) -> "_1366.ElectricMachineLoadCaseBase":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase

        Args:
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)
            name (str)
        """
        load_case_type = conversion.mp_to_pn_enum(
            load_case_type,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.LoadCaseType",
        )
        name = str(name)
        method_result = self.wrapped.AddLoadCaseNamed(
            load_case_type, name if name else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def load_case_named(
        self: Self, load_case_type: "_1371.LoadCaseType", name: "str"
    ) -> "_1366.ElectricMachineLoadCaseBase":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase

        Args:
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)
            name (str)
        """
        load_case_type = conversion.mp_to_pn_enum(
            load_case_type,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.LoadCaseType",
        )
        name = str(name)
        method_result = self.wrapped.LoadCaseNamed(load_case_type, name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def perform_compound_analysis(
        self: Self,
        setup: "_1273.ElectricMachineSetup",
        load_case_type: "_1371.LoadCaseType",
    ) -> "_1597.MethodOutcome":
        """mastapy.utility.MethodOutcome

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)
        """
        load_case_type = conversion.mp_to_pn_enum(
            load_case_type,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.LoadCaseType",
        )
        method_result = self.wrapped.PerformCompoundAnalysis(
            setup.wrapped if setup else None, load_case_type
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def perform_compound_analysis_with_progress(
        self: Self,
        setup: "_1273.ElectricMachineSetup",
        load_case_type: "_1371.LoadCaseType",
        task_progress: "_7567.TaskProgress",
    ) -> "_1597.MethodOutcome":
        """mastapy.utility.MethodOutcome

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)
            task_progress (mastapy.TaskProgress)
        """
        load_case_type = conversion.mp_to_pn_enum(
            load_case_type,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.LoadCaseType",
        )
        method_result = self.wrapped.PerformCompoundAnalysisWithProgress(
            setup.wrapped if setup else None,
            load_case_type,
            task_progress.wrapped if task_progress else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def remove_all_electric_machine_load_cases(self: Self):
        """Method does not return."""
        self.wrapped.RemoveAllElectricMachineLoadCases()

    @enforce_parameter_types
    def try_remove_load_case(
        self: Self, load_case: "_1366.ElectricMachineLoadCaseBase"
    ) -> "bool":
        """bool

        Args:
            load_case (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase)
        """
        method_result = self.wrapped.TryRemoveLoadCase(
            load_case.wrapped if load_case else None
        )
        return method_result

    @enforce_parameter_types
    def try_remove_load_case_named(
        self: Self, load_case_type: "_1371.LoadCaseType", name: "str"
    ) -> "bool":
        """bool

        Args:
            load_case_type (mastapy.electric_machines.load_cases_and_analyses.LoadCaseType)
            name (str)
        """
        load_case_type = conversion.mp_to_pn_enum(
            load_case_type,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.LoadCaseType",
        )
        name = str(name)
        method_result = self.wrapped.TryRemoveLoadCaseNamed(
            load_case_type, name if name else ""
        )
        return method_result

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
    ) -> "ElectricMachineLoadCaseGroup._Cast_ElectricMachineLoadCaseGroup":
        return self._Cast_ElectricMachineLoadCaseGroup(self)
