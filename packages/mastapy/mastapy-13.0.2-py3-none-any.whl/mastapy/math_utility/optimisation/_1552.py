"""OptimizationVariable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_VARIABLE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "OptimizationVariable"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1612
    from mastapy.math_utility.optimisation import _1551, _1563


__docformat__ = "restructuredtext en"
__all__ = ("OptimizationVariable",)


Self = TypeVar("Self", bound="OptimizationVariable")


class OptimizationVariable(_0.APIBase):
    """OptimizationVariable

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_VARIABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OptimizationVariable")

    class _Cast_OptimizationVariable:
        """Special nested class for casting OptimizationVariable to subclasses."""

        def __init__(
            self: "OptimizationVariable._Cast_OptimizationVariable",
            parent: "OptimizationVariable",
        ):
            self._parent = parent

        @property
        def optimization_input(
            self: "OptimizationVariable._Cast_OptimizationVariable",
        ) -> "_1551.OptimizationInput":
            from mastapy.math_utility.optimisation import _1551

            return self._parent._cast(_1551.OptimizationInput)

        @property
        def reporting_optimization_input(
            self: "OptimizationVariable._Cast_OptimizationVariable",
        ) -> "_1563.ReportingOptimizationInput":
            from mastapy.math_utility.optimisation import _1563

            return self._parent._cast(_1563.ReportingOptimizationInput)

        @property
        def optimization_variable(
            self: "OptimizationVariable._Cast_OptimizationVariable",
        ) -> "OptimizationVariable":
            return self._parent

        def __getattr__(
            self: "OptimizationVariable._Cast_OptimizationVariable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OptimizationVariable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measurement(self: Self) -> "_1612.MeasurementBase":
        """mastapy.utility.units_and_measurements.MeasurementBase"""
        temp = self.wrapped.Measurement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @measurement.setter
    @enforce_parameter_types
    def measurement(self: Self, value: "_1612.MeasurementBase"):
        self.wrapped.Measurement = value.wrapped

    @property
    def results(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Results

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "OptimizationVariable._Cast_OptimizationVariable":
        return self._Cast_OptimizationVariable(self)
