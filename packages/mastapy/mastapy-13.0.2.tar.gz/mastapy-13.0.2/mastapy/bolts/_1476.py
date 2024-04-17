"""BoltGeometryDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_GEOMETRY_DATABASE = python_net_import(
    "SMT.MastaAPI.Bolts", "BoltGeometryDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("BoltGeometryDatabase",)


Self = TypeVar("Self", bound="BoltGeometryDatabase")


class BoltGeometryDatabase(_1835.NamedDatabase["_1475.BoltGeometry"]):
    """BoltGeometryDatabase

    This is a mastapy class.
    """

    TYPE = _BOLT_GEOMETRY_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltGeometryDatabase")

    class _Cast_BoltGeometryDatabase:
        """Special nested class for casting BoltGeometryDatabase to subclasses."""

        def __init__(
            self: "BoltGeometryDatabase._Cast_BoltGeometryDatabase",
            parent: "BoltGeometryDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "BoltGeometryDatabase._Cast_BoltGeometryDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "BoltGeometryDatabase._Cast_BoltGeometryDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "BoltGeometryDatabase._Cast_BoltGeometryDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def bolt_geometry_database(
            self: "BoltGeometryDatabase._Cast_BoltGeometryDatabase",
        ) -> "BoltGeometryDatabase":
            return self._parent

        def __getattr__(
            self: "BoltGeometryDatabase._Cast_BoltGeometryDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltGeometryDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BoltGeometryDatabase._Cast_BoltGeometryDatabase":
        return self._Cast_BoltGeometryDatabase(self)
