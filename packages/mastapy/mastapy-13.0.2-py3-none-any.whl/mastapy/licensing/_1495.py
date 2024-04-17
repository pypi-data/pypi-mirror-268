"""LicenceServer"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Iterable

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.class_property import classproperty
from mastapy._internal.python_net import python_net_import
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_LICENCE_SERVER = python_net_import("SMT.MastaAPI.Licensing", "LicenceServer")

if TYPE_CHECKING:
    from mastapy.licensing import _7580, _7581, _7582


__docformat__ = "restructuredtext en"
__all__ = ("LicenceServer",)


Self = TypeVar("Self", bound="LicenceServer")


class LicenceServer:
    """LicenceServer

    This is a mastapy class.
    """

    TYPE = _LICENCE_SERVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LicenceServer")

    class _Cast_LicenceServer:
        """Special nested class for casting LicenceServer to subclasses."""

        def __init__(
            self: "LicenceServer._Cast_LicenceServer", parent: "LicenceServer"
        ):
            self._parent = parent

        @property
        def licence_server(
            self: "LicenceServer._Cast_LicenceServer",
        ) -> "LicenceServer":
            return self._parent

        def __getattr__(self: "LicenceServer._Cast_LicenceServer", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LicenceServer.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @classproperty
    def server_address(cls) -> "str":
        """str"""
        temp = LicenceServer.TYPE.ServerAddress

        if temp is None:
            return ""

        return temp

    @server_address.setter
    @enforce_parameter_types
    def server_address(cls, value: "str"):
        LicenceServer.TYPE.ServerAddress = str(value) if value is not None else ""

    @classproperty
    def server_port(cls) -> "int":
        """int"""
        temp = LicenceServer.TYPE.ServerPort

        if temp is None:
            return 0

        return temp

    @server_port.setter
    @enforce_parameter_types
    def server_port(cls, value: "int"):
        LicenceServer.TYPE.ServerPort = int(value) if value is not None else 0

    @classproperty
    def web_server_port(cls) -> "int":
        """int"""
        temp = LicenceServer.TYPE.WebServerPort

        if temp is None:
            return 0

        return temp

    @web_server_port.setter
    @enforce_parameter_types
    def web_server_port(cls, value: "int"):
        LicenceServer.TYPE.WebServerPort = int(value) if value is not None else 0

    @staticmethod
    @enforce_parameter_types
    def update_server_settings(server_details: "_7580.LicenceServerDetails"):
        """Method does not return.

        Args:
            server_details (mastapy.licensing.LicenceServerDetails)
        """
        LicenceServer.TYPE.UpdateServerSettings(
            server_details.wrapped if server_details else None
        )

    @staticmethod
    def get_server_settings() -> "_7580.LicenceServerDetails":
        """mastapy.licensing.LicenceServerDetails"""
        method_result = LicenceServer.TYPE.GetServerSettings()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @staticmethod
    @enforce_parameter_types
    def request_module(module_code: "str") -> "bool":
        """bool

        Args:
            module_code (str)
        """
        module_code = str(module_code)
        method_result = LicenceServer.TYPE.RequestModule(
            module_code if module_code else ""
        )
        return method_result

    @staticmethod
    @enforce_parameter_types
    def request_module_and_prerequisites(module_code: "str") -> "bool":
        """bool

        Args:
            module_code (str)
        """
        module_code = str(module_code)
        method_result = LicenceServer.TYPE.RequestModuleAndPrerequisites(
            module_code if module_code else ""
        )
        return method_result

    @staticmethod
    @enforce_parameter_types
    def request_modules(module_codes: "List[str]") -> "bool":
        """bool

        Args:
            module_codes (List[str])
        """
        module_codes = conversion.to_list_any(module_codes)
        method_result = LicenceServer.TYPE.RequestModules(module_codes)
        return method_result

    @staticmethod
    @enforce_parameter_types
    def get_module_prerequisites(module_code: "str") -> "Iterable[str]":
        """Iterable[str]

        Args:
            module_code (str)
        """
        module_code = str(module_code)
        return conversion.pn_to_mp_objects_in_iterable(
            LicenceServer.TYPE.GetModulePrerequisites(
                module_code if module_code else ""
            ),
            str,
        )

    @staticmethod
    def get_requested_module_codes() -> "Iterable[str]":
        """Iterable[str]"""
        return conversion.pn_to_mp_objects_in_iterable(
            LicenceServer.TYPE.GetRequestedModuleCodes(), str
        )

    @staticmethod
    @enforce_parameter_types
    def remove_module(module_code: "str"):
        """Method does not return.

        Args:
            module_code (str)
        """
        module_code = str(module_code)
        LicenceServer.TYPE.RemoveModule(module_code if module_code else "")

    @staticmethod
    @enforce_parameter_types
    def remove_modules(module_codes: "List[str]"):
        """Method does not return.

        Args:
            module_codes (List[str])
        """
        module_codes = conversion.to_list_any(module_codes)
        LicenceServer.TYPE.RemoveModules(module_codes)

    @staticmethod
    def get_licensed_module_details() -> "Iterable[_7581.ModuleDetails]":
        """Iterable[mastapy.licensing.ModuleDetails]"""
        return conversion.pn_to_mp_objects_in_iterable(
            LicenceServer.TYPE.GetLicensedModuleDetails()
        )

    @staticmethod
    def get_available_module_details() -> "Iterable[_7581.ModuleDetails]":
        """Iterable[mastapy.licensing.ModuleDetails]"""
        return conversion.pn_to_mp_objects_in_iterable(
            LicenceServer.TYPE.GetAvailableModuleDetails()
        )

    @staticmethod
    def get_requested_module_statuses() -> "Iterable[_7582.ModuleLicenceStatus]":
        """Iterable[mastapy.licensing.ModuleLicenceStatus]"""
        return conversion.pn_to_mp_objects_in_iterable(
            LicenceServer.TYPE.GetRequestedModuleStatuses()
        )

    @property
    def cast_to(self: Self) -> "LicenceServer._Cast_LicenceServer":
        return self._Cast_LicenceServer(self)
