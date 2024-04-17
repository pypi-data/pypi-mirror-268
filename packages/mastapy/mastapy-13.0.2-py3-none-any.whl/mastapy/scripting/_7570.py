"""ApiEnumForAttribute"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_API_ENUM_FOR_ATTRIBUTE = python_net_import(
    "SMT.MastaAPIUtility.Scripting", "ApiEnumForAttribute"
)


__docformat__ = "restructuredtext en"
__all__ = ("ApiEnumForAttribute",)


Self = TypeVar("Self", bound="ApiEnumForAttribute")


class ApiEnumForAttribute:
    """ApiEnumForAttribute

    This is a mastapy class.
    """

    TYPE = _API_ENUM_FOR_ATTRIBUTE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ApiEnumForAttribute")

    class _Cast_ApiEnumForAttribute:
        """Special nested class for casting ApiEnumForAttribute to subclasses."""

        def __init__(
            self: "ApiEnumForAttribute._Cast_ApiEnumForAttribute",
            parent: "ApiEnumForAttribute",
        ):
            self._parent = parent

        @property
        def api_enum_for_attribute(
            self: "ApiEnumForAttribute._Cast_ApiEnumForAttribute",
        ) -> "ApiEnumForAttribute":
            return self._parent

        def __getattr__(
            self: "ApiEnumForAttribute._Cast_ApiEnumForAttribute", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ApiEnumForAttribute.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1
        self._freeze()

    __frozen = False

    def __setattr__(self: Self, attr, value):
        prop = getattr(self.__class__, attr, None)
        if isinstance(prop, property):
            prop.fset(self, value)
        else:
            if self.__frozen and attr not in self.__dict__:
                raise AttributeError(
                    ("Attempted to set unknown " "attribute: '{}'".format(attr))
                ) from None

            super().__setattr__(attr, value)

    def __delattr__(self: Self, name: str):
        raise AttributeError(
            "Cannot delete the attributes of a mastapy object."
        ) from None

    def _freeze(self: Self):
        self.__frozen = True

    @property
    def wrapped_enum(self: Self) -> "type":
        """type

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WrappedEnum

        if temp is None:
            return None

        return temp

    @staticmethod
    @enforce_parameter_types
    def get_wrapped_enum_from(api_enum_type: "type") -> "type":
        """type

        Args:
            api_enum_type (type)
        """
        method_result = ApiEnumForAttribute.TYPE.GetWrappedEnumFrom(api_enum_type)
        return method_result

    @property
    def cast_to(self: Self) -> "ApiEnumForAttribute._Cast_ApiEnumForAttribute":
        return self._Cast_ApiEnumForAttribute(self)
