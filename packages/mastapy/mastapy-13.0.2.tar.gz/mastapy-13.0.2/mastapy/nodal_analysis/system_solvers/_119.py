"""StepHalvingTransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _107
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEP_HALVING_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "StepHalvingTransientSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import (
        _103,
        _104,
        _108,
        _109,
        _110,
        _111,
        _113,
        _114,
        _122,
        _121,
        _106,
        _120,
        _118,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StepHalvingTransientSolver",)


Self = TypeVar("Self", bound="StepHalvingTransientSolver")


class StepHalvingTransientSolver(_107.InternalTransientSolver):
    """StepHalvingTransientSolver

    This is a mastapy class.
    """

    TYPE = _STEP_HALVING_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StepHalvingTransientSolver")

    class _Cast_StepHalvingTransientSolver:
        """Special nested class for casting StepHalvingTransientSolver to subclasses."""

        def __init__(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
            parent: "StepHalvingTransientSolver",
        ):
            self._parent = parent

        @property
        def internal_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_107.InternalTransientSolver":
            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_121.TransientSolver":
            from mastapy.nodal_analysis.system_solvers import _121

            return self._parent._cast(_121.TransientSolver)

        @property
        def dynamic_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_120.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.StiffnessSolver)

        @property
        def solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_118.Solver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.Solver)

        @property
        def backward_euler_acceleration_step_halving_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_103.BackwardEulerAccelerationStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(
                _103.BackwardEulerAccelerationStepHalvingTransientSolver
            )

        @property
        def backward_euler_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_104.BackwardEulerTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _104

            return self._parent._cast(_104.BackwardEulerTransientSolver)

        @property
        def lobatto_iiia_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_108.LobattoIIIATransientSolver":
            from mastapy.nodal_analysis.system_solvers import _108

            return self._parent._cast(_108.LobattoIIIATransientSolver)

        @property
        def lobatto_iiic_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_109.LobattoIIICTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _109

            return self._parent._cast(_109.LobattoIIICTransientSolver)

        @property
        def newmark_acceleration_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_110.NewmarkAccelerationTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _110

            return self._parent._cast(_110.NewmarkAccelerationTransientSolver)

        @property
        def newmark_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_111.NewmarkTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _111

            return self._parent._cast(_111.NewmarkTransientSolver)

        @property
        def simple_acceleration_based_step_halving_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_113.SimpleAccelerationBasedStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _113

            return self._parent._cast(
                _113.SimpleAccelerationBasedStepHalvingTransientSolver
            )

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_114.SimpleVelocityBasedStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _114

            return self._parent._cast(
                _114.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def wilson_theta_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_122.WilsonThetaTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _122

            return self._parent._cast(_122.WilsonThetaTransientSolver)

        @property
        def step_halving_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "StepHalvingTransientSolver":
            return self._parent

        def __getattr__(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StepHalvingTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver":
        return self._Cast_StepHalvingTransientSolver(self)
