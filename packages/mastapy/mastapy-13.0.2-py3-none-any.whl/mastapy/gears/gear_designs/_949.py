"""DesignConstraintCollectionDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_CONSTRAINT_COLLECTION_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "DesignConstraintCollectionDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("DesignConstraintCollectionDatabase",)


Self = TypeVar("Self", bound="DesignConstraintCollectionDatabase")


class DesignConstraintCollectionDatabase(
    _1835.NamedDatabase["_950.DesignConstraintsCollection"]
):
    """DesignConstraintCollectionDatabase

    This is a mastapy class.
    """

    TYPE = _DESIGN_CONSTRAINT_COLLECTION_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignConstraintCollectionDatabase")

    class _Cast_DesignConstraintCollectionDatabase:
        """Special nested class for casting DesignConstraintCollectionDatabase to subclasses."""

        def __init__(
            self: "DesignConstraintCollectionDatabase._Cast_DesignConstraintCollectionDatabase",
            parent: "DesignConstraintCollectionDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "DesignConstraintCollectionDatabase._Cast_DesignConstraintCollectionDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "DesignConstraintCollectionDatabase._Cast_DesignConstraintCollectionDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "DesignConstraintCollectionDatabase._Cast_DesignConstraintCollectionDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def design_constraint_collection_database(
            self: "DesignConstraintCollectionDatabase._Cast_DesignConstraintCollectionDatabase",
        ) -> "DesignConstraintCollectionDatabase":
            return self._parent

        def __getattr__(
            self: "DesignConstraintCollectionDatabase._Cast_DesignConstraintCollectionDatabase",
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
        self: Self, instance_to_wrap: "DesignConstraintCollectionDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DesignConstraintCollectionDatabase._Cast_DesignConstraintCollectionDatabase":
        return self._Cast_DesignConstraintCollectionDatabase(self)
