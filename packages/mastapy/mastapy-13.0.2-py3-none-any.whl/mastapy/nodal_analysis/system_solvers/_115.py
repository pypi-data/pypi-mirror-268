"""SingularDegreeOfFreedomAnalysis"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGULAR_DEGREE_OF_FREEDOM_ANALYSIS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "SingularDegreeOfFreedomAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("SingularDegreeOfFreedomAnalysis",)


Self = TypeVar("Self", bound="SingularDegreeOfFreedomAnalysis")


class SingularDegreeOfFreedomAnalysis(_0.APIBase):
    """SingularDegreeOfFreedomAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGULAR_DEGREE_OF_FREEDOM_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SingularDegreeOfFreedomAnalysis")

    class _Cast_SingularDegreeOfFreedomAnalysis:
        """Special nested class for casting SingularDegreeOfFreedomAnalysis to subclasses."""

        def __init__(
            self: "SingularDegreeOfFreedomAnalysis._Cast_SingularDegreeOfFreedomAnalysis",
            parent: "SingularDegreeOfFreedomAnalysis",
        ):
            self._parent = parent

        @property
        def singular_degree_of_freedom_analysis(
            self: "SingularDegreeOfFreedomAnalysis._Cast_SingularDegreeOfFreedomAnalysis",
        ) -> "SingularDegreeOfFreedomAnalysis":
            return self._parent

        def __getattr__(
            self: "SingularDegreeOfFreedomAnalysis._Cast_SingularDegreeOfFreedomAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SingularDegreeOfFreedomAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def components_using_node(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsUsingNode

        if temp is None:
            return ""

        return temp

    @property
    def global_degree_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GlobalDegreeOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def nodal_entities_using_node(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodalEntitiesUsingNode

        if temp is None:
            return ""

        return temp

    @property
    def node_degree_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeDegreeOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def node_id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeID

        if temp is None:
            return 0

        return temp

    @property
    def node_names(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeNames

        if temp is None:
            return ""

        return temp

    @property
    def vector_value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VectorValue

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "SingularDegreeOfFreedomAnalysis._Cast_SingularDegreeOfFreedomAnalysis":
        return self._Cast_SingularDegreeOfFreedomAnalysis(self)
