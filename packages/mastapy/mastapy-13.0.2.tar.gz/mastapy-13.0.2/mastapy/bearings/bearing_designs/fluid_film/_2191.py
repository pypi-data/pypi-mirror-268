"""CircumferentialFeedJournalBearing"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CIRCUMFERENTIAL_FEED_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm",
    "CircumferentialFeedJournalBearing",
)


__docformat__ = "restructuredtext en"
__all__ = ("CircumferentialFeedJournalBearing",)


Self = TypeVar("Self", bound="CircumferentialFeedJournalBearing")


class CircumferentialFeedJournalBearing(_0.APIBase):
    """CircumferentialFeedJournalBearing

    This is a mastapy class.
    """

    TYPE = _CIRCUMFERENTIAL_FEED_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CircumferentialFeedJournalBearing")

    class _Cast_CircumferentialFeedJournalBearing:
        """Special nested class for casting CircumferentialFeedJournalBearing to subclasses."""

        def __init__(
            self: "CircumferentialFeedJournalBearing._Cast_CircumferentialFeedJournalBearing",
            parent: "CircumferentialFeedJournalBearing",
        ):
            self._parent = parent

        @property
        def circumferential_feed_journal_bearing(
            self: "CircumferentialFeedJournalBearing._Cast_CircumferentialFeedJournalBearing",
        ) -> "CircumferentialFeedJournalBearing":
            return self._parent

        def __getattr__(
            self: "CircumferentialFeedJournalBearing._Cast_CircumferentialFeedJournalBearing",
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
        self: Self, instance_to_wrap: "CircumferentialFeedJournalBearing.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def groove_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GrooveWidth

        if temp is None:
            return 0.0

        return temp

    @groove_width.setter
    @enforce_parameter_types
    def groove_width(self: Self, value: "float"):
        self.wrapped.GrooveWidth = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "CircumferentialFeedJournalBearing._Cast_CircumferentialFeedJournalBearing":
        return self._Cast_CircumferentialFeedJournalBearing(self)
