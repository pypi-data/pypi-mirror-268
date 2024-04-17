"""ParetoOptimisationStrategy"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_STRATEGY = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationStrategy"
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1558, _1554, _1555


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationStrategy",)


Self = TypeVar("Self", bound="ParetoOptimisationStrategy")


class ParetoOptimisationStrategy(_1836.NamedDatabaseItem):
    """ParetoOptimisationStrategy

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_STRATEGY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParetoOptimisationStrategy")

    class _Cast_ParetoOptimisationStrategy:
        """Special nested class for casting ParetoOptimisationStrategy to subclasses."""

        def __init__(
            self: "ParetoOptimisationStrategy._Cast_ParetoOptimisationStrategy",
            parent: "ParetoOptimisationStrategy",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "ParetoOptimisationStrategy._Cast_ParetoOptimisationStrategy",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def pareto_optimisation_strategy(
            self: "ParetoOptimisationStrategy._Cast_ParetoOptimisationStrategy",
        ) -> "ParetoOptimisationStrategy":
            return self._parent

        def __getattr__(
            self: "ParetoOptimisationStrategy._Cast_ParetoOptimisationStrategy",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParetoOptimisationStrategy.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def charts(self: Self) -> "List[_1558.ParetoOptimisationStrategyChartInformation]":
        """List[mastapy.math_utility.optimisation.ParetoOptimisationStrategyChartInformation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Charts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def inputs(self: Self) -> "List[_1554.ParetoOptimisationInput]":
        """List[mastapy.math_utility.optimisation.ParetoOptimisationInput]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Inputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def outputs(self: Self) -> "List[_1555.ParetoOptimisationOutput]":
        """List[mastapy.math_utility.optimisation.ParetoOptimisationOutput]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Outputs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def add_chart(self: Self):
        """Method does not return."""
        self.wrapped.AddChart()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoOptimisationStrategy._Cast_ParetoOptimisationStrategy":
        return self._Cast_ParetoOptimisationStrategy(self)
