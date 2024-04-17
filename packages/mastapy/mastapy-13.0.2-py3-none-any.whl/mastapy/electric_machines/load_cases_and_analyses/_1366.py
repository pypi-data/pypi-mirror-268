"""ElectricMachineLoadCaseBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_LOAD_CASE_BASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "ElectricMachineLoadCaseBase"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import (
        _1384,
        _1359,
        _1367,
        _1353,
        _1355,
        _1358,
        _1365,
        _1368,
        _1374,
        _1382,
        _1383,
    )
    from mastapy.electric_machines import _1273


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineLoadCaseBase",)


Self = TypeVar("Self", bound="ElectricMachineLoadCaseBase")


class ElectricMachineLoadCaseBase(_0.APIBase):
    """ElectricMachineLoadCaseBase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_LOAD_CASE_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineLoadCaseBase")

    class _Cast_ElectricMachineLoadCaseBase:
        """Special nested class for casting ElectricMachineLoadCaseBase to subclasses."""

        def __init__(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
            parent: "ElectricMachineLoadCaseBase",
        ):
            self._parent = parent

        @property
        def basic_dynamic_force_load_case(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
        ) -> "_1353.BasicDynamicForceLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1353

            return self._parent._cast(_1353.BasicDynamicForceLoadCase)

        @property
        def dynamic_force_load_case(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
        ) -> "_1355.DynamicForceLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1355

            return self._parent._cast(_1355.DynamicForceLoadCase)

        @property
        def efficiency_map_load_case(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
        ) -> "_1358.EfficiencyMapLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1358

            return self._parent._cast(_1358.EfficiencyMapLoadCase)

        @property
        def electric_machine_load_case(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
        ) -> "_1365.ElectricMachineLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1365

            return self._parent._cast(_1365.ElectricMachineLoadCase)

        @property
        def electric_machine_mechanical_load_case(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
        ) -> "_1368.ElectricMachineMechanicalLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1368

            return self._parent._cast(_1368.ElectricMachineMechanicalLoadCase)

        @property
        def non_linear_dq_model_multiple_operating_points_load_case(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
        ) -> "_1374.NonLinearDQModelMultipleOperatingPointsLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1374

            return self._parent._cast(
                _1374.NonLinearDQModelMultipleOperatingPointsLoadCase
            )

        @property
        def speed_torque_curve_load_case(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
        ) -> "_1382.SpeedTorqueCurveLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1382

            return self._parent._cast(_1382.SpeedTorqueCurveLoadCase)

        @property
        def speed_torque_load_case(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
        ) -> "_1383.SpeedTorqueLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1383

            return self._parent._cast(_1383.SpeedTorqueLoadCase)

        @property
        def electric_machine_load_case_base(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
        ) -> "ElectricMachineLoadCaseBase":
            return self._parent

        def __getattr__(
            self: "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineLoadCaseBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def folder_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FolderPath

        if temp is None:
            return ""

        return temp

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
    def temperatures(self: Self) -> "_1384.Temperatures":
        """mastapy.electric_machines.load_cases_and_analyses.Temperatures

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Temperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def analyses(self: Self) -> "List[_1359.ElectricMachineAnalysis]":
        """List[mastapy.electric_machines.load_cases_and_analyses.ElectricMachineAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Analyses

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
    def analysis_for(
        self: Self, setup: "_1273.ElectricMachineSetup"
    ) -> "_1359.ElectricMachineAnalysis":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineAnalysis

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
        """
        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def copy_to(
        self: Self, another_group: "_1367.ElectricMachineLoadCaseGroup"
    ) -> "ElectricMachineLoadCaseBase":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase

        Args:
            another_group (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseGroup)
        """
        method_result = self.wrapped.CopyTo(
            another_group.wrapped if another_group else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def remove_analysis(
        self: Self, electric_machine_analysis: "_1359.ElectricMachineAnalysis"
    ):
        """Method does not return.

        Args:
            electric_machine_analysis (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineAnalysis)
        """
        self.wrapped.RemoveAnalysis(
            electric_machine_analysis.wrapped if electric_machine_analysis else None
        )

    @enforce_parameter_types
    def remove_analysis_for(self: Self, setup: "_1273.ElectricMachineSetup"):
        """Method does not return.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
        """
        self.wrapped.RemoveAnalysisFor(setup.wrapped if setup else None)

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
    ) -> "ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase":
        return self._Cast_ElectricMachineLoadCaseBase(self)
