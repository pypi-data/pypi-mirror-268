"""ScriptedPropertyNameAttribute"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCRIPTED_PROPERTY_NAME_ATTRIBUTE = python_net_import(
    "SMT.MastaAPIUtility", "ScriptedPropertyNameAttribute"
)


__docformat__ = "restructuredtext en"
__all__ = ("ScriptedPropertyNameAttribute",)


Self = TypeVar("Self", bound="ScriptedPropertyNameAttribute")


class ScriptedPropertyNameAttribute:
    """ScriptedPropertyNameAttribute

    This is a mastapy class.
    """

    TYPE = _SCRIPTED_PROPERTY_NAME_ATTRIBUTE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ScriptedPropertyNameAttribute")

    class _Cast_ScriptedPropertyNameAttribute:
        """Special nested class for casting ScriptedPropertyNameAttribute to subclasses."""

        def __init__(
            self: "ScriptedPropertyNameAttribute._Cast_ScriptedPropertyNameAttribute",
            parent: "ScriptedPropertyNameAttribute",
        ):
            self._parent = parent

        @property
        def scripted_property_name_attribute(
            self: "ScriptedPropertyNameAttribute._Cast_ScriptedPropertyNameAttribute",
        ) -> "ScriptedPropertyNameAttribute":
            return self._parent

        def __getattr__(
            self: "ScriptedPropertyNameAttribute._Cast_ScriptedPropertyNameAttribute",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ScriptedPropertyNameAttribute.TYPE"):
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
    def property_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertyName

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ScriptedPropertyNameAttribute._Cast_ScriptedPropertyNameAttribute":
        return self._Cast_ScriptedPropertyNameAttribute(self)
