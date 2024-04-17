"""LoadedRollingBearingRaceResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_RACE_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollingBearingRaceResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2008, _2023


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollingBearingRaceResults",)


Self = TypeVar("Self", bound="LoadedRollingBearingRaceResults")


class LoadedRollingBearingRaceResults(_0.APIBase):
    """LoadedRollingBearingRaceResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLING_BEARING_RACE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollingBearingRaceResults")

    class _Cast_LoadedRollingBearingRaceResults:
        """Special nested class for casting LoadedRollingBearingRaceResults to subclasses."""

        def __init__(
            self: "LoadedRollingBearingRaceResults._Cast_LoadedRollingBearingRaceResults",
            parent: "LoadedRollingBearingRaceResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_race_results(
            self: "LoadedRollingBearingRaceResults._Cast_LoadedRollingBearingRaceResults",
        ) -> "_2008.LoadedBallBearingRaceResults":
            from mastapy.bearings.bearing_results.rolling import _2008

            return self._parent._cast(_2008.LoadedBallBearingRaceResults)

        @property
        def loaded_four_point_contact_ball_bearing_race_results(
            self: "LoadedRollingBearingRaceResults._Cast_LoadedRollingBearingRaceResults",
        ) -> "_2023.LoadedFourPointContactBallBearingRaceResults":
            from mastapy.bearings.bearing_results.rolling import _2023

            return self._parent._cast(
                _2023.LoadedFourPointContactBallBearingRaceResults
            )

        @property
        def loaded_rolling_bearing_race_results(
            self: "LoadedRollingBearingRaceResults._Cast_LoadedRollingBearingRaceResults",
        ) -> "LoadedRollingBearingRaceResults":
            return self._parent

        def __getattr__(
            self: "LoadedRollingBearingRaceResults._Cast_LoadedRollingBearingRaceResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollingBearingRaceResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_radius_in_rolling_direction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRadiusInRollingDirection

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

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
    ) -> "LoadedRollingBearingRaceResults._Cast_LoadedRollingBearingRaceResults":
        return self._Cast_LoadedRollingBearingRaceResults(self)
