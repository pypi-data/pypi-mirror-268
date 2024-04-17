"""LocalNodeInfo"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOCAL_NODE_INFO = python_net_import("SMT.MastaAPI.NodalAnalysis", "LocalNodeInfo")


__docformat__ = "restructuredtext en"
__all__ = ("LocalNodeInfo",)


Self = TypeVar("Self", bound="LocalNodeInfo")


class LocalNodeInfo(_0.APIBase):
    """LocalNodeInfo

    This is a mastapy class.
    """

    TYPE = _LOCAL_NODE_INFO
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LocalNodeInfo")

    class _Cast_LocalNodeInfo:
        """Special nested class for casting LocalNodeInfo to subclasses."""

        def __init__(
            self: "LocalNodeInfo._Cast_LocalNodeInfo", parent: "LocalNodeInfo"
        ):
            self._parent = parent

        @property
        def local_node_info(
            self: "LocalNodeInfo._Cast_LocalNodeInfo",
        ) -> "LocalNodeInfo":
            return self._parent

        def __getattr__(self: "LocalNodeInfo._Cast_LocalNodeInfo", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LocalNodeInfo.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def first_degrees_of_freedom_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FirstDegreesOfFreedomIndex

        if temp is None:
            return 0

        return temp

    @property
    def number_of_degrees_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self: Self) -> "LocalNodeInfo._Cast_LocalNodeInfo":
        return self._Cast_LocalNodeInfo(self)
