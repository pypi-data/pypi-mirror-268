"""BearingSettingsDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.Bearings", "BearingSettingsDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("BearingSettingsDatabase",)


Self = TypeVar("Self", bound="BearingSettingsDatabase")


class BearingSettingsDatabase(_1835.NamedDatabase["_1888.BearingSettingsItem"]):
    """BearingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _BEARING_SETTINGS_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingSettingsDatabase")

    class _Cast_BearingSettingsDatabase:
        """Special nested class for casting BearingSettingsDatabase to subclasses."""

        def __init__(
            self: "BearingSettingsDatabase._Cast_BearingSettingsDatabase",
            parent: "BearingSettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "BearingSettingsDatabase._Cast_BearingSettingsDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "BearingSettingsDatabase._Cast_BearingSettingsDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "BearingSettingsDatabase._Cast_BearingSettingsDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def bearing_settings_database(
            self: "BearingSettingsDatabase._Cast_BearingSettingsDatabase",
        ) -> "BearingSettingsDatabase":
            return self._parent

        def __getattr__(
            self: "BearingSettingsDatabase._Cast_BearingSettingsDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingSettingsDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BearingSettingsDatabase._Cast_BearingSettingsDatabase":
        return self._Cast_BearingSettingsDatabase(self)
