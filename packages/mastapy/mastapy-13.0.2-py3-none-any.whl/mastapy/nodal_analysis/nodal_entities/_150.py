"""SimpleBar"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _154
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIMPLE_BAR = python_net_import("SMT.MastaAPI.NodalAnalysis.NodalEntities", "SimpleBar")

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _136, _146, _147


__docformat__ = "restructuredtext en"
__all__ = ("SimpleBar",)


Self = TypeVar("Self", bound="SimpleBar")


class SimpleBar(_154.TwoBodyConnectionNodalComponent):
    """SimpleBar

    This is a mastapy class.
    """

    TYPE = _SIMPLE_BAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SimpleBar")

    class _Cast_SimpleBar:
        """Special nested class for casting SimpleBar to subclasses."""

        def __init__(self: "SimpleBar._Cast_SimpleBar", parent: "SimpleBar"):
            self._parent = parent

        @property
        def two_body_connection_nodal_component(
            self: "SimpleBar._Cast_SimpleBar",
        ) -> "_154.TwoBodyConnectionNodalComponent":
            return self._parent._cast(_154.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(
            self: "SimpleBar._Cast_SimpleBar",
        ) -> "_136.ComponentNodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _136

            return self._parent._cast(_136.ComponentNodalComposite)

        @property
        def nodal_composite(self: "SimpleBar._Cast_SimpleBar") -> "_146.NodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _146

            return self._parent._cast(_146.NodalComposite)

        @property
        def nodal_entity(self: "SimpleBar._Cast_SimpleBar") -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def simple_bar(self: "SimpleBar._Cast_SimpleBar") -> "SimpleBar":
            return self._parent

        def __getattr__(self: "SimpleBar._Cast_SimpleBar", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SimpleBar.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SimpleBar._Cast_SimpleBar":
        return self._Cast_SimpleBar(self)
