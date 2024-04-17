"""NodeVectorState"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.states import _125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODE_VECTOR_STATE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.States", "NodeVectorState"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.states import _126


__docformat__ = "restructuredtext en"
__all__ = ("NodeVectorState",)


Self = TypeVar("Self", bound="NodeVectorState")


class NodeVectorState(_125.EntityVectorState):
    """NodeVectorState

    This is a mastapy class.
    """

    TYPE = _NODE_VECTOR_STATE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodeVectorState")

    class _Cast_NodeVectorState:
        """Special nested class for casting NodeVectorState to subclasses."""

        def __init__(
            self: "NodeVectorState._Cast_NodeVectorState", parent: "NodeVectorState"
        ):
            self._parent = parent

        @property
        def entity_vector_state(
            self: "NodeVectorState._Cast_NodeVectorState",
        ) -> "_125.EntityVectorState":
            return self._parent._cast(_125.EntityVectorState)

        @property
        def node_scalar_state(
            self: "NodeVectorState._Cast_NodeVectorState",
        ) -> "_126.NodeScalarState":
            from mastapy.nodal_analysis.states import _126

            return self._parent._cast(_126.NodeScalarState)

        @property
        def node_vector_state(
            self: "NodeVectorState._Cast_NodeVectorState",
        ) -> "NodeVectorState":
            return self._parent

        def __getattr__(self: "NodeVectorState._Cast_NodeVectorState", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodeVectorState.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NodeVectorState._Cast_NodeVectorState":
        return self._Cast_NodeVectorState(self)
