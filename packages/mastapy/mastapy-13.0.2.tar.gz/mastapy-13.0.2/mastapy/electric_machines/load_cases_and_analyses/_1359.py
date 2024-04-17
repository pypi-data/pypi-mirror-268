"""ElectricMachineAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "ElectricMachineAnalysis"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1268, _1273
    from mastapy.electric_machines.load_cases_and_analyses import (
        _1366,
        _1354,
        _1357,
        _1363,
        _1364,
        _1377,
        _1381,
    )
    from mastapy import _7567


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineAnalysis",)


Self = TypeVar("Self", bound="ElectricMachineAnalysis")


class ElectricMachineAnalysis(_0.APIBase):
    """ElectricMachineAnalysis

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineAnalysis")

    class _Cast_ElectricMachineAnalysis:
        """Special nested class for casting ElectricMachineAnalysis to subclasses."""

        def __init__(
            self: "ElectricMachineAnalysis._Cast_ElectricMachineAnalysis",
            parent: "ElectricMachineAnalysis",
        ):
            self._parent = parent

        @property
        def dynamic_force_analysis(
            self: "ElectricMachineAnalysis._Cast_ElectricMachineAnalysis",
        ) -> "_1354.DynamicForceAnalysis":
            from mastapy.electric_machines.load_cases_and_analyses import _1354

            return self._parent._cast(_1354.DynamicForceAnalysis)

        @property
        def efficiency_map_analysis(
            self: "ElectricMachineAnalysis._Cast_ElectricMachineAnalysis",
        ) -> "_1357.EfficiencyMapAnalysis":
            from mastapy.electric_machines.load_cases_and_analyses import _1357

            return self._parent._cast(_1357.EfficiencyMapAnalysis)

        @property
        def electric_machine_fe_analysis(
            self: "ElectricMachineAnalysis._Cast_ElectricMachineAnalysis",
        ) -> "_1363.ElectricMachineFEAnalysis":
            from mastapy.electric_machines.load_cases_and_analyses import _1363

            return self._parent._cast(_1363.ElectricMachineFEAnalysis)

        @property
        def electric_machine_fe_mechanical_analysis(
            self: "ElectricMachineAnalysis._Cast_ElectricMachineAnalysis",
        ) -> "_1364.ElectricMachineFEMechanicalAnalysis":
            from mastapy.electric_machines.load_cases_and_analyses import _1364

            return self._parent._cast(_1364.ElectricMachineFEMechanicalAnalysis)

        @property
        def single_operating_point_analysis(
            self: "ElectricMachineAnalysis._Cast_ElectricMachineAnalysis",
        ) -> "_1377.SingleOperatingPointAnalysis":
            from mastapy.electric_machines.load_cases_and_analyses import _1377

            return self._parent._cast(_1377.SingleOperatingPointAnalysis)

        @property
        def speed_torque_curve_analysis(
            self: "ElectricMachineAnalysis._Cast_ElectricMachineAnalysis",
        ) -> "_1381.SpeedTorqueCurveAnalysis":
            from mastapy.electric_machines.load_cases_and_analyses import _1381

            return self._parent._cast(_1381.SpeedTorqueCurveAnalysis)

        @property
        def electric_machine_analysis(
            self: "ElectricMachineAnalysis._Cast_ElectricMachineAnalysis",
        ) -> "ElectricMachineAnalysis":
            return self._parent

        def __getattr__(
            self: "ElectricMachineAnalysis._Cast_ElectricMachineAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisTime

        if temp is None:
            return 0.0

        return temp

    @property
    def magnet_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MagnetTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def windings_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindingsTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def electric_machine_detail(self: Self) -> "_1268.ElectricMachineDetail":
        """mastapy.electric_machines.ElectricMachineDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_case(self: Self) -> "_1366.ElectricMachineLoadCaseBase":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def setup(self: Self) -> "_1273.ElectricMachineSetup":
        """mastapy.electric_machines.ElectricMachineSetup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Setup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_ready(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsReady

        if temp is None:
            return False

        return temp

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

    def perform_analysis(self: Self):
        """Method does not return."""
        self.wrapped.PerformAnalysis()

    @enforce_parameter_types
    def perform_analysis_with_progress(self: Self, token: "_7567.TaskProgress"):
        """Method does not return.

        Args:
            token (mastapy.TaskProgress)
        """
        self.wrapped.PerformAnalysisWithProgress(token.wrapped if token else None)

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
    def cast_to(self: Self) -> "ElectricMachineAnalysis._Cast_ElectricMachineAnalysis":
        return self._Cast_ElectricMachineAnalysis(self)
