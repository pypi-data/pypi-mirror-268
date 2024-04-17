"""NonLinearDQModelMultipleOperatingPointsLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_DQ_MODEL_MULTIPLE_OPERATING_POINTS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses",
    "NonLinearDQModelMultipleOperatingPointsLoadCase",
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import (
        _1361,
        _1360,
        _1358,
        _1382,
    )


__docformat__ = "restructuredtext en"
__all__ = ("NonLinearDQModelMultipleOperatingPointsLoadCase",)


Self = TypeVar("Self", bound="NonLinearDQModelMultipleOperatingPointsLoadCase")


class NonLinearDQModelMultipleOperatingPointsLoadCase(
    _1366.ElectricMachineLoadCaseBase
):
    """NonLinearDQModelMultipleOperatingPointsLoadCase

    This is a mastapy class.
    """

    TYPE = _NON_LINEAR_DQ_MODEL_MULTIPLE_OPERATING_POINTS_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_NonLinearDQModelMultipleOperatingPointsLoadCase"
    )

    class _Cast_NonLinearDQModelMultipleOperatingPointsLoadCase:
        """Special nested class for casting NonLinearDQModelMultipleOperatingPointsLoadCase to subclasses."""

        def __init__(
            self: "NonLinearDQModelMultipleOperatingPointsLoadCase._Cast_NonLinearDQModelMultipleOperatingPointsLoadCase",
            parent: "NonLinearDQModelMultipleOperatingPointsLoadCase",
        ):
            self._parent = parent

        @property
        def electric_machine_load_case_base(
            self: "NonLinearDQModelMultipleOperatingPointsLoadCase._Cast_NonLinearDQModelMultipleOperatingPointsLoadCase",
        ) -> "_1366.ElectricMachineLoadCaseBase":
            return self._parent._cast(_1366.ElectricMachineLoadCaseBase)

        @property
        def efficiency_map_load_case(
            self: "NonLinearDQModelMultipleOperatingPointsLoadCase._Cast_NonLinearDQModelMultipleOperatingPointsLoadCase",
        ) -> "_1358.EfficiencyMapLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1358

            return self._parent._cast(_1358.EfficiencyMapLoadCase)

        @property
        def speed_torque_curve_load_case(
            self: "NonLinearDQModelMultipleOperatingPointsLoadCase._Cast_NonLinearDQModelMultipleOperatingPointsLoadCase",
        ) -> "_1382.SpeedTorqueCurveLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1382

            return self._parent._cast(_1382.SpeedTorqueCurveLoadCase)

        @property
        def non_linear_dq_model_multiple_operating_points_load_case(
            self: "NonLinearDQModelMultipleOperatingPointsLoadCase._Cast_NonLinearDQModelMultipleOperatingPointsLoadCase",
        ) -> "NonLinearDQModelMultipleOperatingPointsLoadCase":
            return self._parent

        def __getattr__(
            self: "NonLinearDQModelMultipleOperatingPointsLoadCase._Cast_NonLinearDQModelMultipleOperatingPointsLoadCase",
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
        instance_to_wrap: "NonLinearDQModelMultipleOperatingPointsLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def control_strategy(self: Self) -> "_1361.ElectricMachineControlStrategy":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineControlStrategy"""
        temp = self.wrapped.ControlStrategy

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.ElectricMachineControlStrategy",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines.load_cases_and_analyses._1361",
            "ElectricMachineControlStrategy",
        )(value)

    @control_strategy.setter
    @enforce_parameter_types
    def control_strategy(self: Self, value: "_1361.ElectricMachineControlStrategy"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.ElectricMachineControlStrategy",
        )
        self.wrapped.ControlStrategy = value

    @property
    def include_resistive_voltages(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeResistiveVoltages

        if temp is None:
            return False

        return temp

    @include_resistive_voltages.setter
    @enforce_parameter_types
    def include_resistive_voltages(self: Self, value: "bool"):
        self.wrapped.IncludeResistiveVoltages = (
            bool(value) if value is not None else False
        )

    @property
    def basic_mechanical_loss_settings(
        self: Self,
    ) -> "_1360.ElectricMachineBasicMechanicalLossSettings":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineBasicMechanicalLossSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicMechanicalLossSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "NonLinearDQModelMultipleOperatingPointsLoadCase._Cast_NonLinearDQModelMultipleOperatingPointsLoadCase":
        return self._Cast_NonLinearDQModelMultipleOperatingPointsLoadCase(self)
