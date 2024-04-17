"""AxialHoleJournalBearing"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_designs.fluid_film import _2188
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_HOLE_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "AxialHoleJournalBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("AxialHoleJournalBearing",)


Self = TypeVar("Self", bound="AxialHoleJournalBearing")


class AxialHoleJournalBearing(_2188.AxialFeedJournalBearing):
    """AxialHoleJournalBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_HOLE_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AxialHoleJournalBearing")

    class _Cast_AxialHoleJournalBearing:
        """Special nested class for casting AxialHoleJournalBearing to subclasses."""

        def __init__(
            self: "AxialHoleJournalBearing._Cast_AxialHoleJournalBearing",
            parent: "AxialHoleJournalBearing",
        ):
            self._parent = parent

        @property
        def axial_feed_journal_bearing(
            self: "AxialHoleJournalBearing._Cast_AxialHoleJournalBearing",
        ) -> "_2188.AxialFeedJournalBearing":
            return self._parent._cast(_2188.AxialFeedJournalBearing)

        @property
        def axial_hole_journal_bearing(
            self: "AxialHoleJournalBearing._Cast_AxialHoleJournalBearing",
        ) -> "AxialHoleJournalBearing":
            return self._parent

        def __getattr__(
            self: "AxialHoleJournalBearing._Cast_AxialHoleJournalBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AxialHoleJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hole_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HoleDiameter

        if temp is None:
            return 0.0

        return temp

    @hole_diameter.setter
    @enforce_parameter_types
    def hole_diameter(self: Self, value: "float"):
        self.wrapped.HoleDiameter = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "AxialHoleJournalBearing._Cast_AxialHoleJournalBearing":
        return self._Cast_AxialHoleJournalBearing(self)
