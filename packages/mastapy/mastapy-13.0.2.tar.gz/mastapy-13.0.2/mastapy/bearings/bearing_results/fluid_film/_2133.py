"""LoadedTiltingJournalPad"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.fluid_film import _2125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TILTING_JOURNAL_PAD = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm", "LoadedTiltingJournalPad"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedTiltingJournalPad",)


Self = TypeVar("Self", bound="LoadedTiltingJournalPad")


class LoadedTiltingJournalPad(_2125.LoadedFluidFilmBearingPad):
    """LoadedTiltingJournalPad

    This is a mastapy class.
    """

    TYPE = _LOADED_TILTING_JOURNAL_PAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedTiltingJournalPad")

    class _Cast_LoadedTiltingJournalPad:
        """Special nested class for casting LoadedTiltingJournalPad to subclasses."""

        def __init__(
            self: "LoadedTiltingJournalPad._Cast_LoadedTiltingJournalPad",
            parent: "LoadedTiltingJournalPad",
        ):
            self._parent = parent

        @property
        def loaded_fluid_film_bearing_pad(
            self: "LoadedTiltingJournalPad._Cast_LoadedTiltingJournalPad",
        ) -> "_2125.LoadedFluidFilmBearingPad":
            return self._parent._cast(_2125.LoadedFluidFilmBearingPad)

        @property
        def loaded_tilting_journal_pad(
            self: "LoadedTiltingJournalPad._Cast_LoadedTiltingJournalPad",
        ) -> "LoadedTiltingJournalPad":
            return self._parent

        def __getattr__(
            self: "LoadedTiltingJournalPad._Cast_LoadedTiltingJournalPad", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedTiltingJournalPad.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def eccentricity_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EccentricityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricant_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricantFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "LoadedTiltingJournalPad._Cast_LoadedTiltingJournalPad":
        return self._Cast_LoadedTiltingJournalPad(self)
