"""AxialFeedJournalBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_FEED_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "AxialFeedJournalBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.fluid_film import _2189, _2190


__docformat__ = "restructuredtext en"
__all__ = ("AxialFeedJournalBearing",)


Self = TypeVar("Self", bound="AxialFeedJournalBearing")


class AxialFeedJournalBearing(_0.APIBase):
    """AxialFeedJournalBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_FEED_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AxialFeedJournalBearing")

    class _Cast_AxialFeedJournalBearing:
        """Special nested class for casting AxialFeedJournalBearing to subclasses."""

        def __init__(
            self: "AxialFeedJournalBearing._Cast_AxialFeedJournalBearing",
            parent: "AxialFeedJournalBearing",
        ):
            self._parent = parent

        @property
        def axial_groove_journal_bearing(
            self: "AxialFeedJournalBearing._Cast_AxialFeedJournalBearing",
        ) -> "_2189.AxialGrooveJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2189

            return self._parent._cast(_2189.AxialGrooveJournalBearing)

        @property
        def axial_hole_journal_bearing(
            self: "AxialFeedJournalBearing._Cast_AxialFeedJournalBearing",
        ) -> "_2190.AxialHoleJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2190

            return self._parent._cast(_2190.AxialHoleJournalBearing)

        @property
        def axial_feed_journal_bearing(
            self: "AxialFeedJournalBearing._Cast_AxialFeedJournalBearing",
        ) -> "AxialFeedJournalBearing":
            return self._parent

        def __getattr__(
            self: "AxialFeedJournalBearing._Cast_AxialFeedJournalBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AxialFeedJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def groove_angular_location(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GrooveAngularLocation

        if temp is None:
            return 0.0

        return temp

    @groove_angular_location.setter
    @enforce_parameter_types
    def groove_angular_location(self: Self, value: "float"):
        self.wrapped.GrooveAngularLocation = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "AxialFeedJournalBearing._Cast_AxialFeedJournalBearing":
        return self._Cast_AxialFeedJournalBearing(self)
