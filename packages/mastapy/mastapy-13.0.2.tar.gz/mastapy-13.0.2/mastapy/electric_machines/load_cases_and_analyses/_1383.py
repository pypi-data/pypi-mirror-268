"""SpeedTorqueLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1365
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPEED_TORQUE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "SpeedTorqueLoadCase"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import (
        _1361,
        _1379,
        _1360,
        _1366,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpeedTorqueLoadCase",)


Self = TypeVar("Self", bound="SpeedTorqueLoadCase")


class SpeedTorqueLoadCase(_1365.ElectricMachineLoadCase):
    """SpeedTorqueLoadCase

    This is a mastapy class.
    """

    TYPE = _SPEED_TORQUE_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpeedTorqueLoadCase")

    class _Cast_SpeedTorqueLoadCase:
        """Special nested class for casting SpeedTorqueLoadCase to subclasses."""

        def __init__(
            self: "SpeedTorqueLoadCase._Cast_SpeedTorqueLoadCase",
            parent: "SpeedTorqueLoadCase",
        ):
            self._parent = parent

        @property
        def electric_machine_load_case(
            self: "SpeedTorqueLoadCase._Cast_SpeedTorqueLoadCase",
        ) -> "_1365.ElectricMachineLoadCase":
            return self._parent._cast(_1365.ElectricMachineLoadCase)

        @property
        def electric_machine_load_case_base(
            self: "SpeedTorqueLoadCase._Cast_SpeedTorqueLoadCase",
        ) -> "_1366.ElectricMachineLoadCaseBase":
            from mastapy.electric_machines.load_cases_and_analyses import _1366

            return self._parent._cast(_1366.ElectricMachineLoadCaseBase)

        @property
        def speed_torque_load_case(
            self: "SpeedTorqueLoadCase._Cast_SpeedTorqueLoadCase",
        ) -> "SpeedTorqueLoadCase":
            return self._parent

        def __getattr__(
            self: "SpeedTorqueLoadCase._Cast_SpeedTorqueLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpeedTorqueLoadCase.TYPE"):
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
    def load_specification(self: Self) -> "_1379.SpecifyTorqueOrCurrent":
        """mastapy.electric_machines.load_cases_and_analyses.SpecifyTorqueOrCurrent"""
        temp = self.wrapped.LoadSpecification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.SpecifyTorqueOrCurrent",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines.load_cases_and_analyses._1379",
            "SpecifyTorqueOrCurrent",
        )(value)

    @load_specification.setter
    @enforce_parameter_types
    def load_specification(self: Self, value: "_1379.SpecifyTorqueOrCurrent"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.SpecifyTorqueOrCurrent",
        )
        self.wrapped.LoadSpecification = value

    @property
    def target_torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TargetTorque

        if temp is None:
            return 0.0

        return temp

    @target_torque.setter
    @enforce_parameter_types
    def target_torque(self: Self, value: "float"):
        self.wrapped.TargetTorque = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "SpeedTorqueLoadCase._Cast_SpeedTorqueLoadCase":
        return self._Cast_SpeedTorqueLoadCase(self)
