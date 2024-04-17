"""PedestalJournalBearing"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_designs.fluid_film import _2199
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PEDESTAL_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "PedestalJournalBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("PedestalJournalBearing",)


Self = TypeVar("Self", bound="PedestalJournalBearing")


class PedestalJournalBearing(_2199.PlainJournalHousing):
    """PedestalJournalBearing

    This is a mastapy class.
    """

    TYPE = _PEDESTAL_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PedestalJournalBearing")

    class _Cast_PedestalJournalBearing:
        """Special nested class for casting PedestalJournalBearing to subclasses."""

        def __init__(
            self: "PedestalJournalBearing._Cast_PedestalJournalBearing",
            parent: "PedestalJournalBearing",
        ):
            self._parent = parent

        @property
        def plain_journal_housing(
            self: "PedestalJournalBearing._Cast_PedestalJournalBearing",
        ) -> "_2199.PlainJournalHousing":
            return self._parent._cast(_2199.PlainJournalHousing)

        @property
        def pedestal_journal_bearing(
            self: "PedestalJournalBearing._Cast_PedestalJournalBearing",
        ) -> "PedestalJournalBearing":
            return self._parent

        def __getattr__(
            self: "PedestalJournalBearing._Cast_PedestalJournalBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PedestalJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pedestal_base_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PedestalBaseDepth

        if temp is None:
            return 0.0

        return temp

    @pedestal_base_depth.setter
    @enforce_parameter_types
    def pedestal_base_depth(self: Self, value: "float"):
        self.wrapped.PedestalBaseDepth = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "PedestalJournalBearing._Cast_PedestalJournalBearing":
        return self._Cast_PedestalJournalBearing(self)
