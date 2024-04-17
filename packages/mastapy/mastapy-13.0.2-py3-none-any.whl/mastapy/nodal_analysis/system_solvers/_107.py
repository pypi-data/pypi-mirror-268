"""InternalTransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _121
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERNAL_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "InternalTransientSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import (
        _103,
        _104,
        _108,
        _109,
        _110,
        _111,
        _112,
        _113,
        _114,
        _119,
        _122,
        _106,
        _120,
        _118,
    )


__docformat__ = "restructuredtext en"
__all__ = ("InternalTransientSolver",)


Self = TypeVar("Self", bound="InternalTransientSolver")


class InternalTransientSolver(_121.TransientSolver):
    """InternalTransientSolver

    This is a mastapy class.
    """

    TYPE = _INTERNAL_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InternalTransientSolver")

    class _Cast_InternalTransientSolver:
        """Special nested class for casting InternalTransientSolver to subclasses."""

        def __init__(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
            parent: "InternalTransientSolver",
        ):
            self._parent = parent

        @property
        def transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_121.TransientSolver":
            return self._parent._cast(_121.TransientSolver)

        @property
        def dynamic_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_120.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.StiffnessSolver)

        @property
        def solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_118.Solver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.Solver)

        @property
        def backward_euler_acceleration_step_halving_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_103.BackwardEulerAccelerationStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(
                _103.BackwardEulerAccelerationStepHalvingTransientSolver
            )

        @property
        def backward_euler_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_104.BackwardEulerTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _104

            return self._parent._cast(_104.BackwardEulerTransientSolver)

        @property
        def lobatto_iiia_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_108.LobattoIIIATransientSolver":
            from mastapy.nodal_analysis.system_solvers import _108

            return self._parent._cast(_108.LobattoIIIATransientSolver)

        @property
        def lobatto_iiic_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_109.LobattoIIICTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _109

            return self._parent._cast(_109.LobattoIIICTransientSolver)

        @property
        def newmark_acceleration_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_110.NewmarkAccelerationTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _110

            return self._parent._cast(_110.NewmarkAccelerationTransientSolver)

        @property
        def newmark_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_111.NewmarkTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _111

            return self._parent._cast(_111.NewmarkTransientSolver)

        @property
        def semi_implicit_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_112.SemiImplicitTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _112

            return self._parent._cast(_112.SemiImplicitTransientSolver)

        @property
        def simple_acceleration_based_step_halving_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_113.SimpleAccelerationBasedStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _113

            return self._parent._cast(
                _113.SimpleAccelerationBasedStepHalvingTransientSolver
            )

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_114.SimpleVelocityBasedStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _114

            return self._parent._cast(
                _114.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_119.StepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.StepHalvingTransientSolver)

        @property
        def wilson_theta_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_122.WilsonThetaTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _122

            return self._parent._cast(_122.WilsonThetaTransientSolver)

        @property
        def internal_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "InternalTransientSolver":
            return self._parent

        def __getattr__(
            self: "InternalTransientSolver._Cast_InternalTransientSolver", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InternalTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InternalTransientSolver._Cast_InternalTransientSolver":
        return self._Cast_InternalTransientSolver(self)
