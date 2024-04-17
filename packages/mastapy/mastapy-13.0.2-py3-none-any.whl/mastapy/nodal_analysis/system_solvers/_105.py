"""DenseStiffnessSolver"""

from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.system_solvers import _118
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DENSE_STIFFNESS_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "DenseStiffnessSolver"
)


__docformat__ = "restructuredtext en"
__all__ = ("DenseStiffnessSolver",)


Self = TypeVar("Self", bound="DenseStiffnessSolver")


class DenseStiffnessSolver(_118.Solver):
    """DenseStiffnessSolver

    This is a mastapy class.
    """

    TYPE = _DENSE_STIFFNESS_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DenseStiffnessSolver")

    class _Cast_DenseStiffnessSolver:
        """Special nested class for casting DenseStiffnessSolver to subclasses."""

        def __init__(
            self: "DenseStiffnessSolver._Cast_DenseStiffnessSolver",
            parent: "DenseStiffnessSolver",
        ):
            self._parent = parent

        @property
        def solver(
            self: "DenseStiffnessSolver._Cast_DenseStiffnessSolver",
        ) -> "_118.Solver":
            return self._parent._cast(_118.Solver)

        @property
        def dense_stiffness_solver(
            self: "DenseStiffnessSolver._Cast_DenseStiffnessSolver",
        ) -> "DenseStiffnessSolver":
            return self._parent

        def __getattr__(
            self: "DenseStiffnessSolver._Cast_DenseStiffnessSolver", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DenseStiffnessSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DenseStiffnessSolver._Cast_DenseStiffnessSolver":
        return self._Cast_DenseStiffnessSolver(self)
