"""SingularValuesAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGULAR_VALUES_ANALYSIS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "SingularValuesAnalysis"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import _117


__docformat__ = "restructuredtext en"
__all__ = ("SingularValuesAnalysis",)


Self = TypeVar("Self", bound="SingularValuesAnalysis")


class SingularValuesAnalysis(_0.APIBase):
    """SingularValuesAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGULAR_VALUES_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SingularValuesAnalysis")

    class _Cast_SingularValuesAnalysis:
        """Special nested class for casting SingularValuesAnalysis to subclasses."""

        def __init__(
            self: "SingularValuesAnalysis._Cast_SingularValuesAnalysis",
            parent: "SingularValuesAnalysis",
        ):
            self._parent = parent

        @property
        def singular_values_analysis(
            self: "SingularValuesAnalysis._Cast_SingularValuesAnalysis",
        ) -> "SingularValuesAnalysis":
            return self._parent

        def __getattr__(
            self: "SingularValuesAnalysis._Cast_SingularValuesAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SingularValuesAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def condition_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConditionNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_matrix_degrees_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessMatrixDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def stiffness_matrix_rank(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessMatrixRank

        if temp is None:
            return 0

        return temp

    @property
    def largest_singular_vectors(self: Self) -> "List[_117.SingularVectorAnalysis]":
        """List[mastapy.nodal_analysis.system_solvers.SingularVectorAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LargestSingularVectors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def smallest_singular_vectors(self: Self) -> "List[_117.SingularVectorAnalysis]":
        """List[mastapy.nodal_analysis.system_solvers.SingularVectorAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallestSingularVectors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "SingularValuesAnalysis._Cast_SingularValuesAnalysis":
        return self._Cast_SingularValuesAnalysis(self)
