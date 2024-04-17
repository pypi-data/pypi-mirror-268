"""CylindricalGearDesignConstraintsDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_CONSTRAINTS_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CylindricalGearDesignConstraintsDatabase",
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearDesignConstraintsDatabase",)


Self = TypeVar("Self", bound="CylindricalGearDesignConstraintsDatabase")


class CylindricalGearDesignConstraintsDatabase(
    _1835.NamedDatabase["_1018.CylindricalGearDesignConstraints"]
):
    """CylindricalGearDesignConstraintsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_CONSTRAINTS_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearDesignConstraintsDatabase"
    )

    class _Cast_CylindricalGearDesignConstraintsDatabase:
        """Special nested class for casting CylindricalGearDesignConstraintsDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearDesignConstraintsDatabase._Cast_CylindricalGearDesignConstraintsDatabase",
            parent: "CylindricalGearDesignConstraintsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "CylindricalGearDesignConstraintsDatabase._Cast_CylindricalGearDesignConstraintsDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearDesignConstraintsDatabase._Cast_CylindricalGearDesignConstraintsDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearDesignConstraintsDatabase._Cast_CylindricalGearDesignConstraintsDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def cylindrical_gear_design_constraints_database(
            self: "CylindricalGearDesignConstraintsDatabase._Cast_CylindricalGearDesignConstraintsDatabase",
        ) -> "CylindricalGearDesignConstraintsDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearDesignConstraintsDatabase._Cast_CylindricalGearDesignConstraintsDatabase",
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
        self: Self, instance_to_wrap: "CylindricalGearDesignConstraintsDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearDesignConstraintsDatabase._Cast_CylindricalGearDesignConstraintsDatabase":
        return self._Cast_CylindricalGearDesignConstraintsDatabase(self)
