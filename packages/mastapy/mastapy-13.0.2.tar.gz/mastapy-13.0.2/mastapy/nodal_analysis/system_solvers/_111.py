"""NewmarkTransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _114
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NEWMARK_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "NewmarkTransientSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import _119, _107, _121, _106, _120, _118


__docformat__ = "restructuredtext en"
__all__ = ("NewmarkTransientSolver",)


Self = TypeVar("Self", bound="NewmarkTransientSolver")


class NewmarkTransientSolver(_114.SimpleVelocityBasedStepHalvingTransientSolver):
    """NewmarkTransientSolver

    This is a mastapy class.
    """

    TYPE = _NEWMARK_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NewmarkTransientSolver")

    class _Cast_NewmarkTransientSolver:
        """Special nested class for casting NewmarkTransientSolver to subclasses."""

        def __init__(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
            parent: "NewmarkTransientSolver",
        ):
            self._parent = parent

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ) -> "_114.SimpleVelocityBasedStepHalvingTransientSolver":
            return self._parent._cast(
                _114.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ) -> "_119.StepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ) -> "_107.InternalTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def transient_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ) -> "_121.TransientSolver":
            from mastapy.nodal_analysis.system_solvers import _121

            return self._parent._cast(_121.TransientSolver)

        @property
        def dynamic_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ) -> "_120.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.StiffnessSolver)

        @property
        def solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ) -> "_118.Solver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.Solver)

        @property
        def newmark_transient_solver(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver",
        ) -> "NewmarkTransientSolver":
            return self._parent

        def __getattr__(
            self: "NewmarkTransientSolver._Cast_NewmarkTransientSolver", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NewmarkTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NewmarkTransientSolver._Cast_NewmarkTransientSolver":
        return self._Cast_NewmarkTransientSolver(self)
