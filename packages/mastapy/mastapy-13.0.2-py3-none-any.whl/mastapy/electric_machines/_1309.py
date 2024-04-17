"""StatorRotorMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _273
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_ROTOR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "StatorRotorMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("StatorRotorMaterialDatabase",)


Self = TypeVar("Self", bound="StatorRotorMaterialDatabase")


class StatorRotorMaterialDatabase(_273.MaterialDatabase["_1308.StatorRotorMaterial"]):
    """StatorRotorMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _STATOR_ROTOR_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StatorRotorMaterialDatabase")

    class _Cast_StatorRotorMaterialDatabase:
        """Special nested class for casting StatorRotorMaterialDatabase to subclasses."""

        def __init__(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
            parent: "StatorRotorMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
        ) -> "_273.MaterialDatabase":
            return self._parent._cast(_273.MaterialDatabase)

        @property
        def named_database(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
        ) -> "_1835.NamedDatabase":
            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def stator_rotor_material_database(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
        ) -> "StatorRotorMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StatorRotorMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StatorRotorMaterialDatabase._Cast_StatorRotorMaterialDatabase":
        return self._Cast_StatorRotorMaterialDatabase(self)
