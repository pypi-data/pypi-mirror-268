"""DatabaseConnectionSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASE_CONNECTION_SETTINGS = python_net_import(
    "SMT.MastaAPI.Utility.Databases", "DatabaseConnectionSettings"
)


__docformat__ = "restructuredtext en"
__all__ = ("DatabaseConnectionSettings",)


Self = TypeVar("Self", bound="DatabaseConnectionSettings")


class DatabaseConnectionSettings(_0.APIBase):
    """DatabaseConnectionSettings

    This is a mastapy class.
    """

    TYPE = _DATABASE_CONNECTION_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatabaseConnectionSettings")

    class _Cast_DatabaseConnectionSettings:
        """Special nested class for casting DatabaseConnectionSettings to subclasses."""

        def __init__(
            self: "DatabaseConnectionSettings._Cast_DatabaseConnectionSettings",
            parent: "DatabaseConnectionSettings",
        ):
            self._parent = parent

        @property
        def database_connection_settings(
            self: "DatabaseConnectionSettings._Cast_DatabaseConnectionSettings",
        ) -> "DatabaseConnectionSettings":
            return self._parent

        def __getattr__(
            self: "DatabaseConnectionSettings._Cast_DatabaseConnectionSettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatabaseConnectionSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def can_use_local_db(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CanUseLocalDB

        if temp is None:
            return False

        return temp

    @property
    def display_sql_connection_integrated_security(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplaySQLConnectionIntegratedSecurity

        if temp is None:
            return False

        return temp

    @property
    def force_use_of_local_db2012(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceUseOfLocalDB2012

        if temp is None:
            return False

        return temp

    @property
    def is_local_db_path_specified(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLocalDBPathSpecified

        if temp is None:
            return False

        return temp

    @property
    def local_db_file_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalDBFilePath

        if temp is None:
            return ""

        return temp

    @property
    def network_connection_string(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NetworkConnectionString

        if temp is None:
            return ""

        return temp

    @property
    def sql_connection_db_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SQLConnectionDbName

        if temp is None:
            return ""

        return temp

    @property
    def sql_connection_integrated_security(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SQLConnectionIntegratedSecurity

        if temp is None:
            return False

        return temp

    @property
    def sql_connection_server_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SQLConnectionServerName

        if temp is None:
            return ""

        return temp

    @property
    def sql_connection_user_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SQLConnectionUserName

        if temp is None:
            return ""

        return temp

    @property
    def specified_local_db_file_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecifiedLocalDBFilePath

        if temp is None:
            return ""

        return temp

    @property
    def use_file_db(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UseFileDB

        if temp is None:
            return False

        return temp

    @property
    def use_local_database(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UseLocalDatabase

        if temp is None:
            return False

        return temp

    @property
    def use_network_database(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UseNetworkDatabase

        if temp is None:
            return False

        return temp

    @property
    def uses_network_database_or_local_database_is_on_network_path(
        self: Self,
    ) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UsesNetworkDatabaseOrLocalDatabaseIsOnNetworkPath

        if temp is None:
            return False

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "DatabaseConnectionSettings._Cast_DatabaseConnectionSettings":
        return self._Cast_DatabaseConnectionSettings(self)
