"""NamedTuple1"""

from __future__ import annotations

from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_TUPLE_1 = python_net_import("SMT.MastaAPI.Utility.Generics", "NamedTuple1")


__docformat__ = "restructuredtext en"
__all__ = ("NamedTuple1",)


Self = TypeVar("Self", bound="NamedTuple1")
T1 = TypeVar("T1")


class NamedTuple1(_0.APIBase, Generic[T1]):
    """NamedTuple1

    This is a mastapy class.

    Generic Types:
        T1
    """

    TYPE = _NAMED_TUPLE_1
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedTuple1")

    class _Cast_NamedTuple1:
        """Special nested class for casting NamedTuple1 to subclasses."""

        def __init__(self: "NamedTuple1._Cast_NamedTuple1", parent: "NamedTuple1"):
            self._parent = parent

        @property
        def named_tuple_1(self: "NamedTuple1._Cast_NamedTuple1") -> "NamedTuple1":
            return self._parent

        def __getattr__(self: "NamedTuple1._Cast_NamedTuple1", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedTuple1.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def item_1(self: Self) -> "T1":
        """T1

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Item1

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "NamedTuple1._Cast_NamedTuple1":
        return self._Cast_NamedTuple1(self)
