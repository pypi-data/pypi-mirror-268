"""LoadedPlainOilFedJournalBearingRow"""

from __future__ import annotations

from typing import TypeVar

from PIL.Image import Image

from mastapy._internal import conversion
from mastapy.bearings.bearing_results.fluid_film import _2130
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_PLAIN_OIL_FED_JOURNAL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm",
    "LoadedPlainOilFedJournalBearingRow",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedPlainOilFedJournalBearingRow",)


Self = TypeVar("Self", bound="LoadedPlainOilFedJournalBearingRow")


class LoadedPlainOilFedJournalBearingRow(_2130.LoadedPlainJournalBearingRow):
    """LoadedPlainOilFedJournalBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_PLAIN_OIL_FED_JOURNAL_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedPlainOilFedJournalBearingRow")

    class _Cast_LoadedPlainOilFedJournalBearingRow:
        """Special nested class for casting LoadedPlainOilFedJournalBearingRow to subclasses."""

        def __init__(
            self: "LoadedPlainOilFedJournalBearingRow._Cast_LoadedPlainOilFedJournalBearingRow",
            parent: "LoadedPlainOilFedJournalBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_plain_journal_bearing_row(
            self: "LoadedPlainOilFedJournalBearingRow._Cast_LoadedPlainOilFedJournalBearingRow",
        ) -> "_2130.LoadedPlainJournalBearingRow":
            return self._parent._cast(_2130.LoadedPlainJournalBearingRow)

        @property
        def loaded_plain_oil_fed_journal_bearing_row(
            self: "LoadedPlainOilFedJournalBearingRow._Cast_LoadedPlainOilFedJournalBearingRow",
        ) -> "LoadedPlainOilFedJournalBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedPlainOilFedJournalBearingRow._Cast_LoadedPlainOilFedJournalBearingRow",
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
        self: Self, instance_to_wrap: "LoadedPlainOilFedJournalBearingRow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def attitude_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AttitudeCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonDimensionalMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def power_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_distribution(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureDistribution

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def side_flow_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SideFlowCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedPlainOilFedJournalBearingRow._Cast_LoadedPlainOilFedJournalBearingRow":
        return self._Cast_LoadedPlainOilFedJournalBearingRow(self)
