"""PIDControlNodalComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _145
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PID_CONTROL_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "PIDControlNodalComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _147


__docformat__ = "restructuredtext en"
__all__ = ("PIDControlNodalComponent",)


Self = TypeVar("Self", bound="PIDControlNodalComponent")


class PIDControlNodalComponent(_145.NodalComponent):
    """PIDControlNodalComponent

    This is a mastapy class.
    """

    TYPE = _PID_CONTROL_NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PIDControlNodalComponent")

    class _Cast_PIDControlNodalComponent:
        """Special nested class for casting PIDControlNodalComponent to subclasses."""

        def __init__(
            self: "PIDControlNodalComponent._Cast_PIDControlNodalComponent",
            parent: "PIDControlNodalComponent",
        ):
            self._parent = parent

        @property
        def nodal_component(
            self: "PIDControlNodalComponent._Cast_PIDControlNodalComponent",
        ) -> "_145.NodalComponent":
            return self._parent._cast(_145.NodalComponent)

        @property
        def nodal_entity(
            self: "PIDControlNodalComponent._Cast_PIDControlNodalComponent",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def pid_control_nodal_component(
            self: "PIDControlNodalComponent._Cast_PIDControlNodalComponent",
        ) -> "PIDControlNodalComponent":
            return self._parent

        def __getattr__(
            self: "PIDControlNodalComponent._Cast_PIDControlNodalComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PIDControlNodalComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PIDControlNodalComponent._Cast_PIDControlNodalComponent":
        return self._Cast_PIDControlNodalComponent(self)
