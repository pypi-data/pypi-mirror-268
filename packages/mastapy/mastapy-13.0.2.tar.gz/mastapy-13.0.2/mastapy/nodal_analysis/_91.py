"""TransientSolverOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.nodal_analysis import _71
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRANSIENT_SOLVER_OPTIONS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "TransientSolverOptions"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _56, _86, _93


__docformat__ = "restructuredtext en"
__all__ = ("TransientSolverOptions",)


Self = TypeVar("Self", bound="TransientSolverOptions")


class TransientSolverOptions(_0.APIBase):
    """TransientSolverOptions

    This is a mastapy class.
    """

    TYPE = _TRANSIENT_SOLVER_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TransientSolverOptions")

    class _Cast_TransientSolverOptions:
        """Special nested class for casting TransientSolverOptions to subclasses."""

        def __init__(
            self: "TransientSolverOptions._Cast_TransientSolverOptions",
            parent: "TransientSolverOptions",
        ):
            self._parent = parent

        @property
        def transient_solver_options(
            self: "TransientSolverOptions._Cast_TransientSolverOptions",
        ) -> "TransientSolverOptions":
            return self._parent

        def __getattr__(
            self: "TransientSolverOptions._Cast_TransientSolverOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TransientSolverOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_tolerance_angular_velocity_for_newton_raphson(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AbsoluteToleranceAngularVelocityForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @absolute_tolerance_angular_velocity_for_newton_raphson.setter
    @enforce_parameter_types
    def absolute_tolerance_angular_velocity_for_newton_raphson(
        self: Self, value: "float"
    ):
        self.wrapped.AbsoluteToleranceAngularVelocityForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def absolute_tolerance_angular_velocity_for_step(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AbsoluteToleranceAngularVelocityForStep

        if temp is None:
            return 0.0

        return temp

    @absolute_tolerance_angular_velocity_for_step.setter
    @enforce_parameter_types
    def absolute_tolerance_angular_velocity_for_step(self: Self, value: "float"):
        self.wrapped.AbsoluteToleranceAngularVelocityForStep = (
            float(value) if value is not None else 0.0
        )

    @property
    def absolute_tolerance_lagrange_force_for_newton_raphson(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AbsoluteToleranceLagrangeForceForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @absolute_tolerance_lagrange_force_for_newton_raphson.setter
    @enforce_parameter_types
    def absolute_tolerance_lagrange_force_for_newton_raphson(
        self: Self, value: "float"
    ):
        self.wrapped.AbsoluteToleranceLagrangeForceForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def absolute_tolerance_lagrange_moment_for_newton_raphson(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AbsoluteToleranceLagrangeMomentForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @absolute_tolerance_lagrange_moment_for_newton_raphson.setter
    @enforce_parameter_types
    def absolute_tolerance_lagrange_moment_for_newton_raphson(
        self: Self, value: "float"
    ):
        self.wrapped.AbsoluteToleranceLagrangeMomentForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def absolute_tolerance_simple(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AbsoluteToleranceSimple

        if temp is None:
            return 0.0

        return temp

    @absolute_tolerance_simple.setter
    @enforce_parameter_types
    def absolute_tolerance_simple(self: Self, value: "float"):
        self.wrapped.AbsoluteToleranceSimple = (
            float(value) if value is not None else 0.0
        )

    @property
    def absolute_tolerance_temperature_for_newton_raphson(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AbsoluteToleranceTemperatureForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @absolute_tolerance_temperature_for_newton_raphson.setter
    @enforce_parameter_types
    def absolute_tolerance_temperature_for_newton_raphson(self: Self, value: "float"):
        self.wrapped.AbsoluteToleranceTemperatureForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def absolute_tolerance_temperature_for_step(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AbsoluteToleranceTemperatureForStep

        if temp is None:
            return 0.0

        return temp

    @absolute_tolerance_temperature_for_step.setter
    @enforce_parameter_types
    def absolute_tolerance_temperature_for_step(self: Self, value: "float"):
        self.wrapped.AbsoluteToleranceTemperatureForStep = (
            float(value) if value is not None else 0.0
        )

    @property
    def absolute_tolerance_translational_velocity_for_newton_raphson(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.AbsoluteToleranceTranslationalVelocityForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @absolute_tolerance_translational_velocity_for_newton_raphson.setter
    @enforce_parameter_types
    def absolute_tolerance_translational_velocity_for_newton_raphson(
        self: Self, value: "float"
    ):
        self.wrapped.AbsoluteToleranceTranslationalVelocityForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def absolute_tolerance_translational_velocity_for_step(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AbsoluteToleranceTranslationalVelocityForStep

        if temp is None:
            return 0.0

        return temp

    @absolute_tolerance_translational_velocity_for_step.setter
    @enforce_parameter_types
    def absolute_tolerance_translational_velocity_for_step(self: Self, value: "float"):
        self.wrapped.AbsoluteToleranceTranslationalVelocityForStep = (
            float(value) if value is not None else 0.0
        )

    @property
    def damping_scaling_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DampingScalingFactor

        if temp is None:
            return 0.0

        return temp

    @damping_scaling_factor.setter
    @enforce_parameter_types
    def damping_scaling_factor(self: Self, value: "float"):
        self.wrapped.DampingScalingFactor = float(value) if value is not None else 0.0

    @property
    def damping_scaling_for_initial_transients(
        self: Self,
    ) -> "_56.DampingScalingTypeForInitialTransients":
        """mastapy.nodal_analysis.DampingScalingTypeForInitialTransients"""
        temp = self.wrapped.DampingScalingForInitialTransients

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.DampingScalingTypeForInitialTransients"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._56", "DampingScalingTypeForInitialTransients"
        )(value)

    @damping_scaling_for_initial_transients.setter
    @enforce_parameter_types
    def damping_scaling_for_initial_transients(
        self: Self, value: "_56.DampingScalingTypeForInitialTransients"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.DampingScalingTypeForInitialTransients"
        )
        self.wrapped.DampingScalingForInitialTransients = value

    @property
    def end_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndTime

        if temp is None:
            return 0.0

        return temp

    @end_time.setter
    @enforce_parameter_types
    def end_time(self: Self, value: "float"):
        self.wrapped.EndTime = float(value) if value is not None else 0.0

    @property
    def integration_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_IntegrationMethod":
        """EnumWithSelectedValue[mastapy.nodal_analysis.IntegrationMethod]"""
        temp = self.wrapped.IntegrationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_IntegrationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @integration_method.setter
    @enforce_parameter_types
    def integration_method(self: Self, value: "_71.IntegrationMethod"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_IntegrationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.IntegrationMethod = value

    @property
    def limit_time_step_for_final_results(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LimitTimeStepForFinalResults

        if temp is None:
            return False

        return temp

    @limit_time_step_for_final_results.setter
    @enforce_parameter_types
    def limit_time_step_for_final_results(self: Self, value: "bool"):
        self.wrapped.LimitTimeStepForFinalResults = (
            bool(value) if value is not None else False
        )

    @property
    def log_initial_transients(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LogInitialTransients

        if temp is None:
            return False

        return temp

    @log_initial_transients.setter
    @enforce_parameter_types
    def log_initial_transients(self: Self, value: "bool"):
        self.wrapped.LogInitialTransients = bool(value) if value is not None else False

    @property
    def maximum_number_of_time_steps(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfTimeSteps

        if temp is None:
            return 0

        return temp

    @maximum_number_of_time_steps.setter
    @enforce_parameter_types
    def maximum_number_of_time_steps(self: Self, value: "int"):
        self.wrapped.MaximumNumberOfTimeSteps = int(value) if value is not None else 0

    @property
    def maximum_time_step(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumTimeStep

        if temp is None:
            return 0.0

        return temp

    @maximum_time_step.setter
    @enforce_parameter_types
    def maximum_time_step(self: Self, value: "float"):
        self.wrapped.MaximumTimeStep = float(value) if value is not None else 0.0

    @property
    def maximum_time_step_for_final_results(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumTimeStepForFinalResults

        if temp is None:
            return 0.0

        return temp

    @maximum_time_step_for_final_results.setter
    @enforce_parameter_types
    def maximum_time_step_for_final_results(self: Self, value: "float"):
        self.wrapped.MaximumTimeStepForFinalResults = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_step_between_results(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumStepBetweenResults

        if temp is None:
            return 0.0

        return temp

    @minimum_step_between_results.setter
    @enforce_parameter_types
    def minimum_step_between_results(self: Self, value: "float"):
        self.wrapped.MinimumStepBetweenResults = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_time_step(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumTimeStep

        if temp is None:
            return 0.0

        return temp

    @minimum_time_step.setter
    @enforce_parameter_types
    def minimum_time_step(self: Self, value: "float"):
        self.wrapped.MinimumTimeStep = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_alpha(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RayleighDampingAlpha

        if temp is None:
            return 0.0

        return temp

    @rayleigh_damping_alpha.setter
    @enforce_parameter_types
    def rayleigh_damping_alpha(self: Self, value: "float"):
        self.wrapped.RayleighDampingAlpha = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_beta(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return temp

    @rayleigh_damping_beta.setter
    @enforce_parameter_types
    def rayleigh_damping_beta(self: Self, value: "float"):
        self.wrapped.RayleighDampingBeta = float(value) if value is not None else 0.0

    @property
    def relative_tolerance_simple(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RelativeToleranceSimple

        if temp is None:
            return 0.0

        return temp

    @relative_tolerance_simple.setter
    @enforce_parameter_types
    def relative_tolerance_simple(self: Self, value: "float"):
        self.wrapped.RelativeToleranceSimple = (
            float(value) if value is not None else 0.0
        )

    @property
    def relative_tolerance_for_newton_raphson(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RelativeToleranceForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @relative_tolerance_for_newton_raphson.setter
    @enforce_parameter_types
    def relative_tolerance_for_newton_raphson(self: Self, value: "float"):
        self.wrapped.RelativeToleranceForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def relative_tolerance_for_step(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RelativeToleranceForStep

        if temp is None:
            return 0.0

        return temp

    @relative_tolerance_for_step.setter
    @enforce_parameter_types
    def relative_tolerance_for_step(self: Self, value: "float"):
        self.wrapped.RelativeToleranceForStep = (
            float(value) if value is not None else 0.0
        )

    @property
    def residual_force_tolerance_for_newton_raphson(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResidualForceToleranceForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @residual_force_tolerance_for_newton_raphson.setter
    @enforce_parameter_types
    def residual_force_tolerance_for_newton_raphson(self: Self, value: "float"):
        self.wrapped.ResidualForceToleranceForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def residual_lagrange_angular_tolerance_for_newton_raphson(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResidualLagrangeAngularToleranceForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @residual_lagrange_angular_tolerance_for_newton_raphson.setter
    @enforce_parameter_types
    def residual_lagrange_angular_tolerance_for_newton_raphson(
        self: Self, value: "float"
    ):
        self.wrapped.ResidualLagrangeAngularToleranceForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def residual_lagrange_translational_tolerance_for_newton_raphson(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.ResidualLagrangeTranslationalToleranceForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @residual_lagrange_translational_tolerance_for_newton_raphson.setter
    @enforce_parameter_types
    def residual_lagrange_translational_tolerance_for_newton_raphson(
        self: Self, value: "float"
    ):
        self.wrapped.ResidualLagrangeTranslationalToleranceForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def residual_moment_tolerance_for_newton_raphson(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResidualMomentToleranceForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @residual_moment_tolerance_for_newton_raphson.setter
    @enforce_parameter_types
    def residual_moment_tolerance_for_newton_raphson(self: Self, value: "float"):
        self.wrapped.ResidualMomentToleranceForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def residual_relative_tolerance_for_newton_raphson(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResidualRelativeToleranceForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @residual_relative_tolerance_for_newton_raphson.setter
    @enforce_parameter_types
    def residual_relative_tolerance_for_newton_raphson(self: Self, value: "float"):
        self.wrapped.ResidualRelativeToleranceForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def residual_temperature_tolerance_for_newton_raphson(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResidualTemperatureToleranceForNewtonRaphson

        if temp is None:
            return 0.0

        return temp

    @residual_temperature_tolerance_for_newton_raphson.setter
    @enforce_parameter_types
    def residual_temperature_tolerance_for_newton_raphson(self: Self, value: "float"):
        self.wrapped.ResidualTemperatureToleranceForNewtonRaphson = (
            float(value) if value is not None else 0.0
        )

    @property
    def result_logging_frequency(self: Self) -> "_86.ResultLoggingFrequency":
        """mastapy.nodal_analysis.ResultLoggingFrequency"""
        temp = self.wrapped.ResultLoggingFrequency

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.ResultLoggingFrequency"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._86", "ResultLoggingFrequency"
        )(value)

    @result_logging_frequency.setter
    @enforce_parameter_types
    def result_logging_frequency(self: Self, value: "_86.ResultLoggingFrequency"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.ResultLoggingFrequency"
        )
        self.wrapped.ResultLoggingFrequency = value

    @property
    def rotate_connections_with_bodies(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RotateConnectionsWithBodies

        if temp is None:
            return False

        return temp

    @rotate_connections_with_bodies.setter
    @enforce_parameter_types
    def rotate_connections_with_bodies(self: Self, value: "bool"):
        self.wrapped.RotateConnectionsWithBodies = (
            bool(value) if value is not None else False
        )

    @property
    def solver_tolerance_input_method(
        self: Self,
    ) -> "_93.TransientSolverToleranceInputMethod":
        """mastapy.nodal_analysis.TransientSolverToleranceInputMethod"""
        temp = self.wrapped.SolverToleranceInputMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.TransientSolverToleranceInputMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._93", "TransientSolverToleranceInputMethod"
        )(value)

    @solver_tolerance_input_method.setter
    @enforce_parameter_types
    def solver_tolerance_input_method(
        self: Self, value: "_93.TransientSolverToleranceInputMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.TransientSolverToleranceInputMethod"
        )
        self.wrapped.SolverToleranceInputMethod = value

    @property
    def theta(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Theta

        if temp is None:
            return 0.0

        return temp

    @theta.setter
    @enforce_parameter_types
    def theta(self: Self, value: "float"):
        self.wrapped.Theta = float(value) if value is not None else 0.0

    @property
    def time_for_initial_transients(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TimeForInitialTransients

        if temp is None:
            return 0.0

        return temp

    @time_for_initial_transients.setter
    @enforce_parameter_types
    def time_for_initial_transients(self: Self, value: "float"):
        self.wrapped.TimeForInitialTransients = (
            float(value) if value is not None else 0.0
        )

    @property
    def time_step_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TimeStepLength

        if temp is None:
            return 0.0

        return temp

    @time_step_length.setter
    @enforce_parameter_types
    def time_step_length(self: Self, value: "float"):
        self.wrapped.TimeStepLength = float(value) if value is not None else 0.0

    @property
    def time_to_start_using_final_results_maximum_time_step(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TimeToStartUsingFinalResultsMaximumTimeStep

        if temp is None:
            return 0.0

        return temp

    @time_to_start_using_final_results_maximum_time_step.setter
    @enforce_parameter_types
    def time_to_start_using_final_results_maximum_time_step(self: Self, value: "float"):
        self.wrapped.TimeToStartUsingFinalResultsMaximumTimeStep = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_non_linear_solver_for_step(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseNonLinearSolverForStep

        if temp is None:
            return False

        return temp

    @use_non_linear_solver_for_step.setter
    @enforce_parameter_types
    def use_non_linear_solver_for_step(self: Self, value: "bool"):
        self.wrapped.UseNonLinearSolverForStep = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: Self) -> "TransientSolverOptions._Cast_TransientSolverOptions":
        return self._Cast_TransientSolverOptions(self)
