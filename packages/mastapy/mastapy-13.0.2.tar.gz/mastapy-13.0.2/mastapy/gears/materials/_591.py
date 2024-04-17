"""BevelGearMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.materials import _598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "BevelGearMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMaterialDatabase",)


Self = TypeVar("Self", bound="BevelGearMaterialDatabase")


class BevelGearMaterialDatabase(_598.GearMaterialDatabase["_590.BevelGearMaterial"]):
    """BevelGearMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMaterialDatabase")

    class _Cast_BevelGearMaterialDatabase:
        """Special nested class for casting BevelGearMaterialDatabase to subclasses."""

        def __init__(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
            parent: "BevelGearMaterialDatabase",
        ):
            self._parent = parent

        @property
        def gear_material_database(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
        ) -> "_598.GearMaterialDatabase":
            return self._parent._cast(_598.GearMaterialDatabase)

        @property
        def named_database(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
        ) -> "_1835.NamedDatabase":
            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def bevel_gear_material_database(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
        ) -> "BevelGearMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase":
        return self._Cast_BevelGearMaterialDatabase(self)
