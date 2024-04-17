"""LicenceServerDetails"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LICENCE_SERVER_DETAILS = python_net_import(
    "SMT.MastaAPIUtility.Licensing", "LicenceServerDetails"
)


__docformat__ = "restructuredtext en"
__all__ = ("LicenceServerDetails",)


Self = TypeVar("Self", bound="LicenceServerDetails")


class LicenceServerDetails:
    """LicenceServerDetails

    This is a mastapy class.
    """

    TYPE = _LICENCE_SERVER_DETAILS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LicenceServerDetails")

    class _Cast_LicenceServerDetails:
        """Special nested class for casting LicenceServerDetails to subclasses."""

        def __init__(
            self: "LicenceServerDetails._Cast_LicenceServerDetails",
            parent: "LicenceServerDetails",
        ):
            self._parent = parent

        @property
        def licence_server_details(
            self: "LicenceServerDetails._Cast_LicenceServerDetails",
        ) -> "LicenceServerDetails":
            return self._parent

        def __getattr__(
            self: "LicenceServerDetails._Cast_LicenceServerDetails", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LicenceServerDetails.TYPE" = None):
        self.wrapped = (
            instance_to_wrap if instance_to_wrap else LicenceServerDetails.TYPE()
        )
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
    def ip(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Ip

        if temp is None:
            return ""

        return temp

    @ip.setter
    @enforce_parameter_types
    def ip(self: Self, value: "str"):
        self.wrapped.Ip = str(value) if value is not None else ""

    @property
    def port(self: Self) -> "int":
        """int"""
        temp = self.wrapped.Port

        if temp is None:
            return 0

        return temp

    @port.setter
    @enforce_parameter_types
    def port(self: Self, value: "int"):
        self.wrapped.Port = int(value) if value is not None else 0

    @property
    def web_port(self: Self) -> "int":
        """int"""
        temp = self.wrapped.WebPort

        if temp is None:
            return 0

        return temp

    @web_port.setter
    @enforce_parameter_types
    def web_port(self: Self, value: "int"):
        self.wrapped.WebPort = int(value) if value is not None else 0

    @property
    def licence_groups_ip(self: Self) -> "str":
        """str"""
        temp = self.wrapped.LicenceGroupsIp

        if temp is None:
            return ""

        return temp

    @licence_groups_ip.setter
    @enforce_parameter_types
    def licence_groups_ip(self: Self, value: "str"):
        self.wrapped.LicenceGroupsIp = str(value) if value is not None else ""

    @property
    def licence_groups_port(self: Self) -> "int":
        """int"""
        temp = self.wrapped.LicenceGroupsPort

        if temp is None:
            return 0

        return temp

    @licence_groups_port.setter
    @enforce_parameter_types
    def licence_groups_port(self: Self, value: "int"):
        self.wrapped.LicenceGroupsPort = int(value) if value is not None else 0

    def has_ip(self: Self) -> "bool":
        """bool"""
        method_result = self.wrapped.HasIp()
        return method_result

    def has_port(self: Self) -> "bool":
        """bool"""
        method_result = self.wrapped.HasPort()
        return method_result

    def has_web_port(self: Self) -> "bool":
        """bool"""
        method_result = self.wrapped.HasWebPort()
        return method_result

    def has_licence_groups_ip(self: Self) -> "bool":
        """bool"""
        method_result = self.wrapped.HasLicenceGroupsIp()
        return method_result

    def has_licence_groups_port(self: Self) -> "bool":
        """bool"""
        method_result = self.wrapped.HasLicenceGroupsPort()
        return method_result

    @property
    def cast_to(self: Self) -> "LicenceServerDetails._Cast_LicenceServerDetails":
        return self._Cast_LicenceServerDetails(self)
