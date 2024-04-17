"""ISOTR1417912001CoefficientOfFrictionConstantsDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISOTR1417912001_COEFFICIENT_OF_FRICTION_CONSTANTS_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials",
    "ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("ISOTR1417912001CoefficientOfFrictionConstantsDatabase",)


Self = TypeVar("Self", bound="ISOTR1417912001CoefficientOfFrictionConstantsDatabase")


class ISOTR1417912001CoefficientOfFrictionConstantsDatabase(
    _1835.NamedDatabase["_601.ISOTR1417912001CoefficientOfFrictionConstants"]
):
    """ISOTR1417912001CoefficientOfFrictionConstantsDatabase

    This is a mastapy class.
    """

    TYPE = _ISOTR1417912001_COEFFICIENT_OF_FRICTION_CONSTANTS_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase"
    )

    class _Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase:
        """Special nested class for casting ISOTR1417912001CoefficientOfFrictionConstantsDatabase to subclasses."""

        def __init__(
            self: "ISOTR1417912001CoefficientOfFrictionConstantsDatabase._Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
            parent: "ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "ISOTR1417912001CoefficientOfFrictionConstantsDatabase._Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "ISOTR1417912001CoefficientOfFrictionConstantsDatabase._Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "ISOTR1417912001CoefficientOfFrictionConstantsDatabase._Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def isotr1417912001_coefficient_of_friction_constants_database(
            self: "ISOTR1417912001CoefficientOfFrictionConstantsDatabase._Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
        ) -> "ISOTR1417912001CoefficientOfFrictionConstantsDatabase":
            return self._parent

        def __getattr__(
            self: "ISOTR1417912001CoefficientOfFrictionConstantsDatabase._Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
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
        self: Self,
        instance_to_wrap: "ISOTR1417912001CoefficientOfFrictionConstantsDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ISOTR1417912001CoefficientOfFrictionConstantsDatabase._Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase":
        return self._Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase(self)
