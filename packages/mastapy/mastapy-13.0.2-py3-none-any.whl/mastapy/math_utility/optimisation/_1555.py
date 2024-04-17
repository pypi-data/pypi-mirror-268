"""ParetoOptimisationOutput"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.math_utility.optimisation import _1560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_OUTPUT = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationOutput"
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1561


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationOutput",)


Self = TypeVar("Self", bound="ParetoOptimisationOutput")


class ParetoOptimisationOutput(_1560.ParetoOptimisationVariable):
    """ParetoOptimisationOutput

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_OUTPUT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParetoOptimisationOutput")

    class _Cast_ParetoOptimisationOutput:
        """Special nested class for casting ParetoOptimisationOutput to subclasses."""

        def __init__(
            self: "ParetoOptimisationOutput._Cast_ParetoOptimisationOutput",
            parent: "ParetoOptimisationOutput",
        ):
            self._parent = parent

        @property
        def pareto_optimisation_variable(
            self: "ParetoOptimisationOutput._Cast_ParetoOptimisationOutput",
        ) -> "_1560.ParetoOptimisationVariable":
            return self._parent._cast(_1560.ParetoOptimisationVariable)

        @property
        def pareto_optimisation_variable_base(
            self: "ParetoOptimisationOutput._Cast_ParetoOptimisationOutput",
        ) -> "_1561.ParetoOptimisationVariableBase":
            from mastapy.math_utility.optimisation import _1561

            return self._parent._cast(_1561.ParetoOptimisationVariableBase)

        @property
        def pareto_optimisation_output(
            self: "ParetoOptimisationOutput._Cast_ParetoOptimisationOutput",
        ) -> "ParetoOptimisationOutput":
            return self._parent

        def __getattr__(
            self: "ParetoOptimisationOutput._Cast_ParetoOptimisationOutput", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParetoOptimisationOutput.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def percent(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Percent

        if temp is None:
            return 0.0

        return temp

    @percent.setter
    @enforce_parameter_types
    def percent(self: Self, value: "float"):
        self.wrapped.Percent = float(value) if value is not None else 0.0

    @property
    def exclude_from_dominant_candidates_search(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ExcludeFromDominantCandidatesSearch

        if temp is None:
            return False

        return temp

    @exclude_from_dominant_candidates_search.setter
    @enforce_parameter_types
    def exclude_from_dominant_candidates_search(self: Self, value: "bool"):
        self.wrapped.ExcludeFromDominantCandidatesSearch = (
            bool(value) if value is not None else False
        )

    @property
    def use_original_design_value(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseOriginalDesignValue

        if temp is None:
            return False

        return temp

    @use_original_design_value.setter
    @enforce_parameter_types
    def use_original_design_value(self: Self, value: "bool"):
        self.wrapped.UseOriginalDesignValue = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoOptimisationOutput._Cast_ParetoOptimisationOutput":
        return self._Cast_ParetoOptimisationOutput(self)
