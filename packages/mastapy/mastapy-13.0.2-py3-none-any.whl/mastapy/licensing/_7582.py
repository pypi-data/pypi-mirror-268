"""ModuleLicenceStatus"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODULE_LICENCE_STATUS = python_net_import(
    "SMT.MastaAPIUtility.Licensing", "ModuleLicenceStatus"
)


__docformat__ = "restructuredtext en"
__all__ = ("ModuleLicenceStatus",)


Self = TypeVar("Self", bound="ModuleLicenceStatus")


class ModuleLicenceStatus:
    """ModuleLicenceStatus

    This is a mastapy class.
    """

    TYPE = _MODULE_LICENCE_STATUS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModuleLicenceStatus")

    class _Cast_ModuleLicenceStatus:
        """Special nested class for casting ModuleLicenceStatus to subclasses."""

        def __init__(
            self: "ModuleLicenceStatus._Cast_ModuleLicenceStatus",
            parent: "ModuleLicenceStatus",
        ):
            self._parent = parent

        @property
        def module_licence_status(
            self: "ModuleLicenceStatus._Cast_ModuleLicenceStatus",
        ) -> "ModuleLicenceStatus":
            return self._parent

        def __getattr__(
            self: "ModuleLicenceStatus._Cast_ModuleLicenceStatus", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModuleLicenceStatus.TYPE"):
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
    def module_code(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModuleCode

        if temp is None:
            return ""

        return temp

    @property
    def module_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModuleName

        if temp is None:
            return ""

        return temp

    @property
    def status(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return ""

        return temp

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

    def to_string(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.ToString()
        return method_result

    @property
    def cast_to(self: Self) -> "ModuleLicenceStatus._Cast_ModuleLicenceStatus":
        return self._Cast_ModuleLicenceStatus(self)
