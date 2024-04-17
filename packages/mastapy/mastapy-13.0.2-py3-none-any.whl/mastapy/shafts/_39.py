"""ShaftSettingsDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftSettingsDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSettingsDatabase",)


Self = TypeVar("Self", bound="ShaftSettingsDatabase")


class ShaftSettingsDatabase(_1835.NamedDatabase["_40.ShaftSettingsItem"]):
    """ShaftSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _SHAFT_SETTINGS_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSettingsDatabase")

    class _Cast_ShaftSettingsDatabase:
        """Special nested class for casting ShaftSettingsDatabase to subclasses."""

        def __init__(
            self: "ShaftSettingsDatabase._Cast_ShaftSettingsDatabase",
            parent: "ShaftSettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "ShaftSettingsDatabase._Cast_ShaftSettingsDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "ShaftSettingsDatabase._Cast_ShaftSettingsDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "ShaftSettingsDatabase._Cast_ShaftSettingsDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def shaft_settings_database(
            self: "ShaftSettingsDatabase._Cast_ShaftSettingsDatabase",
        ) -> "ShaftSettingsDatabase":
            return self._parent

        def __getattr__(
            self: "ShaftSettingsDatabase._Cast_ShaftSettingsDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSettingsDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftSettingsDatabase._Cast_ShaftSettingsDatabase":
        return self._Cast_ShaftSettingsDatabase(self)
