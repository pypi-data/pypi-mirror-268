"""EntityVectorState"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENTITY_VECTOR_STATE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.States", "EntityVectorState"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1533
    from mastapy.nodal_analysis.states import _123, _124, _126, _127


__docformat__ = "restructuredtext en"
__all__ = ("EntityVectorState",)


Self = TypeVar("Self", bound="EntityVectorState")


class EntityVectorState(_0.APIBase):
    """EntityVectorState

    This is a mastapy class.
    """

    TYPE = _ENTITY_VECTOR_STATE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EntityVectorState")

    class _Cast_EntityVectorState:
        """Special nested class for casting EntityVectorState to subclasses."""

        def __init__(
            self: "EntityVectorState._Cast_EntityVectorState",
            parent: "EntityVectorState",
        ):
            self._parent = parent

        @property
        def element_scalar_state(
            self: "EntityVectorState._Cast_EntityVectorState",
        ) -> "_123.ElementScalarState":
            from mastapy.nodal_analysis.states import _123

            return self._parent._cast(_123.ElementScalarState)

        @property
        def element_vector_state(
            self: "EntityVectorState._Cast_EntityVectorState",
        ) -> "_124.ElementVectorState":
            from mastapy.nodal_analysis.states import _124

            return self._parent._cast(_124.ElementVectorState)

        @property
        def node_scalar_state(
            self: "EntityVectorState._Cast_EntityVectorState",
        ) -> "_126.NodeScalarState":
            from mastapy.nodal_analysis.states import _126

            return self._parent._cast(_126.NodeScalarState)

        @property
        def node_vector_state(
            self: "EntityVectorState._Cast_EntityVectorState",
        ) -> "_127.NodeVectorState":
            from mastapy.nodal_analysis.states import _127

            return self._parent._cast(_127.NodeVectorState)

        @property
        def entity_vector_state(
            self: "EntityVectorState._Cast_EntityVectorState",
        ) -> "EntityVectorState":
            return self._parent

        def __getattr__(self: "EntityVectorState._Cast_EntityVectorState", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EntityVectorState.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degrees_of_freedom_per_entity(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DegreesOfFreedomPerEntity

        if temp is None:
            return 0

        return temp

    @property
    def number_of_entities(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfEntities

        if temp is None:
            return 0

        return temp

    @property
    def vector(self: Self) -> "_1533.RealVector":
        """mastapy.math_utility.RealVector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Vector

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "EntityVectorState._Cast_EntityVectorState":
        return self._Cast_EntityVectorState(self)
