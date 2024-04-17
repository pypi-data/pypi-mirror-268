"""SimpleAccelerationBasedStepHalvingTransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _119
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIMPLE_ACCELERATION_BASED_STEP_HALVING_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers",
    "SimpleAccelerationBasedStepHalvingTransientSolver",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import (
        _103,
        _110,
        _107,
        _121,
        _106,
        _120,
        _118,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SimpleAccelerationBasedStepHalvingTransientSolver",)


Self = TypeVar("Self", bound="SimpleAccelerationBasedStepHalvingTransientSolver")


class SimpleAccelerationBasedStepHalvingTransientSolver(
    _119.StepHalvingTransientSolver
):
    """SimpleAccelerationBasedStepHalvingTransientSolver

    This is a mastapy class.
    """

    TYPE = _SIMPLE_ACCELERATION_BASED_STEP_HALVING_TRANSIENT_SOLVER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SimpleAccelerationBasedStepHalvingTransientSolver"
    )

    class _Cast_SimpleAccelerationBasedStepHalvingTransientSolver:
        """Special nested class for casting SimpleAccelerationBasedStepHalvingTransientSolver to subclasses."""

        def __init__(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
            parent: "SimpleAccelerationBasedStepHalvingTransientSolver",
        ):
            self._parent = parent

        @property
        def step_halving_transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ) -> "_119.StepHalvingTransientSolver":
            return self._parent._cast(_119.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ) -> "_107.InternalTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ) -> "_121.TransientSolver":
            from mastapy.nodal_analysis.system_solvers import _121

            return self._parent._cast(_121.TransientSolver)

        @property
        def dynamic_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ) -> "_120.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.StiffnessSolver)

        @property
        def solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ) -> "_118.Solver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.Solver)

        @property
        def backward_euler_acceleration_step_halving_transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ) -> "_103.BackwardEulerAccelerationStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(
                _103.BackwardEulerAccelerationStepHalvingTransientSolver
            )

        @property
        def newmark_acceleration_transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ) -> "_110.NewmarkAccelerationTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _110

            return self._parent._cast(_110.NewmarkAccelerationTransientSolver)

        @property
        def simple_acceleration_based_step_halving_transient_solver(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
        ) -> "SimpleAccelerationBasedStepHalvingTransientSolver":
            return self._parent

        def __getattr__(
            self: "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver",
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
        instance_to_wrap: "SimpleAccelerationBasedStepHalvingTransientSolver.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SimpleAccelerationBasedStepHalvingTransientSolver._Cast_SimpleAccelerationBasedStepHalvingTransientSolver":
        return self._Cast_SimpleAccelerationBasedStepHalvingTransientSolver(self)
