"""CylindricalPlasticGearRatingSettingsDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical",
    "CylindricalPlasticGearRatingSettingsDatabase",
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlasticGearRatingSettingsDatabase",)


Self = TypeVar("Self", bound="CylindricalPlasticGearRatingSettingsDatabase")


class CylindricalPlasticGearRatingSettingsDatabase(
    _1835.NamedDatabase["_473.CylindricalPlasticGearRatingSettingsItem"]
):
    """CylindricalPlasticGearRatingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlasticGearRatingSettingsDatabase"
    )

    class _Cast_CylindricalPlasticGearRatingSettingsDatabase:
        """Special nested class for casting CylindricalPlasticGearRatingSettingsDatabase to subclasses."""

        def __init__(
            self: "CylindricalPlasticGearRatingSettingsDatabase._Cast_CylindricalPlasticGearRatingSettingsDatabase",
            parent: "CylindricalPlasticGearRatingSettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "CylindricalPlasticGearRatingSettingsDatabase._Cast_CylindricalPlasticGearRatingSettingsDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalPlasticGearRatingSettingsDatabase._Cast_CylindricalPlasticGearRatingSettingsDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "CylindricalPlasticGearRatingSettingsDatabase._Cast_CylindricalPlasticGearRatingSettingsDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def cylindrical_plastic_gear_rating_settings_database(
            self: "CylindricalPlasticGearRatingSettingsDatabase._Cast_CylindricalPlasticGearRatingSettingsDatabase",
        ) -> "CylindricalPlasticGearRatingSettingsDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalPlasticGearRatingSettingsDatabase._Cast_CylindricalPlasticGearRatingSettingsDatabase",
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
        instance_to_wrap: "CylindricalPlasticGearRatingSettingsDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlasticGearRatingSettingsDatabase._Cast_CylindricalPlasticGearRatingSettingsDatabase":
        return self._Cast_CylindricalPlasticGearRatingSettingsDatabase(self)
