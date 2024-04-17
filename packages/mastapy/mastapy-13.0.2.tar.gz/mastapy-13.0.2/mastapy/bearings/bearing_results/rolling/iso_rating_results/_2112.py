"""ISOResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults", "ISOResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
        _2108,
        _2109,
        _2110,
        _2113,
        _2114,
        _2115,
    )
    from mastapy.bearings.bearing_results.rolling.abma import _2122, _2123, _2124


__docformat__ = "restructuredtext en"
__all__ = ("ISOResults",)


Self = TypeVar("Self", bound="ISOResults")


class ISOResults(_0.APIBase):
    """ISOResults

    This is a mastapy class.
    """

    TYPE = _ISO_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISOResults")

    class _Cast_ISOResults:
        """Special nested class for casting ISOResults to subclasses."""

        def __init__(self: "ISOResults._Cast_ISOResults", parent: "ISOResults"):
            self._parent = parent

        @property
        def ball_iso2812007_results(
            self: "ISOResults._Cast_ISOResults",
        ) -> "_2108.BallISO2812007Results":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2108,
            )

            return self._parent._cast(_2108.BallISO2812007Results)

        @property
        def ball_isots162812008_results(
            self: "ISOResults._Cast_ISOResults",
        ) -> "_2109.BallISOTS162812008Results":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2109,
            )

            return self._parent._cast(_2109.BallISOTS162812008Results)

        @property
        def iso2812007_results(
            self: "ISOResults._Cast_ISOResults",
        ) -> "_2110.ISO2812007Results":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2110,
            )

            return self._parent._cast(_2110.ISO2812007Results)

        @property
        def isots162812008_results(
            self: "ISOResults._Cast_ISOResults",
        ) -> "_2113.ISOTS162812008Results":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2113,
            )

            return self._parent._cast(_2113.ISOTS162812008Results)

        @property
        def roller_iso2812007_results(
            self: "ISOResults._Cast_ISOResults",
        ) -> "_2114.RollerISO2812007Results":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2114,
            )

            return self._parent._cast(_2114.RollerISO2812007Results)

        @property
        def roller_isots162812008_results(
            self: "ISOResults._Cast_ISOResults",
        ) -> "_2115.RollerISOTS162812008Results":
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
                _2115,
            )

            return self._parent._cast(_2115.RollerISOTS162812008Results)

        @property
        def ansiabma112014_results(
            self: "ISOResults._Cast_ISOResults",
        ) -> "_2122.ANSIABMA112014Results":
            from mastapy.bearings.bearing_results.rolling.abma import _2122

            return self._parent._cast(_2122.ANSIABMA112014Results)

        @property
        def ansiabma92015_results(
            self: "ISOResults._Cast_ISOResults",
        ) -> "_2123.ANSIABMA92015Results":
            from mastapy.bearings.bearing_results.rolling.abma import _2123

            return self._parent._cast(_2123.ANSIABMA92015Results)

        @property
        def ansiabma_results(
            self: "ISOResults._Cast_ISOResults",
        ) -> "_2124.ANSIABMAResults":
            from mastapy.bearings.bearing_results.rolling.abma import _2124

            return self._parent._cast(_2124.ANSIABMAResults)

        @property
        def iso_results(self: "ISOResults._Cast_ISOResults") -> "ISOResults":
            return self._parent

        def __getattr__(self: "ISOResults._Cast_ISOResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISOResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def life_modification_factor_for_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeModificationFactorForReliability

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
    def cast_to(self: Self) -> "ISOResults._Cast_ISOResults":
        return self._Cast_ISOResults(self)
