"""AxialGrooveJournalBearing"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_designs.fluid_film import _2188
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_GROOVE_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "AxialGrooveJournalBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("AxialGrooveJournalBearing",)


Self = TypeVar("Self", bound="AxialGrooveJournalBearing")


class AxialGrooveJournalBearing(_2188.AxialFeedJournalBearing):
    """AxialGrooveJournalBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_GROOVE_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AxialGrooveJournalBearing")

    class _Cast_AxialGrooveJournalBearing:
        """Special nested class for casting AxialGrooveJournalBearing to subclasses."""

        def __init__(
            self: "AxialGrooveJournalBearing._Cast_AxialGrooveJournalBearing",
            parent: "AxialGrooveJournalBearing",
        ):
            self._parent = parent

        @property
        def axial_feed_journal_bearing(
            self: "AxialGrooveJournalBearing._Cast_AxialGrooveJournalBearing",
        ) -> "_2188.AxialFeedJournalBearing":
            return self._parent._cast(_2188.AxialFeedJournalBearing)

        @property
        def axial_groove_journal_bearing(
            self: "AxialGrooveJournalBearing._Cast_AxialGrooveJournalBearing",
        ) -> "AxialGrooveJournalBearing":
            return self._parent

        def __getattr__(
            self: "AxialGrooveJournalBearing._Cast_AxialGrooveJournalBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AxialGrooveJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def groove_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GrooveLength

        if temp is None:
            return 0.0

        return temp

    @groove_length.setter
    @enforce_parameter_types
    def groove_length(self: Self, value: "float"):
        self.wrapped.GrooveLength = float(value) if value is not None else 0.0

    @property
    def groove_radial_dimension(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GrooveRadialDimension

        if temp is None:
            return 0.0

        return temp

    @groove_radial_dimension.setter
    @enforce_parameter_types
    def groove_radial_dimension(self: Self, value: "float"):
        self.wrapped.GrooveRadialDimension = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "AxialGrooveJournalBearing._Cast_AxialGrooveJournalBearing":
        return self._Cast_AxialGrooveJournalBearing(self)
