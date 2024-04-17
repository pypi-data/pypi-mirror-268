"""BasicDynamicForceLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.nodal_analysis.elmer import _172
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.electric_machines.load_cases_and_analyses import _1366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BASIC_DYNAMIC_FORCE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "BasicDynamicForceLoadCase"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import (
        _1375,
        _1356,
        _1354,
        _1355,
    )
    from mastapy.electric_machines import _1273


__docformat__ = "restructuredtext en"
__all__ = ("BasicDynamicForceLoadCase",)


Self = TypeVar("Self", bound="BasicDynamicForceLoadCase")


class BasicDynamicForceLoadCase(_1366.ElectricMachineLoadCaseBase):
    """BasicDynamicForceLoadCase

    This is a mastapy class.
    """

    TYPE = _BASIC_DYNAMIC_FORCE_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BasicDynamicForceLoadCase")

    class _Cast_BasicDynamicForceLoadCase:
        """Special nested class for casting BasicDynamicForceLoadCase to subclasses."""

        def __init__(
            self: "BasicDynamicForceLoadCase._Cast_BasicDynamicForceLoadCase",
            parent: "BasicDynamicForceLoadCase",
        ):
            self._parent = parent

        @property
        def electric_machine_load_case_base(
            self: "BasicDynamicForceLoadCase._Cast_BasicDynamicForceLoadCase",
        ) -> "_1366.ElectricMachineLoadCaseBase":
            return self._parent._cast(_1366.ElectricMachineLoadCaseBase)

        @property
        def dynamic_force_load_case(
            self: "BasicDynamicForceLoadCase._Cast_BasicDynamicForceLoadCase",
        ) -> "_1355.DynamicForceLoadCase":
            from mastapy.electric_machines.load_cases_and_analyses import _1355

            return self._parent._cast(_1355.DynamicForceLoadCase)

        @property
        def basic_dynamic_force_load_case(
            self: "BasicDynamicForceLoadCase._Cast_BasicDynamicForceLoadCase",
        ) -> "BasicDynamicForceLoadCase":
            return self._parent

        def __getattr__(
            self: "BasicDynamicForceLoadCase._Cast_BasicDynamicForceLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BasicDynamicForceLoadCase.TYPE"):
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
    def number_of_steps_per_operating_point_specification_method(
        self: Self,
    ) -> "_1375.NumberOfStepsPerOperatingPointSpecificationMethod":
        """mastapy.electric_machines.load_cases_and_analyses.NumberOfStepsPerOperatingPointSpecificationMethod"""
        temp = self.wrapped.NumberOfStepsPerOperatingPointSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.NumberOfStepsPerOperatingPointSpecificationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines.load_cases_and_analyses._1375",
            "NumberOfStepsPerOperatingPointSpecificationMethod",
        )(value)

    @number_of_steps_per_operating_point_specification_method.setter
    @enforce_parameter_types
    def number_of_steps_per_operating_point_specification_method(
        self: Self, value: "_1375.NumberOfStepsPerOperatingPointSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.NumberOfStepsPerOperatingPointSpecificationMethod",
        )
        self.wrapped.NumberOfStepsPerOperatingPointSpecificationMethod = value

    @property
    def number_of_steps_for_the_analysis_period(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfStepsForTheAnalysisPeriod

        if temp is None:
            return 0

        return temp

    @number_of_steps_for_the_analysis_period.setter
    @enforce_parameter_types
    def number_of_steps_for_the_analysis_period(self: Self, value: "int"):
        self.wrapped.NumberOfStepsForTheAnalysisPeriod = (
            int(value) if value is not None else 0
        )

    @property
    def operating_points(self: Self) -> "List[_1356.DynamicForcesOperatingPoint]":
        """List[mastapy.electric_machines.load_cases_and_analyses.DynamicForcesOperatingPoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def add_operating_point(self: Self):
        """Method does not return."""
        self.wrapped.AddOperatingPoint()

    @enforce_parameter_types
    def add_operating_point_specified_by_peak_current_and_current_angle(
        self: Self, peak_current: "float", current_angle: "float", speed: "float"
    ) -> "_1356.DynamicForcesOperatingPoint":
        """mastapy.electric_machines.load_cases_and_analyses.DynamicForcesOperatingPoint

        Args:
            peak_current (float)
            current_angle (float)
            speed (float)
        """
        peak_current = float(peak_current)
        current_angle = float(current_angle)
        speed = float(speed)
        method_result = (
            self.wrapped.AddOperatingPointSpecifiedByPeakCurrentAndCurrentAngle(
                peak_current if peak_current else 0.0,
                current_angle if current_angle else 0.0,
                speed if speed else 0.0,
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def analysis_for(
        self: Self, setup: "_1273.ElectricMachineSetup"
    ) -> "_1354.DynamicForceAnalysis":
        """mastapy.electric_machines.load_cases_and_analyses.DynamicForceAnalysis

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
    def remove_operating_point(
        self: Self, operating_point: "_1356.DynamicForcesOperatingPoint"
    ):
        """Method does not return.

        Args:
            operating_point (mastapy.electric_machines.load_cases_and_analyses.DynamicForcesOperatingPoint)
        """
        self.wrapped.RemoveOperatingPoint(
            operating_point.wrapped if operating_point else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "BasicDynamicForceLoadCase._Cast_BasicDynamicForceLoadCase":
        return self._Cast_BasicDynamicForceLoadCase(self)
