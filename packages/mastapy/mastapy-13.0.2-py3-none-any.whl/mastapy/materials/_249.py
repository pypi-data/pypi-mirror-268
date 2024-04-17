"""BearingMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Materials", "BearingMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("BearingMaterialDatabase",)


Self = TypeVar("Self", bound="BearingMaterialDatabase")


class BearingMaterialDatabase(_1835.NamedDatabase["_248.BearingMaterial"]):
    """BearingMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BEARING_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingMaterialDatabase")

    class _Cast_BearingMaterialDatabase:
        """Special nested class for casting BearingMaterialDatabase to subclasses."""

        def __init__(
            self: "BearingMaterialDatabase._Cast_BearingMaterialDatabase",
            parent: "BearingMaterialDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "BearingMaterialDatabase._Cast_BearingMaterialDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "BearingMaterialDatabase._Cast_BearingMaterialDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "BearingMaterialDatabase._Cast_BearingMaterialDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def bearing_material_database(
            self: "BearingMaterialDatabase._Cast_BearingMaterialDatabase",
        ) -> "BearingMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "BearingMaterialDatabase._Cast_BearingMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BearingMaterialDatabase._Cast_BearingMaterialDatabase":
        return self._Cast_BearingMaterialDatabase(self)
