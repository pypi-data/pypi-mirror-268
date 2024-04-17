"""CombinationAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMBINATION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses",
    "CombinationAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
        _6277,
        _6278,
        _6279,
        _6280,
        _6281,
        _6283,
        _6284,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CombinationAnalysis",)


Self = TypeVar("Self", bound="CombinationAnalysis")


class CombinationAnalysis(_0.APIBase):
    """CombinationAnalysis

    This is a mastapy class.
    """

    TYPE = _COMBINATION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CombinationAnalysis")

    class _Cast_CombinationAnalysis:
        """Special nested class for casting CombinationAnalysis to subclasses."""

        def __init__(
            self: "CombinationAnalysis._Cast_CombinationAnalysis",
            parent: "CombinationAnalysis",
        ):
            self._parent = parent

        @property
        def flexible_pin_analysis(
            self: "CombinationAnalysis._Cast_CombinationAnalysis",
        ) -> "_6277.FlexiblePinAnalysis":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6277,
            )

            return self._parent._cast(_6277.FlexiblePinAnalysis)

        @property
        def flexible_pin_analysis_concept_level(
            self: "CombinationAnalysis._Cast_CombinationAnalysis",
        ) -> "_6278.FlexiblePinAnalysisConceptLevel":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6278,
            )

            return self._parent._cast(_6278.FlexiblePinAnalysisConceptLevel)

        @property
        def flexible_pin_analysis_detail_level_and_pin_fatigue_one_tooth_pass(
            self: "CombinationAnalysis._Cast_CombinationAnalysis",
        ) -> "_6279.FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6279,
            )

            return self._parent._cast(
                _6279.FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
            )

        @property
        def flexible_pin_analysis_gear_and_bearing_rating(
            self: "CombinationAnalysis._Cast_CombinationAnalysis",
        ) -> "_6280.FlexiblePinAnalysisGearAndBearingRating":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6280,
            )

            return self._parent._cast(_6280.FlexiblePinAnalysisGearAndBearingRating)

        @property
        def flexible_pin_analysis_manufacture_level(
            self: "CombinationAnalysis._Cast_CombinationAnalysis",
        ) -> "_6281.FlexiblePinAnalysisManufactureLevel":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6281,
            )

            return self._parent._cast(_6281.FlexiblePinAnalysisManufactureLevel)

        @property
        def flexible_pin_analysis_stop_start_analysis(
            self: "CombinationAnalysis._Cast_CombinationAnalysis",
        ) -> "_6283.FlexiblePinAnalysisStopStartAnalysis":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6283,
            )

            return self._parent._cast(_6283.FlexiblePinAnalysisStopStartAnalysis)

        @property
        def wind_turbine_certification_report(
            self: "CombinationAnalysis._Cast_CombinationAnalysis",
        ) -> "_6284.WindTurbineCertificationReport":
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import (
                _6284,
            )

            return self._parent._cast(_6284.WindTurbineCertificationReport)

        @property
        def combination_analysis(
            self: "CombinationAnalysis._Cast_CombinationAnalysis",
        ) -> "CombinationAnalysis":
            return self._parent

        def __getattr__(
            self: "CombinationAnalysis._Cast_CombinationAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CombinationAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self: Self) -> "CombinationAnalysis._Cast_CombinationAnalysis":
        return self._Cast_CombinationAnalysis(self)
