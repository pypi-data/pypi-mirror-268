"""ElectricMachineResultsForOpenCircuitAndOnLoad"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_FOR_OPEN_CIRCUIT_AND_ON_LOAD = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results",
    "ElectricMachineResultsForOpenCircuitAndOnLoad",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.electric_machines.results import _1351, _1352


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineResultsForOpenCircuitAndOnLoad",)


Self = TypeVar("Self", bound="ElectricMachineResultsForOpenCircuitAndOnLoad")


class ElectricMachineResultsForOpenCircuitAndOnLoad(_0.APIBase):
    """ElectricMachineResultsForOpenCircuitAndOnLoad

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_FOR_OPEN_CIRCUIT_AND_ON_LOAD
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineResultsForOpenCircuitAndOnLoad"
    )

    class _Cast_ElectricMachineResultsForOpenCircuitAndOnLoad:
        """Special nested class for casting ElectricMachineResultsForOpenCircuitAndOnLoad to subclasses."""

        def __init__(
            self: "ElectricMachineResultsForOpenCircuitAndOnLoad._Cast_ElectricMachineResultsForOpenCircuitAndOnLoad",
            parent: "ElectricMachineResultsForOpenCircuitAndOnLoad",
        ):
            self._parent = parent

        @property
        def electric_machine_results_for_open_circuit_and_on_load(
            self: "ElectricMachineResultsForOpenCircuitAndOnLoad._Cast_ElectricMachineResultsForOpenCircuitAndOnLoad",
        ) -> "ElectricMachineResultsForOpenCircuitAndOnLoad":
            return self._parent

        def __getattr__(
            self: "ElectricMachineResultsForOpenCircuitAndOnLoad._Cast_ElectricMachineResultsForOpenCircuitAndOnLoad",
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
        self: Self,
        instance_to_wrap: "ElectricMachineResultsForOpenCircuitAndOnLoad.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apparent_d_axis_inductance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApparentDAxisInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def apparent_inductance_multiplied_by_current_d_axis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApparentInductanceMultipliedByCurrentDAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def apparent_inductance_multiplied_by_current_q_axis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApparentInductanceMultipliedByCurrentQAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def apparent_q_axis_inductance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApparentQAxisInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def average_alignment_torque_dq(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageAlignmentTorqueDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def average_reluctance_torque_dq(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageReluctanceTorqueDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def base_speed_dq(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseSpeedDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def current_angle_for_maximum_torque_dq(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentAngleForMaximumTorqueDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_armature_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisArmatureFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricalConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def line_line_inductance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LineLineInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def linear_dq_model_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearDQModelChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_angle_from_phasor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadAngleFromPhasor

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_speed_dq(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumSpeedDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_torque_achievable_dq(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTorqueAchievableDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def mechanical_time_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MechanicalTimeConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def permanent_magnet_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermanentMagnetFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_reactive_voltage_drms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseReactiveVoltageDRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_reactive_voltage_qrms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseReactiveVoltageQRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_terminal_voltage_from_phasor_rms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseTerminalVoltageFromPhasorRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phasor_diagram(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhasorDiagram

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def power_factor_angle_from_phasor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFactorAngleFromPhasor

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_armature_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisArmatureFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def steady_state_short_circuit_current(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateShortCircuitCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def on_load_results(self: Self) -> "_1351.OnLoadElectricMachineResults":
        """mastapy.electric_machines.results.OnLoadElectricMachineResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OnLoadResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def open_circuit_results(self: Self) -> "_1352.OpenCircuitElectricMachineResults":
        """mastapy.electric_machines.results.OpenCircuitElectricMachineResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OpenCircuitResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_on_load_results(self: Self) -> "List[_1351.OnLoadElectricMachineResults]":
        """List[mastapy.electric_machines.results.OnLoadElectricMachineResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllOnLoadResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_open_circuit_results(
        self: Self,
    ) -> "List[_1352.OpenCircuitElectricMachineResults]":
        """List[mastapy.electric_machines.results.OpenCircuitElectricMachineResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllOpenCircuitResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def on_load_results_for_slices(
        self: Self,
    ) -> "List[_1351.OnLoadElectricMachineResults]":
        """List[mastapy.electric_machines.results.OnLoadElectricMachineResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OnLoadResultsForSlices

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def open_circuit_results_for_slices(
        self: Self,
    ) -> "List[_1352.OpenCircuitElectricMachineResults]":
        """List[mastapy.electric_machines.results.OpenCircuitElectricMachineResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OpenCircuitResultsForSlices

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
    ) -> "ElectricMachineResultsForOpenCircuitAndOnLoad._Cast_ElectricMachineResultsForOpenCircuitAndOnLoad":
        return self._Cast_ElectricMachineResultsForOpenCircuitAndOnLoad(self)
