"""NamedTuple4"""

from __future__ import annotations

from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_TUPLE_4 = python_net_import("SMT.MastaAPI.Utility.Generics", "NamedTuple4")


__docformat__ = "restructuredtext en"
__all__ = ("NamedTuple4",)


Self = TypeVar("Self", bound="NamedTuple4")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")


class NamedTuple4(_0.APIBase, Generic[T1, T2, T3, T4]):
    """NamedTuple4

    This is a mastapy class.

    Generic Types:
        T1
        T2
        T3
        T4
    """

    TYPE = _NAMED_TUPLE_4
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedTuple4")

    class _Cast_NamedTuple4:
        """Special nested class for casting NamedTuple4 to subclasses."""

        def __init__(self: "NamedTuple4._Cast_NamedTuple4", parent: "NamedTuple4"):
            self._parent = parent

        @property
        def named_tuple_4(self: "NamedTuple4._Cast_NamedTuple4") -> "NamedTuple4":
            return self._parent

        def __getattr__(self: "NamedTuple4._Cast_NamedTuple4", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedTuple4.TYPE"):
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
    def item_3(self: Self) -> "T3":
        """T3

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Item3

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def item_4(self: Self) -> "T4":
        """T4

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Item4

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
    def cast_to(self: Self) -> "NamedTuple4._Cast_NamedTuple4":
        return self._Cast_NamedTuple4(self)
