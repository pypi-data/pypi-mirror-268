"""LoadedFluidFilmBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results import _1961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FLUID_FILM_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm", "LoadedFluidFilmBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.fluid_film import (
        _2127,
        _2128,
        _2129,
        _2131,
        _2134,
        _2135,
    )
    from mastapy.bearings.bearing_results import _1964, _1956
    from mastapy.bearings import _1882


__docformat__ = "restructuredtext en"
__all__ = ("LoadedFluidFilmBearingResults",)


Self = TypeVar("Self", bound="LoadedFluidFilmBearingResults")


class LoadedFluidFilmBearingResults(_1961.LoadedDetailedBearingResults):
    """LoadedFluidFilmBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_FLUID_FILM_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedFluidFilmBearingResults")

    class _Cast_LoadedFluidFilmBearingResults:
        """Special nested class for casting LoadedFluidFilmBearingResults to subclasses."""

        def __init__(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
            parent: "LoadedFluidFilmBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_1961.LoadedDetailedBearingResults":
            return self._parent._cast(_1961.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_1882.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingLoadCaseResultsLightweight)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2127.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2127

            return self._parent._cast(_2127.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2128.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2128

            return self._parent._cast(_2128.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2129.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2129

            return self._parent._cast(_2129.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2131.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2131

            return self._parent._cast(_2131.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2134.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2134

            return self._parent._cast(_2134.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2135.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2135

            return self._parent._cast(_2135.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "LoadedFluidFilmBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedFluidFilmBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults":
        return self._Cast_LoadedFluidFilmBearingResults(self)
