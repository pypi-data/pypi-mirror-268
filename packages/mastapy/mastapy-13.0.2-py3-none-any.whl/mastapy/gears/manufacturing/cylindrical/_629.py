"""CylindricalShaperDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical import _613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SHAPER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalShaperDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1835, _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalShaperDatabase",)


Self = TypeVar("Self", bound="CylindricalShaperDatabase")


class CylindricalShaperDatabase(
    _613.CylindricalCutterDatabase["_717.CylindricalGearShaper"]
):
    """CylindricalShaperDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SHAPER_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalShaperDatabase")

    class _Cast_CylindricalShaperDatabase:
        """Special nested class for casting CylindricalShaperDatabase to subclasses."""

        def __init__(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
            parent: "CylindricalShaperDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_cutter_database(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
        ) -> "_613.CylindricalCutterDatabase":
            return self._parent._cast(_613.CylindricalCutterDatabase)

        @property
        def named_database(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
        ) -> "_1835.NamedDatabase":
            from mastapy.utility.databases import _1835

            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def cylindrical_shaper_database(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
        ) -> "CylindricalShaperDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalShaperDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase":
        return self._Cast_CylindricalShaperDatabase(self)
