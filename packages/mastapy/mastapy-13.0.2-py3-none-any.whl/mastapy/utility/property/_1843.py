"""DeletableCollectionMember"""

from __future__ import annotations

from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DELETABLE_COLLECTION_MEMBER = python_net_import(
    "SMT.MastaAPI.Utility.Property", "DeletableCollectionMember"
)


__docformat__ = "restructuredtext en"
__all__ = ("DeletableCollectionMember",)


Self = TypeVar("Self", bound="DeletableCollectionMember")
T = TypeVar("T")


class DeletableCollectionMember(_0.APIBase, Generic[T]):
    """DeletableCollectionMember

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _DELETABLE_COLLECTION_MEMBER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DeletableCollectionMember")

    class _Cast_DeletableCollectionMember:
        """Special nested class for casting DeletableCollectionMember to subclasses."""

        def __init__(
            self: "DeletableCollectionMember._Cast_DeletableCollectionMember",
            parent: "DeletableCollectionMember",
        ):
            self._parent = parent

        @property
        def deletable_collection_member(
            self: "DeletableCollectionMember._Cast_DeletableCollectionMember",
        ) -> "DeletableCollectionMember":
            return self._parent

        def __getattr__(
            self: "DeletableCollectionMember._Cast_DeletableCollectionMember", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DeletableCollectionMember.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def item(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Item

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @property
    def cast_to(
        self: Self,
    ) -> "DeletableCollectionMember._Cast_DeletableCollectionMember":
        return self._Cast_DeletableCollectionMember(self)
