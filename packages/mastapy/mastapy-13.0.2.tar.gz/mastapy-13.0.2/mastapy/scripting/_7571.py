"""ApiVersion"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_API_VERSION = python_net_import("SMT.MastaAPIUtility.Scripting", "ApiVersion")


__docformat__ = "restructuredtext en"
__all__ = ("ApiVersion",)


Self = TypeVar("Self", bound="ApiVersion")


class ApiVersion:
    """ApiVersion

    This is a mastapy class.
    """

    TYPE = _API_VERSION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ApiVersion")

    class _Cast_ApiVersion:
        """Special nested class for casting ApiVersion to subclasses."""

        def __init__(self: "ApiVersion._Cast_ApiVersion", parent: "ApiVersion"):
            self._parent = parent

        @property
        def api_version(self: "ApiVersion._Cast_ApiVersion") -> "ApiVersion":
            return self._parent

        def __getattr__(self: "ApiVersion._Cast_ApiVersion", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ApiVersion.TYPE"):
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
    def file_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FileName

        if temp is None:
            return ""

        return temp

    @property
    def assembly_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyName

        if temp is None:
            return ""

        return temp

    @property
    def assembly_name_without_version(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyNameWithoutVersion

        if temp is None:
            return ""

        return temp

    @property
    def file_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilePath

        if temp is None:
            return ""

        return temp

    @property
    def customer_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CustomerName

        if temp is None:
            return ""

        return temp

    @enforce_parameter_types
    def compare_to(self: Self, other: "ApiVersion") -> "int":
        """int

        Args:
            other (mastapy.scripting.ApiVersion)
        """
        method_result = self.wrapped.CompareTo(other.wrapped if other else None)
        return method_result

    def to_string(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.ToString()
        return method_result

    @property
    def cast_to(self: Self) -> "ApiVersion._Cast_ApiVersion":
        return self._Cast_ApiVersion(self)
