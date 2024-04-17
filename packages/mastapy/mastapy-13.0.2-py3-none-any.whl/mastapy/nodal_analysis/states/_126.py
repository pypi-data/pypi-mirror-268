"""NodeScalarState"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.states import _127
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODE_SCALAR_STATE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.States", "NodeScalarState"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.states import _125


__docformat__ = "restructuredtext en"
__all__ = ("NodeScalarState",)


Self = TypeVar("Self", bound="NodeScalarState")


class NodeScalarState(_127.NodeVectorState):
    """NodeScalarState

    This is a mastapy class.
    """

    TYPE = _NODE_SCALAR_STATE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodeScalarState")

    class _Cast_NodeScalarState:
        """Special nested class for casting NodeScalarState to subclasses."""

        def __init__(
            self: "NodeScalarState._Cast_NodeScalarState", parent: "NodeScalarState"
        ):
            self._parent = parent

        @property
        def node_vector_state(
            self: "NodeScalarState._Cast_NodeScalarState",
        ) -> "_127.NodeVectorState":
            return self._parent._cast(_127.NodeVectorState)

        @property
        def entity_vector_state(
            self: "NodeScalarState._Cast_NodeScalarState",
        ) -> "_125.EntityVectorState":
            from mastapy.nodal_analysis.states import _125

            return self._parent._cast(_125.EntityVectorState)

        @property
        def node_scalar_state(
            self: "NodeScalarState._Cast_NodeScalarState",
        ) -> "NodeScalarState":
            return self._parent

        def __getattr__(self: "NodeScalarState._Cast_NodeScalarState", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodeScalarState.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NodeScalarState._Cast_NodeScalarState":
        return self._Cast_NodeScalarState(self)
