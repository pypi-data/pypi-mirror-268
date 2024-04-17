"""CycloidalDiscMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _273
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Cycloidal", "CycloidalDiscMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscMaterialDatabase",)


Self = TypeVar("Self", bound="CycloidalDiscMaterialDatabase")


class CycloidalDiscMaterialDatabase(
    _273.MaterialDatabase["_1463.CycloidalDiscMaterial"]
):
    """CycloidalDiscMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscMaterialDatabase")

    class _Cast_CycloidalDiscMaterialDatabase:
        """Special nested class for casting CycloidalDiscMaterialDatabase to subclasses."""

        def __init__(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
            parent: "CycloidalDiscMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
        ) -> "_273.MaterialDatabase":
            return self._parent._cast(_273.MaterialDatabase)

        @property
        def named_database(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
        ) -> "_1835.NamedDatabase":
            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def cycloidal_disc_material_database(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
        ) -> "CycloidalDiscMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscMaterialDatabase._Cast_CycloidalDiscMaterialDatabase":
        return self._Cast_CycloidalDiscMaterialDatabase(self)
