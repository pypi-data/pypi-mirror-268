"""PIDControlSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PID_CONTROL_SETTINGS = python_net_import(
    "SMT.MastaAPI.MathUtility.Control", "PIDControlSettings"
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_data import _1572
    from mastapy.math_utility import _1530


__docformat__ = "restructuredtext en"
__all__ = ("PIDControlSettings",)


Self = TypeVar("Self", bound="PIDControlSettings")


class PIDControlSettings(_0.APIBase):
    """PIDControlSettings

    This is a mastapy class.
    """

    TYPE = _PID_CONTROL_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PIDControlSettings")

    class _Cast_PIDControlSettings:
        """Special nested class for casting PIDControlSettings to subclasses."""

        def __init__(
            self: "PIDControlSettings._Cast_PIDControlSettings",
            parent: "PIDControlSettings",
        ):
            self._parent = parent

        @property
        def pid_control_settings(
            self: "PIDControlSettings._Cast_PIDControlSettings",
        ) -> "PIDControlSettings":
            return self._parent

        def __getattr__(self: "PIDControlSettings._Cast_PIDControlSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PIDControlSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def control_start_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ControlStartTime

        if temp is None:
            return 0.0

        return temp

    @control_start_time.setter
    @enforce_parameter_types
    def control_start_time(self: Self, value: "float"):
        self.wrapped.ControlStartTime = float(value) if value is not None else 0.0

    @property
    def differential_gain(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DifferentialGain

        if temp is None:
            return 0.0

        return temp

    @differential_gain.setter
    @enforce_parameter_types
    def differential_gain(self: Self, value: "float"):
        self.wrapped.DifferentialGain = float(value) if value is not None else 0.0

    @property
    def differential_gain_vs_time_and_error(
        self: Self,
    ) -> "_1572.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.DifferentialGainVsTimeAndError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @differential_gain_vs_time_and_error.setter
    @enforce_parameter_types
    def differential_gain_vs_time_and_error(
        self: Self, value: "_1572.GriddedSurfaceAccessor"
    ):
        self.wrapped.DifferentialGainVsTimeAndError = value.wrapped

    @property
    def differential_time_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DifferentialTimeConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def integral_gain(self: Self) -> "float":
        """float"""
        temp = self.wrapped.IntegralGain

        if temp is None:
            return 0.0

        return temp

    @integral_gain.setter
    @enforce_parameter_types
    def integral_gain(self: Self, value: "float"):
        self.wrapped.IntegralGain = float(value) if value is not None else 0.0

    @property
    def integral_gain_vs_time_and_error(self: Self) -> "_1572.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.IntegralGainVsTimeAndError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @integral_gain_vs_time_and_error.setter
    @enforce_parameter_types
    def integral_gain_vs_time_and_error(
        self: Self, value: "_1572.GriddedSurfaceAccessor"
    ):
        self.wrapped.IntegralGainVsTimeAndError = value.wrapped

    @property
    def integral_time_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntegralTimeConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def max_change_in_manipulated_value_per_unit_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaxChangeInManipulatedValuePerUnitTime

        if temp is None:
            return 0.0

        return temp

    @max_change_in_manipulated_value_per_unit_time.setter
    @enforce_parameter_types
    def max_change_in_manipulated_value_per_unit_time(self: Self, value: "float"):
        self.wrapped.MaxChangeInManipulatedValuePerUnitTime = (
            float(value) if value is not None else 0.0
        )

    @property
    def max_manipulated_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaxManipulatedValue

        if temp is None:
            return 0.0

        return temp

    @max_manipulated_value.setter
    @enforce_parameter_types
    def max_manipulated_value(self: Self, value: "float"):
        self.wrapped.MaxManipulatedValue = float(value) if value is not None else 0.0

    @property
    def min_manipulated_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinManipulatedValue

        if temp is None:
            return 0.0

        return temp

    @min_manipulated_value.setter
    @enforce_parameter_types
    def min_manipulated_value(self: Self, value: "float"):
        self.wrapped.MinManipulatedValue = float(value) if value is not None else 0.0

    @property
    def pid_calculates_change_in_manipulated_value(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.PIDCalculatesChangeInManipulatedValue

        if temp is None:
            return False

        return temp

    @pid_calculates_change_in_manipulated_value.setter
    @enforce_parameter_types
    def pid_calculates_change_in_manipulated_value(self: Self, value: "bool"):
        self.wrapped.PIDCalculatesChangeInManipulatedValue = (
            bool(value) if value is not None else False
        )

    @property
    def proportional_gain(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProportionalGain

        if temp is None:
            return 0.0

        return temp

    @proportional_gain.setter
    @enforce_parameter_types
    def proportional_gain(self: Self, value: "float"):
        self.wrapped.ProportionalGain = float(value) if value is not None else 0.0

    @property
    def proportional_gain_vs_time_and_error(
        self: Self,
    ) -> "_1572.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.ProportionalGainVsTimeAndError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @proportional_gain_vs_time_and_error.setter
    @enforce_parameter_types
    def proportional_gain_vs_time_and_error(
        self: Self, value: "_1572.GriddedSurfaceAccessor"
    ):
        self.wrapped.ProportionalGainVsTimeAndError = value.wrapped

    @property
    def set_point_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SetPointValue

        if temp is None:
            return 0.0

        return temp

    @set_point_value.setter
    @enforce_parameter_types
    def set_point_value(self: Self, value: "float"):
        self.wrapped.SetPointValue = float(value) if value is not None else 0.0

    @property
    def update_frequency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UpdateFrequency

        if temp is None:
            return 0.0

        return temp

    @update_frequency.setter
    @enforce_parameter_types
    def update_frequency(self: Self, value: "float"):
        self.wrapped.UpdateFrequency = float(value) if value is not None else 0.0

    @property
    def update_method(self: Self) -> "_1530.PIDControlUpdateMethod":
        """mastapy.math_utility.PIDControlUpdateMethod"""
        temp = self.wrapped.UpdateMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.PIDControlUpdateMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1530", "PIDControlUpdateMethod"
        )(value)

    @update_method.setter
    @enforce_parameter_types
    def update_method(self: Self, value: "_1530.PIDControlUpdateMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.PIDControlUpdateMethod"
        )
        self.wrapped.UpdateMethod = value

    @property
    def update_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UpdateTime

        if temp is None:
            return 0.0

        return temp

    @update_time.setter
    @enforce_parameter_types
    def update_time(self: Self, value: "float"):
        self.wrapped.UpdateTime = float(value) if value is not None else 0.0

    @property
    def use_differential_gain_scheduling(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDifferentialGainScheduling

        if temp is None:
            return False

        return temp

    @use_differential_gain_scheduling.setter
    @enforce_parameter_types
    def use_differential_gain_scheduling(self: Self, value: "bool"):
        self.wrapped.UseDifferentialGainScheduling = (
            bool(value) if value is not None else False
        )

    @property
    def use_integral_gain_scheduling(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseIntegralGainScheduling

        if temp is None:
            return False

        return temp

    @use_integral_gain_scheduling.setter
    @enforce_parameter_types
    def use_integral_gain_scheduling(self: Self, value: "bool"):
        self.wrapped.UseIntegralGainScheduling = (
            bool(value) if value is not None else False
        )

    @property
    def use_integrator_anti_windup(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseIntegratorAntiWindup

        if temp is None:
            return False

        return temp

    @use_integrator_anti_windup.setter
    @enforce_parameter_types
    def use_integrator_anti_windup(self: Self, value: "bool"):
        self.wrapped.UseIntegratorAntiWindup = (
            bool(value) if value is not None else False
        )

    @property
    def use_proportional_gain_scheduling(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseProportionalGainScheduling

        if temp is None:
            return False

        return temp

    @use_proportional_gain_scheduling.setter
    @enforce_parameter_types
    def use_proportional_gain_scheduling(self: Self, value: "bool"):
        self.wrapped.UseProportionalGainScheduling = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: Self) -> "PIDControlSettings._Cast_PIDControlSettings":
        return self._Cast_PIDControlSettings(self)
