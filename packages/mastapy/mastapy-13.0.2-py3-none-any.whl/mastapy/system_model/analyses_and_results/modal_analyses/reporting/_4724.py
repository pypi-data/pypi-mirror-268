"""CalculateFullFEResultsForMode"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CALCULATE_FULL_FE_RESULTS_FOR_MODE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
    "CalculateFullFEResultsForMode",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4728


__docformat__ = "restructuredtext en"
__all__ = ("CalculateFullFEResultsForMode",)


Self = TypeVar("Self", bound="CalculateFullFEResultsForMode")


class CalculateFullFEResultsForMode(_0.APIBase):
    """CalculateFullFEResultsForMode

    This is a mastapy class.
    """

    TYPE = _CALCULATE_FULL_FE_RESULTS_FOR_MODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CalculateFullFEResultsForMode")

    class _Cast_CalculateFullFEResultsForMode:
        """Special nested class for casting CalculateFullFEResultsForMode to subclasses."""

        def __init__(
            self: "CalculateFullFEResultsForMode._Cast_CalculateFullFEResultsForMode",
            parent: "CalculateFullFEResultsForMode",
        ):
            self._parent = parent

        @property
        def calculate_full_fe_results_for_mode(
            self: "CalculateFullFEResultsForMode._Cast_CalculateFullFEResultsForMode",
        ) -> "CalculateFullFEResultsForMode":
            return self._parent

        def __getattr__(
            self: "CalculateFullFEResultsForMode._Cast_CalculateFullFEResultsForMode",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CalculateFullFEResultsForMode.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_results(self: Self) -> "List[_4728.ModalCMSResultsForModeAndFE]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.ModalCMSResultsForModeAndFE]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    ) -> "CalculateFullFEResultsForMode._Cast_CalculateFullFEResultsForMode":
        return self._Cast_CalculateFullFEResultsForMode(self)
