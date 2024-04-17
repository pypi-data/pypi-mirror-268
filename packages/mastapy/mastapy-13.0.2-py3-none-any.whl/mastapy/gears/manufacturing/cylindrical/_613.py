"""CylindricalCutterDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_CUTTER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalCutterDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import (
        _716,
        _708,
        _714,
        _719,
        _720,
    )
    from mastapy.gears.manufacturing.cylindrical import _618, _629
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalCutterDatabase",)


Self = TypeVar("Self", bound="CylindricalCutterDatabase")
T = TypeVar("T", bound="_716.CylindricalGearRealCutterDesign")


class CylindricalCutterDatabase(_1835.NamedDatabase[T]):
    """CylindricalCutterDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CYLINDRICAL_CUTTER_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalCutterDatabase")

    class _Cast_CylindricalCutterDatabase:
        """Special nested class for casting CylindricalCutterDatabase to subclasses."""

        def __init__(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
            parent: "CylindricalCutterDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def cylindrical_hob_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_618.CylindricalHobDatabase":
            from mastapy.gears.manufacturing.cylindrical import _618

            return self._parent._cast(_618.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_629.CylindricalShaperDatabase":
            from mastapy.gears.manufacturing.cylindrical import _629

            return self._parent._cast(_629.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_708.CylindricalFormedWheelGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _708

            return self._parent._cast(_708.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_714.CylindricalGearPlungeShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _714

            return self._parent._cast(_714.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_719.CylindricalGearShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _719

            return self._parent._cast(_719.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_720.CylindricalWormGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _720

            return self._parent._cast(_720.CylindricalWormGrinderDatabase)

        @property
        def cylindrical_cutter_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "CylindricalCutterDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalCutterDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase":
        return self._Cast_CylindricalCutterDatabase(self)
