"""BevelGearISOMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.materials import _587
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ISO_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "BevelGearISOMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.materials import _273
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearISOMaterialDatabase",)


Self = TypeVar("Self", bound="BevelGearISOMaterialDatabase")


class BevelGearISOMaterialDatabase(
    _587.BevelGearAbstractMaterialDatabase["_588.BevelGearISOMaterial"]
):
    """BevelGearISOMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_ISO_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearISOMaterialDatabase")

    class _Cast_BevelGearISOMaterialDatabase:
        """Special nested class for casting BevelGearISOMaterialDatabase to subclasses."""

        def __init__(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
            parent: "BevelGearISOMaterialDatabase",
        ):
            self._parent = parent

        @property
        def bevel_gear_abstract_material_database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ) -> "_587.BevelGearAbstractMaterialDatabase":
            return self._parent._cast(_587.BevelGearAbstractMaterialDatabase)

        @property
        def material_database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ) -> "_273.MaterialDatabase":
            from mastapy.materials import _273

            return self._parent._cast(_273.MaterialDatabase)

        @property
        def named_database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ) -> "_1835.NamedDatabase":
            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def bevel_gear_iso_material_database(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
        ) -> "BevelGearISOMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearISOMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase":
        return self._Cast_BevelGearISOMaterialDatabase(self)
