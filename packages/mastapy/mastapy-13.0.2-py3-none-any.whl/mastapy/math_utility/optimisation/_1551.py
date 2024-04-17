"""OptimizationInput"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility.optimisation import _1552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_INPUT = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "OptimizationInput"
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1563


__docformat__ = "restructuredtext en"
__all__ = ("OptimizationInput",)


Self = TypeVar("Self", bound="OptimizationInput")


class OptimizationInput(_1552.OptimizationVariable):
    """OptimizationInput

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_INPUT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OptimizationInput")

    class _Cast_OptimizationInput:
        """Special nested class for casting OptimizationInput to subclasses."""

        def __init__(
            self: "OptimizationInput._Cast_OptimizationInput",
            parent: "OptimizationInput",
        ):
            self._parent = parent

        @property
        def optimization_variable(
            self: "OptimizationInput._Cast_OptimizationInput",
        ) -> "_1552.OptimizationVariable":
            return self._parent._cast(_1552.OptimizationVariable)

        @property
        def reporting_optimization_input(
            self: "OptimizationInput._Cast_OptimizationInput",
        ) -> "_1563.ReportingOptimizationInput":
            from mastapy.math_utility.optimisation import _1563

            return self._parent._cast(_1563.ReportingOptimizationInput)

        @property
        def optimization_input(
            self: "OptimizationInput._Cast_OptimizationInput",
        ) -> "OptimizationInput":
            return self._parent

        def __getattr__(self: "OptimizationInput._Cast_OptimizationInput", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OptimizationInput.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "OptimizationInput._Cast_OptimizationInput":
        return self._Cast_OptimizationInput(self)
