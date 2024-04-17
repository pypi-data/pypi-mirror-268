"""MaterialsSettingsDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIALS_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.Materials", "MaterialsSettingsDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("MaterialsSettingsDatabase",)


Self = TypeVar("Self", bound="MaterialsSettingsDatabase")


class MaterialsSettingsDatabase(_1835.NamedDatabase["_276.MaterialsSettingsItem"]):
    """MaterialsSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _MATERIALS_SETTINGS_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaterialsSettingsDatabase")

    class _Cast_MaterialsSettingsDatabase:
        """Special nested class for casting MaterialsSettingsDatabase to subclasses."""

        def __init__(
            self: "MaterialsSettingsDatabase._Cast_MaterialsSettingsDatabase",
            parent: "MaterialsSettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "MaterialsSettingsDatabase._Cast_MaterialsSettingsDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "MaterialsSettingsDatabase._Cast_MaterialsSettingsDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "MaterialsSettingsDatabase._Cast_MaterialsSettingsDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def materials_settings_database(
            self: "MaterialsSettingsDatabase._Cast_MaterialsSettingsDatabase",
        ) -> "MaterialsSettingsDatabase":
            return self._parent

        def __getattr__(
            self: "MaterialsSettingsDatabase._Cast_MaterialsSettingsDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaterialsSettingsDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MaterialsSettingsDatabase._Cast_MaterialsSettingsDatabase":
        return self._Cast_MaterialsSettingsDatabase(self)
