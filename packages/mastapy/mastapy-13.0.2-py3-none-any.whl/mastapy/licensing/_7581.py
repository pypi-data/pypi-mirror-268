"""ModuleDetails"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODULE_DETAILS = python_net_import("SMT.MastaAPIUtility.Licensing", "ModuleDetails")


__docformat__ = "restructuredtext en"
__all__ = ("ModuleDetails",)


Self = TypeVar("Self", bound="ModuleDetails")


class ModuleDetails:
    """ModuleDetails

    This is a mastapy class.
    """

    TYPE = _MODULE_DETAILS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModuleDetails")

    class _Cast_ModuleDetails:
        """Special nested class for casting ModuleDetails to subclasses."""

        def __init__(
            self: "ModuleDetails._Cast_ModuleDetails", parent: "ModuleDetails"
        ):
            self._parent = parent

        @property
        def module_details(
            self: "ModuleDetails._Cast_ModuleDetails",
        ) -> "ModuleDetails":
            return self._parent

        def __getattr__(self: "ModuleDetails._Cast_ModuleDetails", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModuleDetails.TYPE"):
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
    def is_licensed(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLicensed

        if temp is None:
            return False

        return temp

    @property
    def expiry_date(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExpiryDate

        if temp is None:
            return ""

        return temp

    @property
    def user_count(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserCount

        if temp is None:
            return ""

        return temp

    @property
    def maximum_users(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumUsers

        if temp is None:
            return 0

        return temp

    @property
    def code(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Code

        if temp is None:
            return ""

        return temp

    @property
    def description(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Description

        if temp is None:
            return ""

        return temp

    @property
    def scope(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Scope

        if temp is None:
            return ""

        return temp

    def to_string(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.ToString()
        return method_result

    @property
    def cast_to(self: Self) -> "ModuleDetails._Cast_ModuleDetails":
        return self._Cast_ModuleDetails(self)
