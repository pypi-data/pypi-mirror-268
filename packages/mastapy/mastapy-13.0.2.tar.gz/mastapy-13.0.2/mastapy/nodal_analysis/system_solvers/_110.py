"""NewmarkAccelerationTransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _113
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NEWMARK_ACCELERATION_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "NewmarkAccelerationTransientSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import _119, _107, _121, _106, _120, _118


__docformat__ = "restructuredtext en"
__all__ = ("NewmarkAccelerationTransientSolver",)


Self = TypeVar("Self", bound="NewmarkAccelerationTransientSolver")


class NewmarkAccelerationTransientSolver(
    _113.SimpleAccelerationBasedStepHalvingTransientSolver
):
    """NewmarkAccelerationTransientSolver

    This is a mastapy class.
    """

    TYPE = _NEWMARK_ACCELERATION_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NewmarkAccelerationTransientSolver")

    class _Cast_NewmarkAccelerationTransientSolver:
        """Special nested class for casting NewmarkAccelerationTransientSolver to subclasses."""

        def __init__(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
            parent: "NewmarkAccelerationTransientSolver",
        ):
            self._parent = parent

        @property
        def simple_acceleration_based_step_halving_transient_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ) -> "_113.SimpleAccelerationBasedStepHalvingTransientSolver":
            return self._parent._cast(
                _113.SimpleAccelerationBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ) -> "_119.StepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ) -> "_107.InternalTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def transient_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ) -> "_121.TransientSolver":
            from mastapy.nodal_analysis.system_solvers import _121

            return self._parent._cast(_121.TransientSolver)

        @property
        def dynamic_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ) -> "_120.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.StiffnessSolver)

        @property
        def solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ) -> "_118.Solver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.Solver)

        @property
        def newmark_acceleration_transient_solver(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
        ) -> "NewmarkAccelerationTransientSolver":
            return self._parent

        def __getattr__(
            self: "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver",
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
        self: Self, instance_to_wrap: "NewmarkAccelerationTransientSolver.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "NewmarkAccelerationTransientSolver._Cast_NewmarkAccelerationTransientSolver":
        return self._Cast_NewmarkAccelerationTransientSolver(self)
