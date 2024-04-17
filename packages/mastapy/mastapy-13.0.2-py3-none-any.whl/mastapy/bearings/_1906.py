"""SKFSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.utility import _1601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SKF_SETTINGS = python_net_import("SMT.MastaAPI.Bearings", "SKFSettings")

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import _2102
    from mastapy.utility import _1602


__docformat__ = "restructuredtext en"
__all__ = ("SKFSettings",)


Self = TypeVar("Self", bound="SKFSettings")


class SKFSettings(_1601.PerMachineSettings):
    """SKFSettings

    This is a mastapy class.
    """

    TYPE = _SKF_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SKFSettings")

    class _Cast_SKFSettings:
        """Special nested class for casting SKFSettings to subclasses."""

        def __init__(self: "SKFSettings._Cast_SKFSettings", parent: "SKFSettings"):
            self._parent = parent

        @property
        def per_machine_settings(
            self: "SKFSettings._Cast_SKFSettings",
        ) -> "_1601.PerMachineSettings":
            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def persistent_singleton(
            self: "SKFSettings._Cast_SKFSettings",
        ) -> "_1602.PersistentSingleton":
            from mastapy.utility import _1602

            return self._parent._cast(_1602.PersistentSingleton)

        @property
        def skf_settings(self: "SKFSettings._Cast_SKFSettings") -> "SKFSettings":
            return self._parent

        def __getattr__(self: "SKFSettings._Cast_SKFSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SKFSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def enable_skf_module(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.EnableSKFModule

        if temp is None:
            return False

        return temp

    @enable_skf_module.setter
    @enforce_parameter_types
    def enable_skf_module(self: Self, value: "bool"):
        self.wrapped.EnableSKFModule = bool(value) if value is not None else False

    @property
    def log_file_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LogFilePath

        if temp is None:
            return ""

        return temp

    @property
    def log_http_requests(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LogHTTPRequests

        if temp is None:
            return False

        return temp

    @log_http_requests.setter
    @enforce_parameter_types
    def log_http_requests(self: Self, value: "bool"):
        self.wrapped.LogHTTPRequests = bool(value) if value is not None else False

    @property
    def skf_authentication(self: Self) -> "_2102.SKFAuthentication":
        """mastapy.bearings.bearing_results.rolling.skf_module.SKFAuthentication

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFAuthentication

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SKFSettings._Cast_SKFSettings":
        return self._Cast_SKFSettings(self)
