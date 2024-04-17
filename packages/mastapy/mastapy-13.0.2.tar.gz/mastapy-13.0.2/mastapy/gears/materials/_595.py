"""CylindricalGearMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _273
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "CylindricalGearMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _594, _592, _593, _596
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMaterialDatabase",)


Self = TypeVar("Self", bound="CylindricalGearMaterialDatabase")
T = TypeVar("T", bound="_594.CylindricalGearMaterial")


class CylindricalGearMaterialDatabase(_273.MaterialDatabase[T]):
    """CylindricalGearMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CYLINDRICAL_GEAR_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMaterialDatabase")

    class _Cast_CylindricalGearMaterialDatabase:
        """Special nested class for casting CylindricalGearMaterialDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
            parent: "CylindricalGearMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ) -> "_273.MaterialDatabase":
            return self._parent._cast(_273.MaterialDatabase)

        @property
        def named_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ) -> "_1835.NamedDatabase":
            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def cylindrical_gear_agma_material_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ) -> "_592.CylindricalGearAGMAMaterialDatabase":
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ) -> "_593.CylindricalGearISOMaterialDatabase":
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ) -> "_596.CylindricalGearPlasticMaterialDatabase":
            from mastapy.gears.materials import _596

            return self._parent._cast(_596.CylindricalGearPlasticMaterialDatabase)

        @property
        def cylindrical_gear_material_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ) -> "CylindricalGearMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase":
        return self._Cast_CylindricalGearMaterialDatabase(self)
