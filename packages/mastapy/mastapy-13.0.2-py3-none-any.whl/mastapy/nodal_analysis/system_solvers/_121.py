"""TransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.system_solvers import _106
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "TransientSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _92
    from mastapy.nodal_analysis.system_solvers import (
        _103,
        _104,
        _107,
        _108,
        _109,
        _110,
        _111,
        _112,
        _113,
        _114,
        _119,
        _122,
        _120,
        _118,
    )


__docformat__ = "restructuredtext en"
__all__ = ("TransientSolver",)


Self = TypeVar("Self", bound="TransientSolver")


class TransientSolver(_106.DynamicSolver):
    """TransientSolver

    This is a mastapy class.
    """

    TYPE = _TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TransientSolver")

    class _Cast_TransientSolver:
        """Special nested class for casting TransientSolver to subclasses."""

        def __init__(
            self: "TransientSolver._Cast_TransientSolver", parent: "TransientSolver"
        ):
            self._parent = parent

        @property
        def dynamic_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_106.DynamicSolver":
            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_120.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.StiffnessSolver)

        @property
        def solver(self: "TransientSolver._Cast_TransientSolver") -> "_118.Solver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.Solver)

        @property
        def backward_euler_acceleration_step_halving_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_103.BackwardEulerAccelerationStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(
                _103.BackwardEulerAccelerationStepHalvingTransientSolver
            )

        @property
        def backward_euler_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_104.BackwardEulerTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _104

            return self._parent._cast(_104.BackwardEulerTransientSolver)

        @property
        def internal_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_107.InternalTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def lobatto_iiia_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_108.LobattoIIIATransientSolver":
            from mastapy.nodal_analysis.system_solvers import _108

            return self._parent._cast(_108.LobattoIIIATransientSolver)

        @property
        def lobatto_iiic_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_109.LobattoIIICTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _109

            return self._parent._cast(_109.LobattoIIICTransientSolver)

        @property
        def newmark_acceleration_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_110.NewmarkAccelerationTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _110

            return self._parent._cast(_110.NewmarkAccelerationTransientSolver)

        @property
        def newmark_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_111.NewmarkTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _111

            return self._parent._cast(_111.NewmarkTransientSolver)

        @property
        def semi_implicit_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_112.SemiImplicitTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _112

            return self._parent._cast(_112.SemiImplicitTransientSolver)

        @property
        def simple_acceleration_based_step_halving_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_113.SimpleAccelerationBasedStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _113

            return self._parent._cast(
                _113.SimpleAccelerationBasedStepHalvingTransientSolver
            )

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_114.SimpleVelocityBasedStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _114

            return self._parent._cast(
                _114.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_119.StepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.StepHalvingTransientSolver)

        @property
        def wilson_theta_transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "_122.WilsonThetaTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _122

            return self._parent._cast(_122.WilsonThetaTransientSolver)

        @property
        def transient_solver(
            self: "TransientSolver._Cast_TransientSolver",
        ) -> "TransientSolver":
            return self._parent

        def __getattr__(self: "TransientSolver._Cast_TransientSolver", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_number_of_jacobian_evaluations_per_newton_raphson_solve(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageNumberOfJacobianEvaluationsPerNewtonRaphsonSolve

        if temp is None:
            return 0.0

        return temp

    @property
    def interface_analysis_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InterfaceAnalysisTime

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_failed_newton_raphson_solves(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfFailedNewtonRaphsonSolves

        if temp is None:
            return 0

        return temp

    @property
    def number_of_failed_time_steps(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfFailedTimeSteps

        if temp is None:
            return 0

        return temp

    @property
    def number_of_failed_time_steps_at_minimum_time_step(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfFailedTimeStepsAtMinimumTimeStep

        if temp is None:
            return 0

        return temp

    @property
    def number_of_interface_time_steps(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfInterfaceTimeSteps

        if temp is None:
            return 0

        return temp

    @property
    def number_of_newton_raphson_jacobian_evaluations(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfNewtonRaphsonJacobianEvaluations

        if temp is None:
            return 0

        return temp

    @property
    def number_of_newton_raphson_maximum_iterations_reached(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfNewtonRaphsonMaximumIterationsReached

        if temp is None:
            return 0

        return temp

    @property
    def number_of_newton_raphson_other_status_results(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfNewtonRaphsonOtherStatusResults

        if temp is None:
            return 0

        return temp

    @property
    def number_of_newton_raphson_residual_evaluations(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfNewtonRaphsonResidualEvaluations

        if temp is None:
            return 0

        return temp

    @property
    def number_of_newton_raphson_residual_tolerance_met(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfNewtonRaphsonResidualToleranceMet

        if temp is None:
            return 0

        return temp

    @property
    def number_of_newton_raphson_solves(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfNewtonRaphsonSolves

        if temp is None:
            return 0

        return temp

    @property
    def number_of_newton_raphson_values_not_changing(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfNewtonRaphsonValuesNotChanging

        if temp is None:
            return 0

        return temp

    @property
    def number_of_time_steps_taken(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTimeStepsTaken

        if temp is None:
            return 0

        return temp

    @property
    def number_of_times_step_error_tolerance_not_met(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTimesStepErrorToleranceNotMet

        if temp is None:
            return 0

        return temp

    @property
    def solver_status(self: Self) -> "_92.TransientSolverStatus":
        """mastapy.nodal_analysis.TransientSolverStatus"""
        temp = self.wrapped.SolverStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.TransientSolverStatus"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._92", "TransientSolverStatus"
        )(value)

    @solver_status.setter
    @enforce_parameter_types
    def solver_status(self: Self, value: "_92.TransientSolverStatus"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.TransientSolverStatus"
        )
        self.wrapped.SolverStatus = value

    def times_of_logged_results(self: Self) -> "List[float]":
        """List[float]"""
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.TimesOfLoggedResults(), float
        )

    @property
    def cast_to(self: Self) -> "TransientSolver._Cast_TransientSolver":
        return self._Cast_TransientSolver(self)
