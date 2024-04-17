"""BevelGearAbstractMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _273
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ABSTRACT_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "BevelGearAbstractMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _590, _589
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearAbstractMaterialDatabase",)


Self = TypeVar("Self", bound="BevelGearAbstractMaterialDatabase")
T = TypeVar("T", bound="_590.BevelGearMaterial")


class BevelGearAbstractMaterialDatabase(_273.MaterialDatabase[T]):
    """BevelGearAbstractMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _BEVEL_GEAR_ABSTRACT_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearAbstractMaterialDatabase")

    class _Cast_BevelGearAbstractMaterialDatabase:
        """Special nested class for casting BevelGearAbstractMaterialDatabase to subclasses."""

        def __init__(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
            parent: "BevelGearAbstractMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "_273.MaterialDatabase":
            return self._parent._cast(_273.MaterialDatabase)

        @property
        def named_database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "_1835.NamedDatabase":
            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def bevel_gear_iso_material_database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "_589.BevelGearISOMaterialDatabase":
            from mastapy.gears.materials import _589

            return self._parent._cast(_589.BevelGearISOMaterialDatabase)

        @property
        def bevel_gear_abstract_material_database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "BevelGearAbstractMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "BevelGearAbstractMaterialDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase":
        return self._Cast_BevelGearAbstractMaterialDatabase(self)
