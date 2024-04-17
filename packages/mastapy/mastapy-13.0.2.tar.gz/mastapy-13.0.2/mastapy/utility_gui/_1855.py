"""DataInputFileOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_INPUT_FILE_OPTIONS = python_net_import(
    "SMT.MastaAPI.UtilityGUI", "DataInputFileOptions"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2565
    from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _7005,
    )


__docformat__ = "restructuredtext en"
__all__ = ("DataInputFileOptions",)


Self = TypeVar("Self", bound="DataInputFileOptions")


class DataInputFileOptions(_0.APIBase):
    """DataInputFileOptions

    This is a mastapy class.
    """

    TYPE = _DATA_INPUT_FILE_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DataInputFileOptions")

    class _Cast_DataInputFileOptions:
        """Special nested class for casting DataInputFileOptions to subclasses."""

        def __init__(
            self: "DataInputFileOptions._Cast_DataInputFileOptions",
            parent: "DataInputFileOptions",
        ):
            self._parent = parent

        @property
        def rotor_set_data_input_file_options(
            self: "DataInputFileOptions._Cast_DataInputFileOptions",
        ) -> "_2565.RotorSetDataInputFileOptions":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2565,
            )

            return self._parent._cast(_2565.RotorSetDataInputFileOptions)

        @property
        def multi_time_series_data_input_file_options(
            self: "DataInputFileOptions._Cast_DataInputFileOptions",
        ) -> "_7005.MultiTimeSeriesDataInputFileOptions":
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
                _7005,
            )

            return self._parent._cast(_7005.MultiTimeSeriesDataInputFileOptions)

        @property
        def data_input_file_options(
            self: "DataInputFileOptions._Cast_DataInputFileOptions",
        ) -> "DataInputFileOptions":
            return self._parent

        def __getattr__(
            self: "DataInputFileOptions._Cast_DataInputFileOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DataInputFileOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def column_headers_row(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ColumnHeadersRow

        if temp is None:
            return 0

        return temp

    @column_headers_row.setter
    @enforce_parameter_types
    def column_headers_row(self: Self, value: "int"):
        self.wrapped.ColumnHeadersRow = int(value) if value is not None else 0

    @property
    def data_end_row(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.DataEndRow

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @data_end_row.setter
    @enforce_parameter_types
    def data_end_row(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.DataEndRow = value

    @property
    def data_start_row(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.DataStartRow

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @data_start_row.setter
    @enforce_parameter_types
    def data_start_row(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.DataStartRow = value

    @property
    def selected_file_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.SelectedFileName

        if temp is None:
            return ""

        return temp

    @selected_file_name.setter
    @enforce_parameter_types
    def selected_file_name(self: Self, value: "str"):
        self.wrapped.SelectedFileName = str(value) if value is not None else ""

    @property
    def sheet(self: Self) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.Sheet

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @sheet.setter
    @enforce_parameter_types
    def sheet(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.Sheet = value

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
    def open_file(self: Self, filename: "str"):
        """Method does not return.

        Args:
            filename (str)
        """
        filename = str(filename)
        self.wrapped.OpenFile(filename if filename else "")

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
    def cast_to(self: Self) -> "DataInputFileOptions._Cast_DataInputFileOptions":
        return self._Cast_DataInputFileOptions(self)
