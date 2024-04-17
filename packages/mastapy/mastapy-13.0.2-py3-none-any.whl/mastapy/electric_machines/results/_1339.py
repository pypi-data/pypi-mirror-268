"""ElectricMachineResultsForPhaseAtTimeStep"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_FOR_PHASE_AT_TIME_STEP = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "ElectricMachineResultsForPhaseAtTimeStep"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineResultsForPhaseAtTimeStep",)


Self = TypeVar("Self", bound="ElectricMachineResultsForPhaseAtTimeStep")


class ElectricMachineResultsForPhaseAtTimeStep(_0.APIBase):
    """ElectricMachineResultsForPhaseAtTimeStep

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_FOR_PHASE_AT_TIME_STEP
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineResultsForPhaseAtTimeStep"
    )

    class _Cast_ElectricMachineResultsForPhaseAtTimeStep:
        """Special nested class for casting ElectricMachineResultsForPhaseAtTimeStep to subclasses."""

        def __init__(
            self: "ElectricMachineResultsForPhaseAtTimeStep._Cast_ElectricMachineResultsForPhaseAtTimeStep",
            parent: "ElectricMachineResultsForPhaseAtTimeStep",
        ):
            self._parent = parent

        @property
        def electric_machine_results_for_phase_at_time_step(
            self: "ElectricMachineResultsForPhaseAtTimeStep._Cast_ElectricMachineResultsForPhaseAtTimeStep",
        ) -> "ElectricMachineResultsForPhaseAtTimeStep":
            return self._parent

        def __getattr__(
            self: "ElectricMachineResultsForPhaseAtTimeStep._Cast_ElectricMachineResultsForPhaseAtTimeStep",
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
        self: Self, instance_to_wrap: "ElectricMachineResultsForPhaseAtTimeStep.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Current

        if temp is None:
            return 0.0

        return temp

    @property
    def dc_winding_losses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DCWindingLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FluxLinkage

        if temp is None:
            return 0.0

        return temp

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
    def phase_terminal_voltage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseTerminalVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def reactive_voltage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReactiveVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def resistive_voltage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResistiveVoltage

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
    ) -> "ElectricMachineResultsForPhaseAtTimeStep._Cast_ElectricMachineResultsForPhaseAtTimeStep":
        return self._Cast_ElectricMachineResultsForPhaseAtTimeStep(self)
