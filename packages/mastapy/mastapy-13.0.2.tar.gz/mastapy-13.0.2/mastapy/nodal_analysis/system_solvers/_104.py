"""BackwardEulerTransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _114
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BACKWARD_EULER_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "BackwardEulerTransientSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import _119, _107, _121, _106, _120, _118


__docformat__ = "restructuredtext en"
__all__ = ("BackwardEulerTransientSolver",)


Self = TypeVar("Self", bound="BackwardEulerTransientSolver")


class BackwardEulerTransientSolver(_114.SimpleVelocityBasedStepHalvingTransientSolver):
    """BackwardEulerTransientSolver

    This is a mastapy class.
    """

    TYPE = _BACKWARD_EULER_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BackwardEulerTransientSolver")

    class _Cast_BackwardEulerTransientSolver:
        """Special nested class for casting BackwardEulerTransientSolver to subclasses."""

        def __init__(
            self: "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver",
            parent: "BackwardEulerTransientSolver",
        ):
            self._parent = parent

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver",
        ) -> "_114.SimpleVelocityBasedStepHalvingTransientSolver":
            return self._parent._cast(
                _114.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver",
        ) -> "_119.StepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver",
        ) -> "_107.InternalTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def transient_solver(
            self: "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver",
        ) -> "_121.TransientSolver":
            from mastapy.nodal_analysis.system_solvers import _121

            return self._parent._cast(_121.TransientSolver)

        @property
        def dynamic_solver(
            self: "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver",
        ) -> "_120.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.StiffnessSolver)

        @property
        def solver(
            self: "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver",
        ) -> "_118.Solver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.Solver)

        @property
        def backward_euler_transient_solver(
            self: "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver",
        ) -> "BackwardEulerTransientSolver":
            return self._parent

        def __getattr__(
            self: "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BackwardEulerTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BackwardEulerTransientSolver._Cast_BackwardEulerTransientSolver":
        return self._Cast_BackwardEulerTransientSolver(self)
