"""LoadedPlainJournalBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_PLAIN_JOURNAL_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm", "LoadedPlainJournalBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1885
    from mastapy.bearings.bearing_results.fluid_film import _2132


__docformat__ = "restructuredtext en"
__all__ = ("LoadedPlainJournalBearingRow",)


Self = TypeVar("Self", bound="LoadedPlainJournalBearingRow")


class LoadedPlainJournalBearingRow(_0.APIBase):
    """LoadedPlainJournalBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_PLAIN_JOURNAL_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedPlainJournalBearingRow")

    class _Cast_LoadedPlainJournalBearingRow:
        """Special nested class for casting LoadedPlainJournalBearingRow to subclasses."""

        def __init__(
            self: "LoadedPlainJournalBearingRow._Cast_LoadedPlainJournalBearingRow",
            parent: "LoadedPlainJournalBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_plain_oil_fed_journal_bearing_row(
            self: "LoadedPlainJournalBearingRow._Cast_LoadedPlainJournalBearingRow",
        ) -> "_2132.LoadedPlainOilFedJournalBearingRow":
            from mastapy.bearings.bearing_results.fluid_film import _2132

            return self._parent._cast(_2132.LoadedPlainOilFedJournalBearingRow)

        @property
        def loaded_plain_journal_bearing_row(
            self: "LoadedPlainJournalBearingRow._Cast_LoadedPlainJournalBearingRow",
        ) -> "LoadedPlainJournalBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedPlainJournalBearingRow._Cast_LoadedPlainJournalBearingRow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedPlainJournalBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_position_of_the_minimum_film_thickness_from_the_x_axis(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularPositionOfTheMinimumFilmThicknessFromTheXAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def attitude_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AttitudeAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def attitude_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AttitudeForce

        if temp is None:
            return 0.0

        return temp

    @property
    def clipped_minimum_film_thickness_at_row_centre(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClippedMinimumFilmThicknessAtRowCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_traction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfTraction

        if temp is None:
            return 0.0

        return temp

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
    def force_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceX

        if temp is None:
            return 0.0

        return temp

    @property
    def force_y(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceY

        if temp is None:
            return 0.0

        return temp

    @property
    def journal_bearing_loading_chart(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.JournalBearingLoadingChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def minimum_film_thickness_at_row_centre(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFilmThicknessAtRowCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonDimensionalLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_load_per_unit_of_projected_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialLoadPerUnitOfProjectedArea

        if temp is None:
            return 0.0

        return temp

    @property
    def row(self: Self) -> "_1885.BearingRow":
        """mastapy.bearings.BearingRow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Row

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bearings.BearingRow")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.bearings._1885", "BearingRow")(
            value
        )

    @property
    def sommerfeld_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SommerfeldNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedPlainJournalBearingRow._Cast_LoadedPlainJournalBearingRow":
        return self._Cast_LoadedPlainJournalBearingRow(self)
