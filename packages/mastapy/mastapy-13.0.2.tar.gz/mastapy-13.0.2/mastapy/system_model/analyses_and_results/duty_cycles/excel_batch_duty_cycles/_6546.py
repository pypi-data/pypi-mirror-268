"""ExcelBatchDutyCycleSpectraCreatorDetails"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXCEL_BATCH_DUTY_CYCLE_SPECTRA_CREATOR_DETAILS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DutyCycles.ExcelBatchDutyCycles",
    "ExcelBatchDutyCycleSpectraCreatorDetails",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.duty_cycles.excel_batch_duty_cycles import (
        _6547,
        _6550,
        _6549,
    )
    from mastapy.utility import _1606


__docformat__ = "restructuredtext en"
__all__ = ("ExcelBatchDutyCycleSpectraCreatorDetails",)


Self = TypeVar("Self", bound="ExcelBatchDutyCycleSpectraCreatorDetails")


class ExcelBatchDutyCycleSpectraCreatorDetails(_0.APIBase):
    """ExcelBatchDutyCycleSpectraCreatorDetails

    This is a mastapy class.
    """

    TYPE = _EXCEL_BATCH_DUTY_CYCLE_SPECTRA_CREATOR_DETAILS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExcelBatchDutyCycleSpectraCreatorDetails"
    )

    class _Cast_ExcelBatchDutyCycleSpectraCreatorDetails:
        """Special nested class for casting ExcelBatchDutyCycleSpectraCreatorDetails to subclasses."""

        def __init__(
            self: "ExcelBatchDutyCycleSpectraCreatorDetails._Cast_ExcelBatchDutyCycleSpectraCreatorDetails",
            parent: "ExcelBatchDutyCycleSpectraCreatorDetails",
        ):
            self._parent = parent

        @property
        def excel_batch_duty_cycle_spectra_creator_details(
            self: "ExcelBatchDutyCycleSpectraCreatorDetails._Cast_ExcelBatchDutyCycleSpectraCreatorDetails",
        ) -> "ExcelBatchDutyCycleSpectraCreatorDetails":
            return self._parent

        def __getattr__(
            self: "ExcelBatchDutyCycleSpectraCreatorDetails._Cast_ExcelBatchDutyCycleSpectraCreatorDetails",
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
        self: Self, instance_to_wrap: "ExcelBatchDutyCycleSpectraCreatorDetails.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excel_files_found(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcelFilesFound

        if temp is None:
            return 0

        return temp

    @property
    def folder(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Folder

        if temp is None:
            return ""

        return temp

    @property
    def excel_file_details(self: Self) -> "_6547.ExcelFileDetails":
        """mastapy.system_model.analyses_and_results.duty_cycles.excel_batch_duty_cycles.ExcelFileDetails

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcelFileDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def masta_file_details(self: Self) -> "_6550.MASTAFileDetails":
        """mastapy.system_model.analyses_and_results.duty_cycles.excel_batch_duty_cycles.MASTAFileDetails

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MASTAFileDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def working_folder(self: Self) -> "_1606.SelectableFolder":
        """mastapy.utility.SelectableFolder

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingFolder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def excel_sheet_design_state_selection(
        self: Self,
    ) -> "List[_6549.ExcelSheetDesignStateSelector]":
        """List[mastapy.system_model.analyses_and_results.duty_cycles.excel_batch_duty_cycles.ExcelSheetDesignStateSelector]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcelSheetDesignStateSelection

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

    def edit_folder_path(self: Self):
        """Method does not return."""
        self.wrapped.EditFolderPath()

    def prepare_working_folder(self: Self):
        """Method does not return."""
        self.wrapped.PrepareWorkingFolder()

    def write_masta_files(self: Self):
        """Method does not return."""
        self.wrapped.WriteMASTAFiles()

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
    ) -> "ExcelBatchDutyCycleSpectraCreatorDetails._Cast_ExcelBatchDutyCycleSpectraCreatorDetails":
        return self._Cast_ExcelBatchDutyCycleSpectraCreatorDetails(self)
