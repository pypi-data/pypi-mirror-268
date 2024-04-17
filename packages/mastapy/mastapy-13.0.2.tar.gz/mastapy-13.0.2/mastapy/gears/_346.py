"""PocketingPowerLossCoefficientsDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POCKETING_POWER_LOSS_COEFFICIENTS_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears", "PocketingPowerLossCoefficientsDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("PocketingPowerLossCoefficientsDatabase",)


Self = TypeVar("Self", bound="PocketingPowerLossCoefficientsDatabase")


class PocketingPowerLossCoefficientsDatabase(
    _1835.NamedDatabase["_345.PocketingPowerLossCoefficients"]
):
    """PocketingPowerLossCoefficientsDatabase

    This is a mastapy class.
    """

    TYPE = _POCKETING_POWER_LOSS_COEFFICIENTS_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PocketingPowerLossCoefficientsDatabase"
    )

    class _Cast_PocketingPowerLossCoefficientsDatabase:
        """Special nested class for casting PocketingPowerLossCoefficientsDatabase to subclasses."""

        def __init__(
            self: "PocketingPowerLossCoefficientsDatabase._Cast_PocketingPowerLossCoefficientsDatabase",
            parent: "PocketingPowerLossCoefficientsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "PocketingPowerLossCoefficientsDatabase._Cast_PocketingPowerLossCoefficientsDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "PocketingPowerLossCoefficientsDatabase._Cast_PocketingPowerLossCoefficientsDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "PocketingPowerLossCoefficientsDatabase._Cast_PocketingPowerLossCoefficientsDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def pocketing_power_loss_coefficients_database(
            self: "PocketingPowerLossCoefficientsDatabase._Cast_PocketingPowerLossCoefficientsDatabase",
        ) -> "PocketingPowerLossCoefficientsDatabase":
            return self._parent

        def __getattr__(
            self: "PocketingPowerLossCoefficientsDatabase._Cast_PocketingPowerLossCoefficientsDatabase",
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
        self: Self, instance_to_wrap: "PocketingPowerLossCoefficientsDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PocketingPowerLossCoefficientsDatabase._Cast_PocketingPowerLossCoefficientsDatabase":
        return self._Cast_PocketingPowerLossCoefficientsDatabase(self)
