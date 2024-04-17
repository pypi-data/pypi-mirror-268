"""MachineryEncasedJournalBearing"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_designs.fluid_film import _2199
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MACHINERY_ENCASED_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "MachineryEncasedJournalBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("MachineryEncasedJournalBearing",)


Self = TypeVar("Self", bound="MachineryEncasedJournalBearing")


class MachineryEncasedJournalBearing(_2199.PlainJournalHousing):
    """MachineryEncasedJournalBearing

    This is a mastapy class.
    """

    TYPE = _MACHINERY_ENCASED_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MachineryEncasedJournalBearing")

    class _Cast_MachineryEncasedJournalBearing:
        """Special nested class for casting MachineryEncasedJournalBearing to subclasses."""

        def __init__(
            self: "MachineryEncasedJournalBearing._Cast_MachineryEncasedJournalBearing",
            parent: "MachineryEncasedJournalBearing",
        ):
            self._parent = parent

        @property
        def plain_journal_housing(
            self: "MachineryEncasedJournalBearing._Cast_MachineryEncasedJournalBearing",
        ) -> "_2199.PlainJournalHousing":
            return self._parent._cast(_2199.PlainJournalHousing)

        @property
        def machinery_encased_journal_bearing(
            self: "MachineryEncasedJournalBearing._Cast_MachineryEncasedJournalBearing",
        ) -> "MachineryEncasedJournalBearing":
            return self._parent

        def __getattr__(
            self: "MachineryEncasedJournalBearing._Cast_MachineryEncasedJournalBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MachineryEncasedJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MachineryEncasedJournalBearing._Cast_MachineryEncasedJournalBearing":
        return self._Cast_MachineryEncasedJournalBearing(self)
