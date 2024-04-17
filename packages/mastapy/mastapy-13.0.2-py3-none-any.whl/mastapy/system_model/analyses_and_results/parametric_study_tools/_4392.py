"""ParametricStudyDOEResultVariable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.math_utility.optimisation import _1561
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_DOE_RESULT_VARIABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ParametricStudyDOEResultVariable",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1562


__docformat__ = "restructuredtext en"
__all__ = ("ParametricStudyDOEResultVariable",)


Self = TypeVar("Self", bound="ParametricStudyDOEResultVariable")


class ParametricStudyDOEResultVariable(_1561.ParetoOptimisationVariableBase):
    """ParametricStudyDOEResultVariable

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_DOE_RESULT_VARIABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParametricStudyDOEResultVariable")

    class _Cast_ParametricStudyDOEResultVariable:
        """Special nested class for casting ParametricStudyDOEResultVariable to subclasses."""

        def __init__(
            self: "ParametricStudyDOEResultVariable._Cast_ParametricStudyDOEResultVariable",
            parent: "ParametricStudyDOEResultVariable",
        ):
            self._parent = parent

        @property
        def pareto_optimisation_variable_base(
            self: "ParametricStudyDOEResultVariable._Cast_ParametricStudyDOEResultVariable",
        ) -> "_1561.ParetoOptimisationVariableBase":
            return self._parent._cast(_1561.ParetoOptimisationVariableBase)

        @property
        def parametric_study_doe_result_variable(
            self: "ParametricStudyDOEResultVariable._Cast_ParametricStudyDOEResultVariable",
        ) -> "ParametricStudyDOEResultVariable":
            return self._parent

        def __getattr__(
            self: "ParametricStudyDOEResultVariable._Cast_ParametricStudyDOEResultVariable",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParametricStudyDOEResultVariable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def entity_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EntityName

        if temp is None:
            return ""

        return temp

    @property
    def max(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Max

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @max.setter
    @enforce_parameter_types
    def max(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Max = value

    @property
    def min(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Min

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @min.setter
    @enforce_parameter_types
    def min(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Min = value

    @property
    def parameter_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParameterName

        if temp is None:
            return ""

        return temp

    @property
    def target_for_dominant_candidate_search(
        self: Self,
    ) -> "_1562.PropertyTargetForDominantCandidateSearch":
        """mastapy.math_utility.optimisation.PropertyTargetForDominantCandidateSearch"""
        temp = self.wrapped.TargetForDominantCandidateSearch

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

    @target_for_dominant_candidate_search.setter
    @enforce_parameter_types
    def target_for_dominant_candidate_search(
        self: Self, value: "_1562.PropertyTargetForDominantCandidateSearch"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.MathUtility.Optimisation.PropertyTargetForDominantCandidateSearch",
        )
        self.wrapped.TargetForDominantCandidateSearch = value

    @property
    def cast_to(
        self: Self,
    ) -> "ParametricStudyDOEResultVariable._Cast_ParametricStudyDOEResultVariable":
        return self._Cast_ParametricStudyDOEResultVariable(self)
