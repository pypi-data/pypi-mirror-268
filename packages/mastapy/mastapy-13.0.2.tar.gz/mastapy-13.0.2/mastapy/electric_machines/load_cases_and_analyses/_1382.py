"""SpeedTorqueCurveLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.electric_machines.load_cases_and_analyses import _1374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPEED_TORQUE_CURVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "SpeedTorqueCurveLoadCase"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1273
    from mastapy.electric_machines.load_cases_and_analyses import _1381, _1366


__docformat__ = "restructuredtext en"
__all__ = ("SpeedTorqueCurveLoadCase",)


Self = TypeVar("Self", bound="SpeedTorqueCurveLoadCase")


class SpeedTorqueCurveLoadCase(_1374.NonLinearDQModelMultipleOperatingPointsLoadCase):
    """SpeedTorqueCurveLoadCase

    This is a mastapy class.
    """

    TYPE = _SPEED_TORQUE_CURVE_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpeedTorqueCurveLoadCase")

    class _Cast_SpeedTorqueCurveLoadCase:
        """Special nested class for casting SpeedTorqueCurveLoadCase to subclasses."""

        def __init__(
            self: "SpeedTorqueCurveLoadCase._Cast_SpeedTorqueCurveLoadCase",
            parent: "SpeedTorqueCurveLoadCase",
        ):
            self._parent = parent

        @property
        def non_linear_dq_model_multiple_operating_points_load_case(
            self: "SpeedTorqueCurveLoadCase._Cast_SpeedTorqueCurveLoadCase",
        ) -> "_1374.NonLinearDQModelMultipleOperatingPointsLoadCase":
            return self._parent._cast(
                _1374.NonLinearDQModelMultipleOperatingPointsLoadCase
            )

        @property
        def electric_machine_load_case_base(
            self: "SpeedTorqueCurveLoadCase._Cast_SpeedTorqueCurveLoadCase",
        ) -> "_1366.ElectricMachineLoadCaseBase":
            from mastapy.electric_machines.load_cases_and_analyses import _1366

            return self._parent._cast(_1366.ElectricMachineLoadCaseBase)

        @property
        def speed_torque_curve_load_case(
            self: "SpeedTorqueCurveLoadCase._Cast_SpeedTorqueCurveLoadCase",
        ) -> "SpeedTorqueCurveLoadCase":
            return self._parent

        def __getattr__(
            self: "SpeedTorqueCurveLoadCase._Cast_SpeedTorqueCurveLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpeedTorqueCurveLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def number_of_speed_values(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSpeedValues

        if temp is None:
            return 0

        return temp

    @number_of_speed_values.setter
    @enforce_parameter_types
    def number_of_speed_values(self: Self, value: "int"):
        self.wrapped.NumberOfSpeedValues = int(value) if value is not None else 0

    @enforce_parameter_types
    def analysis_for(
        self: Self, setup: "_1273.ElectricMachineSetup"
    ) -> "_1381.SpeedTorqueCurveAnalysis":
        """mastapy.electric_machines.load_cases_and_analyses.SpeedTorqueCurveAnalysis

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
    def cast_to(
        self: Self,
    ) -> "SpeedTorqueCurveLoadCase._Cast_SpeedTorqueCurveLoadCase":
        return self._Cast_SpeedTorqueCurveLoadCase(self)
