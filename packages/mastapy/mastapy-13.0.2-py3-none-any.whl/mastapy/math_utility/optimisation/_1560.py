"""ParetoOptimisationVariable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.math_utility.optimisation import _1561
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_VARIABLE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationVariable"
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1562, _1554, _1555


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationVariable",)


Self = TypeVar("Self", bound="ParetoOptimisationVariable")


class ParetoOptimisationVariable(_1561.ParetoOptimisationVariableBase):
    """ParetoOptimisationVariable

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_VARIABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParetoOptimisationVariable")

    class _Cast_ParetoOptimisationVariable:
        """Special nested class for casting ParetoOptimisationVariable to subclasses."""

        def __init__(
            self: "ParetoOptimisationVariable._Cast_ParetoOptimisationVariable",
            parent: "ParetoOptimisationVariable",
        ):
            self._parent = parent

        @property
        def pareto_optimisation_variable_base(
            self: "ParetoOptimisationVariable._Cast_ParetoOptimisationVariable",
        ) -> "_1561.ParetoOptimisationVariableBase":
            return self._parent._cast(_1561.ParetoOptimisationVariableBase)

        @property
        def pareto_optimisation_input(
            self: "ParetoOptimisationVariable._Cast_ParetoOptimisationVariable",
        ) -> "_1554.ParetoOptimisationInput":
            from mastapy.math_utility.optimisation import _1554

            return self._parent._cast(_1554.ParetoOptimisationInput)

        @property
        def pareto_optimisation_output(
            self: "ParetoOptimisationVariable._Cast_ParetoOptimisationVariable",
        ) -> "_1555.ParetoOptimisationOutput":
            from mastapy.math_utility.optimisation import _1555

            return self._parent._cast(_1555.ParetoOptimisationOutput)

        @property
        def pareto_optimisation_variable(
            self: "ParetoOptimisationVariable._Cast_ParetoOptimisationVariable",
        ) -> "ParetoOptimisationVariable":
            return self._parent

        def __getattr__(
            self: "ParetoOptimisationVariable._Cast_ParetoOptimisationVariable",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParetoOptimisationVariable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def property_target_for_dominant_candidate_search(
        self: Self,
    ) -> "_1562.PropertyTargetForDominantCandidateSearch":
        """mastapy.math_utility.optimisation.PropertyTargetForDominantCandidateSearch"""
        temp = self.wrapped.PropertyTargetForDominantCandidateSearch

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.MathUtility.Optimisation.PropertyTargetForDominantCandidateSearch",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility.optimisation._1562",
            "PropertyTargetForDominantCandidateSearch",
        )(value)

    @property_target_for_dominant_candidate_search.setter
    @enforce_parameter_types
    def property_target_for_dominant_candidate_search(
        self: Self, value: "_1562.PropertyTargetForDominantCandidateSearch"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.MathUtility.Optimisation.PropertyTargetForDominantCandidateSearch",
        )
        self.wrapped.PropertyTargetForDominantCandidateSearch = value

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoOptimisationVariable._Cast_ParetoOptimisationVariable":
        return self._Cast_ParetoOptimisationVariable(self)
