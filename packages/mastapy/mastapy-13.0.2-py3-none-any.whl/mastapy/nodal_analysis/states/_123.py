"""ElementScalarState"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.states import _124
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_SCALAR_STATE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.States", "ElementScalarState"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.states import _125


__docformat__ = "restructuredtext en"
__all__ = ("ElementScalarState",)


Self = TypeVar("Self", bound="ElementScalarState")


class ElementScalarState(_124.ElementVectorState):
    """ElementScalarState

    This is a mastapy class.
    """

    TYPE = _ELEMENT_SCALAR_STATE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementScalarState")

    class _Cast_ElementScalarState:
        """Special nested class for casting ElementScalarState to subclasses."""

        def __init__(
            self: "ElementScalarState._Cast_ElementScalarState",
            parent: "ElementScalarState",
        ):
            self._parent = parent

        @property
        def element_vector_state(
            self: "ElementScalarState._Cast_ElementScalarState",
        ) -> "_124.ElementVectorState":
            return self._parent._cast(_124.ElementVectorState)

        @property
        def entity_vector_state(
            self: "ElementScalarState._Cast_ElementScalarState",
        ) -> "_125.EntityVectorState":
            from mastapy.nodal_analysis.states import _125

            return self._parent._cast(_125.EntityVectorState)

        @property
        def element_scalar_state(
            self: "ElementScalarState._Cast_ElementScalarState",
        ) -> "ElementScalarState":
            return self._parent

        def __getattr__(self: "ElementScalarState._Cast_ElementScalarState", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementScalarState.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ElementScalarState._Cast_ElementScalarState":
        return self._Cast_ElementScalarState(self)
