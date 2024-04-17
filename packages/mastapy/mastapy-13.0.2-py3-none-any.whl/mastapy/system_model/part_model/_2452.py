"""ComponentsConnectedResult"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENTS_CONNECTED_RESULT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "ComponentsConnectedResult"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453


__docformat__ = "restructuredtext en"
__all__ = ("ComponentsConnectedResult",)


Self = TypeVar("Self", bound="ComponentsConnectedResult")


class ComponentsConnectedResult(_0.APIBase):
    """ComponentsConnectedResult

    This is a mastapy class.
    """

    TYPE = _COMPONENTS_CONNECTED_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentsConnectedResult")

    class _Cast_ComponentsConnectedResult:
        """Special nested class for casting ComponentsConnectedResult to subclasses."""

        def __init__(
            self: "ComponentsConnectedResult._Cast_ComponentsConnectedResult",
            parent: "ComponentsConnectedResult",
        ):
            self._parent = parent

        @property
        def components_connected_result(
            self: "ComponentsConnectedResult._Cast_ComponentsConnectedResult",
        ) -> "ComponentsConnectedResult":
            return self._parent

        def __getattr__(
            self: "ComponentsConnectedResult._Cast_ComponentsConnectedResult", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentsConnectedResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_failed(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionFailed

        if temp is None:
            return False

        return temp

    @property
    def failure_message(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FailureMessage

        if temp is None:
            return ""

        return temp

    @property
    def was_connection_created(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WasConnectionCreated

        if temp is None:
            return False

        return temp

    @property
    def created_socket_connection(self: Self) -> "_2453.ConnectedSockets":
        """mastapy.system_model.part_model.ConnectedSockets

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CreatedSocketConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentsConnectedResult._Cast_ComponentsConnectedResult":
        return self._Cast_ComponentsConnectedResult(self)
