"""LobattoIIIATransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _114
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOBATTO_IIIA_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "LobattoIIIATransientSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import _119, _107, _121, _106, _120, _118


__docformat__ = "restructuredtext en"
__all__ = ("LobattoIIIATransientSolver",)


Self = TypeVar("Self", bound="LobattoIIIATransientSolver")


class LobattoIIIATransientSolver(_114.SimpleVelocityBasedStepHalvingTransientSolver):
    """LobattoIIIATransientSolver

    This is a mastapy class.
    """

    TYPE = _LOBATTO_IIIA_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LobattoIIIATransientSolver")

    class _Cast_LobattoIIIATransientSolver:
        """Special nested class for casting LobattoIIIATransientSolver to subclasses."""

        def __init__(
            self: "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver",
            parent: "LobattoIIIATransientSolver",
        ):
            self._parent = parent

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver",
        ) -> "_114.SimpleVelocityBasedStepHalvingTransientSolver":
            return self._parent._cast(
                _114.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver",
        ) -> "_119.StepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.StepHalvingTransientSolver)

        @property
        def internal_transient_solver(
            self: "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver",
        ) -> "_107.InternalTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def transient_solver(
            self: "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver",
        ) -> "_121.TransientSolver":
            from mastapy.nodal_analysis.system_solvers import _121

            return self._parent._cast(_121.TransientSolver)

        @property
        def dynamic_solver(
            self: "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver",
        ) -> "_120.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.StiffnessSolver)

        @property
        def solver(
            self: "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver",
        ) -> "_118.Solver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.Solver)

        @property
        def lobatto_iiia_transient_solver(
            self: "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver",
        ) -> "LobattoIIIATransientSolver":
            return self._parent

        def __getattr__(
            self: "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LobattoIIIATransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LobattoIIIATransientSolver._Cast_LobattoIIIATransientSolver":
        return self._Cast_LobattoIIIATransientSolver(self)
