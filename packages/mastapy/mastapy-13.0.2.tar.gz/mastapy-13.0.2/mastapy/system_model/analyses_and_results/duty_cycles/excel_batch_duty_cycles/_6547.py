"""ExcelFileDetails"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.utility.units_and_measurements import _1617
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXCEL_FILE_DETAILS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DutyCycles.ExcelBatchDutyCycles",
    "ExcelFileDetails",
)


__docformat__ = "restructuredtext en"
__all__ = ("ExcelFileDetails",)


Self = TypeVar("Self", bound="ExcelFileDetails")


class ExcelFileDetails(_0.APIBase):
    """ExcelFileDetails

    This is a mastapy class.
    """

    TYPE = _EXCEL_FILE_DETAILS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExcelFileDetails")

    class _Cast_ExcelFileDetails:
        """Special nested class for casting ExcelFileDetails to subclasses."""

        def __init__(
            self: "ExcelFileDetails._Cast_ExcelFileDetails", parent: "ExcelFileDetails"
        ):
            self._parent = parent

        @property
        def excel_file_details(
            self: "ExcelFileDetails._Cast_ExcelFileDetails",
        ) -> "ExcelFileDetails":
            return self._parent

        def __getattr__(self: "ExcelFileDetails._Cast_ExcelFileDetails", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExcelFileDetails.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def combine_positive_and_negative_speeds(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CombinePositiveAndNegativeSpeeds

        if temp is None:
            return False

        return temp

    @combine_positive_and_negative_speeds.setter
    @enforce_parameter_types
    def combine_positive_and_negative_speeds(self: Self, value: "bool"):
        self.wrapped.CombinePositiveAndNegativeSpeeds = (
            bool(value) if value is not None else False
        )

    @property
    def compress_load_cases(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CompressLoadCases

        if temp is None:
            return False

        return temp

    @compress_load_cases.setter
    @enforce_parameter_types
    def compress_load_cases(self: Self, value: "bool"):
        self.wrapped.CompressLoadCases = bool(value) if value is not None else False

    @property
    def cycles_unit(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.CyclesUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @cycles_unit.setter
    @enforce_parameter_types
    def cycles_unit(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.CyclesUnit = value

    @property
    def duration_unit(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.DurationUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @duration_unit.setter
    @enforce_parameter_types
    def duration_unit(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.DurationUnit = value

    @property
    def first_data_column(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.FirstDataColumn

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @first_data_column.setter
    @enforce_parameter_types
    def first_data_column(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.FirstDataColumn = value

    @property
    def first_data_row(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.FirstDataRow

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @first_data_row.setter
    @enforce_parameter_types
    def first_data_row(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.FirstDataRow = value

    @property
    def header_column(self: Self) -> "int":
        """int"""
        temp = self.wrapped.HeaderColumn

        if temp is None:
            return 0

        return temp

    @header_column.setter
    @enforce_parameter_types
    def header_column(self: Self, value: "int"):
        self.wrapped.HeaderColumn = int(value) if value is not None else 0

    @property
    def header_row(self: Self) -> "int":
        """int"""
        temp = self.wrapped.HeaderRow

        if temp is None:
            return 0

        return temp

    @header_row.setter
    @enforce_parameter_types
    def header_row(self: Self, value: "int"):
        self.wrapped.HeaderRow = int(value) if value is not None else 0

    @property
    def ignore_sheet_names_containing(self: Self) -> "str":
        """str"""
        temp = self.wrapped.IgnoreSheetNamesContaining

        if temp is None:
            return ""

        return temp

    @ignore_sheet_names_containing.setter
    @enforce_parameter_types
    def ignore_sheet_names_containing(self: Self, value: "str"):
        self.wrapped.IgnoreSheetNamesContaining = (
            str(value) if value is not None else ""
        )

    @property
    def negate_speeds_and_torques(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.NegateSpeedsAndTorques

        if temp is None:
            return False

        return temp

    @negate_speeds_and_torques.setter
    @enforce_parameter_types
    def negate_speeds_and_torques(self: Self, value: "bool"):
        self.wrapped.NegateSpeedsAndTorques = (
            bool(value) if value is not None else False
        )

    @property
    def number_of_data_columns(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfDataColumns

        if temp is None:
            return 0

        return temp

    @number_of_data_columns.setter
    @enforce_parameter_types
    def number_of_data_columns(self: Self, value: "int"):
        self.wrapped.NumberOfDataColumns = int(value) if value is not None else 0

    @property
    def number_of_data_rows(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfDataRows

        if temp is None:
            return 0

        return temp

    @number_of_data_rows.setter
    @enforce_parameter_types
    def number_of_data_rows(self: Self, value: "int"):
        self.wrapped.NumberOfDataRows = int(value) if value is not None else 0

    @property
    def show_zero_duration_speeds_and_torques(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowZeroDurationSpeedsAndTorques

        if temp is None:
            return False

        return temp

    @show_zero_duration_speeds_and_torques.setter
    @enforce_parameter_types
    def show_zero_duration_speeds_and_torques(self: Self, value: "bool"):
        self.wrapped.ShowZeroDurationSpeedsAndTorques = (
            bool(value) if value is not None else False
        )

    @property
    def specify_duration(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyDuration

        if temp is None:
            return False

        return temp

    @specify_duration.setter
    @enforce_parameter_types
    def specify_duration(self: Self, value: "bool"):
        self.wrapped.SpecifyDuration = bool(value) if value is not None else False

    @property
    def specify_number_of_data_rows_and_columns(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyNumberOfDataRowsAndColumns

        if temp is None:
            return False

        return temp

    @specify_number_of_data_rows_and_columns.setter
    @enforce_parameter_types
    def specify_number_of_data_rows_and_columns(self: Self, value: "bool"):
        self.wrapped.SpecifyNumberOfDataRowsAndColumns = (
            bool(value) if value is not None else False
        )

    @property
    def speed_unit(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.SpeedUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @speed_unit.setter
    @enforce_parameter_types
    def speed_unit(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SpeedUnit = value

    @property
    def torque_unit(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.TorqueUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @torque_unit.setter
    @enforce_parameter_types
    def torque_unit(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.TorqueUnit = value

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
    def cast_to(self: Self) -> "ExcelFileDetails._Cast_ExcelFileDetails":
        return self._Cast_ExcelFileDetails(self)
