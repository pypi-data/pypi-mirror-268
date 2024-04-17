"""DynamicForceLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.electric_machines.load_cases_and_analyses import _1379, _1353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "DynamicForceLoadCase"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import (
        _1361,
        _1376,
        _1380,
        _1360,
        _1356,
        _1366,
    )


__docformat__ = "restructuredtext en"
__all__ = ("DynamicForceLoadCase",)


Self = TypeVar("Self", bound="DynamicForceLoadCase")


class DynamicForceLoadCase(_1353.BasicDynamicForceLoadCase):
    """DynamicForceLoadCase

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicForceLoadCase")

    class _Cast_DynamicForceLoadCase:
        """Special nested class for casting DynamicForceLoadCase to subclasses."""

        def __init__(
            self: "DynamicForceLoadCase._Cast_DynamicForceLoadCase",
            parent: "DynamicForceLoadCase",
        ):
            self._parent = parent

        @property
        def basic_dynamic_force_load_case(
            self: "DynamicForceLoadCase._Cast_DynamicForceLoadCase",
        ) -> "_1353.BasicDynamicForceLoadCase":
            return self._parent._cast(_1353.BasicDynamicForceLoadCase)

        @property
        def electric_machine_load_case_base(
            self: "DynamicForceLoadCase._Cast_DynamicForceLoadCase",
        ) -> "_1366.ElectricMachineLoadCaseBase":
            from mastapy.electric_machines.load_cases_and_analyses import _1366

            return self._parent._cast(_1366.ElectricMachineLoadCaseBase)

        @property
        def dynamic_force_load_case(
            self: "DynamicForceLoadCase._Cast_DynamicForceLoadCase",
        ) -> "DynamicForceLoadCase":
            return self._parent

        def __getattr__(
            self: "DynamicForceLoadCase._Cast_DynamicForceLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicForceLoadCase.TYPE"):
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
    def load_specification(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_SpecifyTorqueOrCurrent":
        """EnumWithSelectedValue[mastapy.electric_machines.load_cases_and_analyses.SpecifyTorqueOrCurrent]"""
        temp = self.wrapped.LoadSpecification

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_SpecifyTorqueOrCurrent.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @load_specification.setter
    @enforce_parameter_types
    def load_specification(self: Self, value: "_1379.SpecifyTorqueOrCurrent"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_SpecifyTorqueOrCurrent.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LoadSpecification = value

    @property
    def maximum_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumSpeed

        if temp is None:
            return 0.0

        return temp

    @maximum_speed.setter
    @enforce_parameter_types
    def maximum_speed(self: Self, value: "float"):
        self.wrapped.MaximumSpeed = float(value) if value is not None else 0.0

    @property
    def minimum_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumSpeed

        if temp is None:
            return 0.0

        return temp

    @minimum_speed.setter
    @enforce_parameter_types
    def minimum_speed(self: Self, value: "float"):
        self.wrapped.MinimumSpeed = float(value) if value is not None else 0.0

    @property
    def number_of_operating_points(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfOperatingPoints

        if temp is None:
            return 0

        return temp

    @number_of_operating_points.setter
    @enforce_parameter_types
    def number_of_operating_points(self: Self, value: "int"):
        self.wrapped.NumberOfOperatingPoints = int(value) if value is not None else 0

    @property
    def operating_points_specification_method(
        self: Self,
    ) -> "_1376.OperatingPointsSpecificationMethod":
        """mastapy.electric_machines.load_cases_and_analyses.OperatingPointsSpecificationMethod"""
        temp = self.wrapped.OperatingPointsSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.OperatingPointsSpecificationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines.load_cases_and_analyses._1376",
            "OperatingPointsSpecificationMethod",
        )(value)

    @operating_points_specification_method.setter
    @enforce_parameter_types
    def operating_points_specification_method(
        self: Self, value: "_1376.OperatingPointsSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.OperatingPointsSpecificationMethod",
        )
        self.wrapped.OperatingPointsSpecificationMethod = value

    @property
    def speed_points_distribution(self: Self) -> "_1380.SpeedPointsDistribution":
        """mastapy.electric_machines.load_cases_and_analyses.SpeedPointsDistribution"""
        temp = self.wrapped.SpeedPointsDistribution

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.SpeedPointsDistribution",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines.load_cases_and_analyses._1380",
            "SpeedPointsDistribution",
        )(value)

    @speed_points_distribution.setter
    @enforce_parameter_types
    def speed_points_distribution(self: Self, value: "_1380.SpeedPointsDistribution"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.SpeedPointsDistribution",
        )
        self.wrapped.SpeedPointsDistribution = value

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

    @enforce_parameter_types
    def add_operating_point(
        self: Self, torque: "float", speed: "float"
    ) -> "_1356.DynamicForcesOperatingPoint":
        """mastapy.electric_machines.load_cases_and_analyses.DynamicForcesOperatingPoint

        Args:
            torque (float)
            speed (float)
        """
        torque = float(torque)
        speed = float(speed)
        method_result = self.wrapped.AddOperatingPoint(
            torque if torque else 0.0, speed if speed else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_speeds(self: Self, values: "List[float]"):
        """Method does not return.

        Args:
            values (List[float])
        """
        values = conversion.mp_to_pn_list_float(values)
        self.wrapped.SetSpeeds(values)

    @enforce_parameter_types
    def set_speeds_in_si_units(self: Self, values: "List[float]"):
        """Method does not return.

        Args:
            values (List[float])
        """
        values = conversion.mp_to_pn_list_float(values)
        self.wrapped.SetSpeedsInSIUnits(values)

    @property
    def cast_to(self: Self) -> "DynamicForceLoadCase._Cast_DynamicForceLoadCase":
        return self._Cast_DynamicForceLoadCase(self)
