"""ElectricMachineResultsForPhase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_FOR_PHASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "ElectricMachineResultsForPhase"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import _1370


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineResultsForPhase",)


Self = TypeVar("Self", bound="ElectricMachineResultsForPhase")


class ElectricMachineResultsForPhase(_0.APIBase):
    """ElectricMachineResultsForPhase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_FOR_PHASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineResultsForPhase")

    class _Cast_ElectricMachineResultsForPhase:
        """Special nested class for casting ElectricMachineResultsForPhase to subclasses."""

        def __init__(
            self: "ElectricMachineResultsForPhase._Cast_ElectricMachineResultsForPhase",
            parent: "ElectricMachineResultsForPhase",
        ):
            self._parent = parent

        @property
        def electric_machine_results_for_phase(
            self: "ElectricMachineResultsForPhase._Cast_ElectricMachineResultsForPhase",
        ) -> "ElectricMachineResultsForPhase":
            return self._parent

        def __getattr__(
            self: "ElectricMachineResultsForPhase._Cast_ElectricMachineResultsForPhase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineResultsForPhase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def phase(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Phase

        if temp is None:
            return 0

        return temp

    @property
    def phase_current_peak(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseCurrentPeak

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_current_rms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseCurrentRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_current_harmonic_distortion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseCurrentHarmonicDistortion

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_reactive_voltage_rms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseReactiveVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistive_voltage_peak(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseResistiveVoltagePeak

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistive_voltage_rms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseResistiveVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_terminal_voltage_peak(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseTerminalVoltagePeak

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_terminal_voltage_rms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseTerminalVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def power_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def power_factor_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFactorAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def power_factor_direction(self: Self) -> "_1370.LeadingOrLagging":
        """mastapy.electric_machines.load_cases_and_analyses.LeadingOrLagging

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFactorDirection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.LeadingOrLagging"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines.load_cases_and_analyses._1370",
            "LeadingOrLagging",
        )(value)

    @property
    def power_factor_with_harmonic_distortion_adjustment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFactorWithHarmonicDistortionAdjustment

        if temp is None:
            return 0.0

        return temp

    @property
    def terminal_voltage_harmonic_distortion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TerminalVoltageHarmonicDistortion

        if temp is None:
            return 0.0

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
    ) -> "ElectricMachineResultsForPhase._Cast_ElectricMachineResultsForPhase":
        return self._Cast_ElectricMachineResultsForPhase(self)
