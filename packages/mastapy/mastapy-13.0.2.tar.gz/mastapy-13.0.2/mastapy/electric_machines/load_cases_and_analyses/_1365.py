"""ElectricMachineLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.nodal_analysis.elmer import _172
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.electric_machines.load_cases_and_analyses import _1366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "ElectricMachineLoadCase"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import _1369, _1363, _1383
    from mastapy.electric_machines import _1273


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineLoadCase",)


Self = TypeVar("Self", bound="ElectricMachineLoadCase")


class ElectricMachineLoadCase(_1366.ElectricMachineLoadCaseBase):
    """ElectricMachineLoadCase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineLoadCase")

    class _Cast_ElectricMachineLoadCase:
        """Special nested class for casting ElectricMachineLoadCase to subclasses."""

        def __init__(
            self: "ElectricMachineLoadCase._Cast_ElectricMachineLoadCase",
            parent: "ElectricMachineLoadCase",
        ):
            self._parent = parent

        @property
        def electric_machine_load_case_base(
            self: "ElectricMachineLoadCase._Cast_ElectricMachineLoadCase",
        ) -> "_1366.ElectricMachineLoadCaseBase":
            return self._parent._cast(_1366.ElectricMachineLoadCaseBase)

        @property
        def speed_torque_load_case(
            self: "ElectricMachineLoadCase._Cast_ElectricMachineLoadCase",
        ) -> "_1383.SpeedTorqueLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1383

            return self._parent._cast(_1383.SpeedTorqueLoadCase)

        @property
        def electric_machine_load_case(
            self: "ElectricMachineLoadCase._Cast_ElectricMachineLoadCase",
        ) -> "ElectricMachineLoadCase":
            return self._parent

        def __getattr__(
            self: "ElectricMachineLoadCase._Cast_ElectricMachineLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_period(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod":
        """EnumWithSelectedValue[mastapy.nodal_analysis.elmer.ElectricMachineAnalysisPeriod]"""
        temp = self.wrapped.AnalysisPeriod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @analysis_period.setter
    @enforce_parameter_types
    def analysis_period(self: Self, value: "_172.ElectricMachineAnalysisPeriod"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.AnalysisPeriod = value

    @property
    def core_loss_minor_loop_hysteresis_loss_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoreLossMinorLoopHysteresisLossFactor

        if temp is None:
            return 0.0

        return temp

    @core_loss_minor_loop_hysteresis_loss_factor.setter
    @enforce_parameter_types
    def core_loss_minor_loop_hysteresis_loss_factor(self: Self, value: "float"):
        self.wrapped.CoreLossMinorLoopHysteresisLossFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def current_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CurrentAngle

        if temp is None:
            return 0.0

        return temp

    @current_angle.setter
    @enforce_parameter_types
    def current_angle(self: Self, value: "float"):
        self.wrapped.CurrentAngle = float(value) if value is not None else 0.0

    @property
    def end_winding_inductance_method(self: Self) -> "_1369.EndWindingInductanceMethod":
        """mastapy.electric_machines.load_cases_and_analyses.EndWindingInductanceMethod"""
        temp = self.wrapped.EndWindingInductanceMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.EndWindingInductanceMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines.load_cases_and_analyses._1369",
            "EndWindingInductanceMethod",
        )(value)

    @end_winding_inductance_method.setter
    @enforce_parameter_types
    def end_winding_inductance_method(
        self: Self, value: "_1369.EndWindingInductanceMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.EndWindingInductanceMethod",
        )
        self.wrapped.EndWindingInductanceMethod = value

    @property
    def include_iron_and_eddy_current_losses(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeIronAndEddyCurrentLosses

        if temp is None:
            return False

        return temp

    @include_iron_and_eddy_current_losses.setter
    @enforce_parameter_types
    def include_iron_and_eddy_current_losses(self: Self, value: "bool"):
        self.wrapped.IncludeIronAndEddyCurrentLosses = (
            bool(value) if value is not None else False
        )

    @property
    def include_open_circuit_calculation(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeOpenCircuitCalculation

        if temp is None:
            return False

        return temp

    @include_open_circuit_calculation.setter
    @enforce_parameter_types
    def include_open_circuit_calculation(self: Self, value: "bool"):
        self.wrapped.IncludeOpenCircuitCalculation = (
            bool(value) if value is not None else False
        )

    @property
    def include_winding_ac_losses(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeWindingACLosses

        if temp is None:
            return False

        return temp

    @include_winding_ac_losses.setter
    @enforce_parameter_types
    def include_winding_ac_losses(self: Self, value: "bool"):
        self.wrapped.IncludeWindingACLosses = (
            bool(value) if value is not None else False
        )

    @property
    def minimum_number_of_steps_for_voltages_and_losses_calculation(
        self: Self,
    ) -> "int":
        """int"""
        temp = self.wrapped.MinimumNumberOfStepsForVoltagesAndLossesCalculation

        if temp is None:
            return 0

        return temp

    @minimum_number_of_steps_for_voltages_and_losses_calculation.setter
    @enforce_parameter_types
    def minimum_number_of_steps_for_voltages_and_losses_calculation(
        self: Self, value: "int"
    ):
        self.wrapped.MinimumNumberOfStepsForVoltagesAndLossesCalculation = (
            int(value) if value is not None else 0
        )

    @property
    def non_linear_relaxation_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NonLinearRelaxationFactor

        if temp is None:
            return 0.0

        return temp

    @non_linear_relaxation_factor.setter
    @enforce_parameter_types
    def non_linear_relaxation_factor(self: Self, value: "float"):
        self.wrapped.NonLinearRelaxationFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def non_linear_system_convergence_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NonLinearSystemConvergenceTolerance

        if temp is None:
            return 0.0

        return temp

    @non_linear_system_convergence_tolerance.setter
    @enforce_parameter_types
    def non_linear_system_convergence_tolerance(self: Self, value: "float"):
        self.wrapped.NonLinearSystemConvergenceTolerance = (
            float(value) if value is not None else 0.0
        )

    @property
    def non_linear_system_maximum_number_of_iterations(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NonLinearSystemMaximumNumberOfIterations

        if temp is None:
            return 0

        return temp

    @non_linear_system_maximum_number_of_iterations.setter
    @enforce_parameter_types
    def non_linear_system_maximum_number_of_iterations(self: Self, value: "int"):
        self.wrapped.NonLinearSystemMaximumNumberOfIterations = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_cycles(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfCycles

        if temp is None:
            return 0

        return temp

    @number_of_cycles.setter
    @enforce_parameter_types
    def number_of_cycles(self: Self, value: "int"):
        self.wrapped.NumberOfCycles = int(value) if value is not None else 0

    @property
    def number_of_initial_transient_steps(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfInitialTransientSteps

        if temp is None:
            return 0

        return temp

    @number_of_initial_transient_steps.setter
    @enforce_parameter_types
    def number_of_initial_transient_steps(self: Self, value: "int"):
        self.wrapped.NumberOfInitialTransientSteps = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_steps_per_analysis_period(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfStepsPerAnalysisPeriod

        if temp is None:
            return 0

        return temp

    @number_of_steps_per_analysis_period.setter
    @enforce_parameter_types
    def number_of_steps_per_analysis_period(self: Self, value: "int"):
        self.wrapped.NumberOfStepsPerAnalysisPeriod = (
            int(value) if value is not None else 0
        )

    @property
    def override_design_end_winding_inductance_method(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDesignEndWindingInductanceMethod

        if temp is None:
            return False

        return temp

    @override_design_end_winding_inductance_method.setter
    @enforce_parameter_types
    def override_design_end_winding_inductance_method(self: Self, value: "bool"):
        self.wrapped.OverrideDesignEndWindingInductanceMethod = (
            bool(value) if value is not None else False
        )

    @property
    def peak_line_current(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PeakLineCurrent

        if temp is None:
            return 0.0

        return temp

    @peak_line_current.setter
    @enforce_parameter_types
    def peak_line_current(self: Self, value: "float"):
        self.wrapped.PeakLineCurrent = float(value) if value is not None else 0.0

    @property
    def rms_line_current(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RMSLineCurrent

        if temp is None:
            return 0.0

        return temp

    @rms_line_current.setter
    @enforce_parameter_types
    def rms_line_current(self: Self, value: "float"):
        self.wrapped.RMSLineCurrent = float(value) if value is not None else 0.0

    @property
    def speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @speed.setter
    @enforce_parameter_types
    def speed(self: Self, value: "float"):
        self.wrapped.Speed = float(value) if value is not None else 0.0

    @property
    def total_number_of_time_steps(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalNumberOfTimeSteps

        if temp is None:
            return 0

        return temp

    @property
    def user_specified_end_winding_inductance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedEndWindingInductance

        if temp is None:
            return 0.0

        return temp

    @user_specified_end_winding_inductance.setter
    @enforce_parameter_types
    def user_specified_end_winding_inductance(self: Self, value: "float"):
        self.wrapped.UserSpecifiedEndWindingInductance = (
            float(value) if value is not None else 0.0
        )

    @enforce_parameter_types
    def analysis_for(
        self: Self, setup: "_1273.ElectricMachineSetup"
    ) -> "_1363.ElectricMachineFEAnalysis":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineFEAnalysis

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

    @property
    def cast_to(self: Self) -> "ElectricMachineLoadCase._Cast_ElectricMachineLoadCase":
        return self._Cast_ElectricMachineLoadCase(self)
