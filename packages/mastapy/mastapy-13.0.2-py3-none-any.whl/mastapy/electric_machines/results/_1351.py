"""OnLoadElectricMachineResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.results import _1333
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ON_LOAD_ELECTRIC_MACHINE_RESULTS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "OnLoadElectricMachineResults"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import _1373, _1370
    from mastapy.electric_machines import _1323


__docformat__ = "restructuredtext en"
__all__ = ("OnLoadElectricMachineResults",)


Self = TypeVar("Self", bound="OnLoadElectricMachineResults")


class OnLoadElectricMachineResults(_1333.ElectricMachineResults):
    """OnLoadElectricMachineResults

    This is a mastapy class.
    """

    TYPE = _ON_LOAD_ELECTRIC_MACHINE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OnLoadElectricMachineResults")

    class _Cast_OnLoadElectricMachineResults:
        """Special nested class for casting OnLoadElectricMachineResults to subclasses."""

        def __init__(
            self: "OnLoadElectricMachineResults._Cast_OnLoadElectricMachineResults",
            parent: "OnLoadElectricMachineResults",
        ):
            self._parent = parent

        @property
        def electric_machine_results(
            self: "OnLoadElectricMachineResults._Cast_OnLoadElectricMachineResults",
        ) -> "_1333.ElectricMachineResults":
            return self._parent._cast(_1333.ElectricMachineResults)

        @property
        def on_load_electric_machine_results(
            self: "OnLoadElectricMachineResults._Cast_OnLoadElectricMachineResults",
        ) -> "OnLoadElectricMachineResults":
            return self._parent

        def __getattr__(
            self: "OnLoadElectricMachineResults._Cast_OnLoadElectricMachineResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OnLoadElectricMachineResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_power_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AveragePowerFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def average_power_factor_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AveragePowerFactorAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def average_power_factor_with_harmonic_distortion_adjustment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AveragePowerFactorWithHarmonicDistortionAdjustment

        if temp is None:
            return 0.0

        return temp

    @property
    def average_torque_dq(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageTorqueDQ

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
    def efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Efficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_loading(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricalLoading

        if temp is None:
            return 0.0

        return temp

    @property
    def input_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputPower

        if temp is None:
            return 0.0

        return temp

    @property
    def line_resistance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LineResistance

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_terminal_voltage_peak(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LineToLineTerminalVoltagePeak

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_terminal_voltage_rms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LineToLineTerminalVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_terminal_voltage_total_harmonic_distortion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LineToLineTerminalVoltageTotalHarmonicDistortion

        if temp is None:
            return 0.0

        return temp

    @property
    def motor_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MotorConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def motoring_or_generating(self: Self) -> "_1373.MotoringOrGenerating":
        """mastapy.electric_machines.load_cases_and_analyses.MotoringOrGenerating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MotoringOrGenerating

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.MotoringOrGenerating",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines.load_cases_and_analyses._1373",
            "MotoringOrGenerating",
        )(value)

    @property
    def output_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OutputPower

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseResistance

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
    def phase_resistive_voltage_drms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseResistiveVoltageDRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistive_voltage_qrms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseResistiveVoltageQRMS

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
    def phase_terminal_voltage_total_harmonic_distortion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseTerminalVoltageTotalHarmonicDistortion

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
    def power_from_electromagnetic_analysis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFromElectromagneticAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def stall_current(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StallCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def stall_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StallTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ripple_percentage_mst(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueRipplePercentageMST

        if temp is None:
            return 0.0

        return temp

    @property
    def total_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_material_resistivity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindingMaterialResistivity

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_skin_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindingSkinDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def windings(self: Self) -> "_1323.Windings":
        """mastapy.electric_machines.Windings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Windings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "OnLoadElectricMachineResults._Cast_OnLoadElectricMachineResults":
        return self._Cast_OnLoadElectricMachineResults(self)
