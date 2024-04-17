"""RigidBar"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _145
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGID_BAR = python_net_import("SMT.MastaAPI.NodalAnalysis.NodalEntities", "RigidBar")

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _147


__docformat__ = "restructuredtext en"
__all__ = ("RigidBar",)


Self = TypeVar("Self", bound="RigidBar")


class RigidBar(_145.NodalComponent):
    """RigidBar

    This is a mastapy class.
    """

    TYPE = _RIGID_BAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RigidBar")

    class _Cast_RigidBar:
        """Special nested class for casting RigidBar to subclasses."""

        def __init__(self: "RigidBar._Cast_RigidBar", parent: "RigidBar"):
            self._parent = parent

        @property
        def nodal_component(self: "RigidBar._Cast_RigidBar") -> "_145.NodalComponent":
            return self._parent._cast(_145.NodalComponent)

        @property
        def nodal_entity(self: "RigidBar._Cast_RigidBar") -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def rigid_bar(self: "RigidBar._Cast_RigidBar") -> "RigidBar":
            return self._parent

        def __getattr__(self: "RigidBar._Cast_RigidBar", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RigidBar.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RigidBar._Cast_RigidBar":
        return self._Cast_RigidBar(self)
