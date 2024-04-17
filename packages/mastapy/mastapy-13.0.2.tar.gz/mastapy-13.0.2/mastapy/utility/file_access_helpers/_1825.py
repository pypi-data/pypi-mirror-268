"""TextFileDelimiterOptions"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TEXT_FILE_DELIMITER_OPTIONS = python_net_import(
    "SMT.MastaAPI.Utility.FileAccessHelpers", "TextFileDelimiterOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("TextFileDelimiterOptions",)


Self = TypeVar("Self", bound="TextFileDelimiterOptions")


class TextFileDelimiterOptions(_0.APIBase):
    """TextFileDelimiterOptions

    This is a mastapy class.
    """

    TYPE = _TEXT_FILE_DELIMITER_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TextFileDelimiterOptions")

    class _Cast_TextFileDelimiterOptions:
        """Special nested class for casting TextFileDelimiterOptions to subclasses."""

        def __init__(
            self: "TextFileDelimiterOptions._Cast_TextFileDelimiterOptions",
            parent: "TextFileDelimiterOptions",
        ):
            self._parent = parent

        @property
        def text_file_delimiter_options(
            self: "TextFileDelimiterOptions._Cast_TextFileDelimiterOptions",
        ) -> "TextFileDelimiterOptions":
            return self._parent

        def __getattr__(
            self: "TextFileDelimiterOptions._Cast_TextFileDelimiterOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TextFileDelimiterOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def other(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Other

        if temp is None:
            return ""

        return temp

    @other.setter
    @enforce_parameter_types
    def other(self: Self, value: "str"):
        self.wrapped.Other = str(value) if value is not None else ""

    @property
    def treat_consecutive_delimiters_as_one(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.TreatConsecutiveDelimitersAsOne

        if temp is None:
            return False

        return temp

    @treat_consecutive_delimiters_as_one.setter
    @enforce_parameter_types
    def treat_consecutive_delimiters_as_one(self: Self, value: "bool"):
        self.wrapped.TreatConsecutiveDelimitersAsOne = (
            bool(value) if value is not None else False
        )

    @property
    def use_comma(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseComma

        if temp is None:
            return False

        return temp

    @use_comma.setter
    @enforce_parameter_types
    def use_comma(self: Self, value: "bool"):
        self.wrapped.UseComma = bool(value) if value is not None else False

    @property
    def use_semi_colon(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSemiColon

        if temp is None:
            return False

        return temp

    @use_semi_colon.setter
    @enforce_parameter_types
    def use_semi_colon(self: Self, value: "bool"):
        self.wrapped.UseSemiColon = bool(value) if value is not None else False

    @property
    def use_space(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSpace

        if temp is None:
            return False

        return temp

    @use_space.setter
    @enforce_parameter_types
    def use_space(self: Self, value: "bool"):
        self.wrapped.UseSpace = bool(value) if value is not None else False

    @property
    def use_tab(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseTab

        if temp is None:
            return False

        return temp

    @use_tab.setter
    @enforce_parameter_types
    def use_tab(self: Self, value: "bool"):
        self.wrapped.UseTab = bool(value) if value is not None else False

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
    ) -> "TextFileDelimiterOptions._Cast_TextFileDelimiterOptions":
        return self._Cast_TextFileDelimiterOptions(self)
