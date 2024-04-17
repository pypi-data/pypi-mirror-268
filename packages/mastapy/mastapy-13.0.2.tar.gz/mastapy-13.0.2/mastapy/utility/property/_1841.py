"""EnumWithSelectedValue"""

from __future__ import annotations

from typing import TypeVar, List, Generic

from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _7561
from mastapy.utility.property import _7587
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue",)


Self = TypeVar("Self", bound="EnumWithSelectedValue")
TAPIEnum = TypeVar("TAPIEnum")


class EnumWithSelectedValue(
    _7561.MarshalByRefObjectPermanent, _7587.IEnumWithSelectedValue, Generic[TAPIEnum]
):
    """EnumWithSelectedValue

    This is a mastapy class.

    Generic Types:
        TAPIEnum
    """

    TYPE = _ENUM_WITH_SELECTED_VALUE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EnumWithSelectedValue")

    class _Cast_EnumWithSelectedValue:
        """Special nested class for casting EnumWithSelectedValue to subclasses."""

        def __init__(
            self: "EnumWithSelectedValue._Cast_EnumWithSelectedValue",
            parent: "EnumWithSelectedValue",
        ):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(
            self: "EnumWithSelectedValue._Cast_EnumWithSelectedValue",
        ) -> "_7561.MarshalByRefObjectPermanent":
            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def enum_with_selected_value(
            self: "EnumWithSelectedValue._Cast_EnumWithSelectedValue",
        ) -> "EnumWithSelectedValue":
            return self._parent

        def __getattr__(
            self: "EnumWithSelectedValue._Cast_EnumWithSelectedValue", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EnumWithSelectedValue.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_value(self: Self) -> "TAPIEnum":
        """TAPIEnum

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def available_values(self: Self) -> "List[TAPIEnum]":
        """List[TAPIEnum]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "EnumWithSelectedValue._Cast_EnumWithSelectedValue":
        return self._Cast_EnumWithSelectedValue(self)
