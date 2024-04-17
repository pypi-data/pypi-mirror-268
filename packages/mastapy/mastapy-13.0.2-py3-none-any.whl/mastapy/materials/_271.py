"""LubricationDetailDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LUBRICATION_DETAIL_DATABASE = python_net_import(
    "SMT.MastaAPI.Materials", "LubricationDetailDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("LubricationDetailDatabase",)


Self = TypeVar("Self", bound="LubricationDetailDatabase")


class LubricationDetailDatabase(_1835.NamedDatabase["_270.LubricationDetail"]):
    """LubricationDetailDatabase

    This is a mastapy class.
    """

    TYPE = _LUBRICATION_DETAIL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LubricationDetailDatabase")

    class _Cast_LubricationDetailDatabase:
        """Special nested class for casting LubricationDetailDatabase to subclasses."""

        def __init__(
            self: "LubricationDetailDatabase._Cast_LubricationDetailDatabase",
            parent: "LubricationDetailDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "LubricationDetailDatabase._Cast_LubricationDetailDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "LubricationDetailDatabase._Cast_LubricationDetailDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "LubricationDetailDatabase._Cast_LubricationDetailDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def lubrication_detail_database(
            self: "LubricationDetailDatabase._Cast_LubricationDetailDatabase",
        ) -> "LubricationDetailDatabase":
            return self._parent

        def __getattr__(
            self: "LubricationDetailDatabase._Cast_LubricationDetailDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LubricationDetailDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LubricationDetailDatabase._Cast_LubricationDetailDatabase":
        return self._Cast_LubricationDetailDatabase(self)
