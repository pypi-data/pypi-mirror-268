"""NamedTuple2"""

from __future__ import annotations

from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_TUPLE_2 = python_net_import("SMT.MastaAPI.Utility.Generics", "NamedTuple2")


__docformat__ = "restructuredtext en"
__all__ = ("NamedTuple2",)


Self = TypeVar("Self", bound="NamedTuple2")
T1 = TypeVar("T1")
T2 = TypeVar("T2")


class NamedTuple2(_0.APIBase, Generic[T1, T2]):
    """NamedTuple2

    This is a mastapy class.

    Generic Types:
        T1
        T2
    """

    TYPE = _NAMED_TUPLE_2
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedTuple2")

    class _Cast_NamedTuple2:
        """Special nested class for casting NamedTuple2 to subclasses."""

        def __init__(self: "NamedTuple2._Cast_NamedTuple2", parent: "NamedTuple2"):
            self._parent = parent

        @property
        def named_tuple_2(self: "NamedTuple2._Cast_NamedTuple2") -> "NamedTuple2":
            return self._parent

        def __getattr__(self: "NamedTuple2._Cast_NamedTuple2", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedTuple2.TYPE"):
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
    def item_2(self: Self) -> "T2":
        """T2

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Item2

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
    def cast_to(self: Self) -> "NamedTuple2._Cast_NamedTuple2":
        return self._Cast_NamedTuple2(self)
