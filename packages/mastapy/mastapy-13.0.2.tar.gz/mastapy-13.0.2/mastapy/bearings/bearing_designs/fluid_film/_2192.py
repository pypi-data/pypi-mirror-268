"""CylindricalHousingJournalBearing"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_designs.fluid_film import _2199
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_HOUSING_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "CylindricalHousingJournalBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalHousingJournalBearing",)


Self = TypeVar("Self", bound="CylindricalHousingJournalBearing")


class CylindricalHousingJournalBearing(_2199.PlainJournalHousing):
    """CylindricalHousingJournalBearing

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_HOUSING_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalHousingJournalBearing")

    class _Cast_CylindricalHousingJournalBearing:
        """Special nested class for casting CylindricalHousingJournalBearing to subclasses."""

        def __init__(
            self: "CylindricalHousingJournalBearing._Cast_CylindricalHousingJournalBearing",
            parent: "CylindricalHousingJournalBearing",
        ):
            self._parent = parent

        @property
        def plain_journal_housing(
            self: "CylindricalHousingJournalBearing._Cast_CylindricalHousingJournalBearing",
        ) -> "_2199.PlainJournalHousing":
            return self._parent._cast(_2199.PlainJournalHousing)

        @property
        def cylindrical_housing_journal_bearing(
            self: "CylindricalHousingJournalBearing._Cast_CylindricalHousingJournalBearing",
        ) -> "CylindricalHousingJournalBearing":
            return self._parent

        def __getattr__(
            self: "CylindricalHousingJournalBearing._Cast_CylindricalHousingJournalBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalHousingJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalHousingJournalBearing._Cast_CylindricalHousingJournalBearing":
        return self._Cast_CylindricalHousingJournalBearing(self)
