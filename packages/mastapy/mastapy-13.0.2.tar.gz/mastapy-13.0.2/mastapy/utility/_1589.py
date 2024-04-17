"""FileHistory"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FILE_HISTORY = python_net_import("SMT.MastaAPI.Utility", "FileHistory")

if TYPE_CHECKING:
    from mastapy.utility import _1590


__docformat__ = "restructuredtext en"
__all__ = ("FileHistory",)


Self = TypeVar("Self", bound="FileHistory")


class FileHistory(_0.APIBase):
    """FileHistory

    This is a mastapy class.
    """

    TYPE = _FILE_HISTORY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FileHistory")

    class _Cast_FileHistory:
        """Special nested class for casting FileHistory to subclasses."""

        def __init__(self: "FileHistory._Cast_FileHistory", parent: "FileHistory"):
            self._parent = parent

        @property
        def file_history(self: "FileHistory._Cast_FileHistory") -> "FileHistory":
            return self._parent

        def __getattr__(self: "FileHistory._Cast_FileHistory", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FileHistory.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_history_items(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfHistoryItems

        if temp is None:
            return 0

        return temp

    @property
    def items(self: Self) -> "List[_1590.FileHistoryItem]":
        """List[mastapy.utility.FileHistoryItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Items

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

    def clear_history(self: Self):
        """Method does not return."""
        self.wrapped.ClearHistory()

    @enforce_parameter_types
    def add_file_history_item(self: Self, item: "_1590.FileHistoryItem"):
        """Method does not return.

        Args:
            item (mastapy.utility.FileHistoryItem)
        """
        self.wrapped.AddFileHistoryItem(item.wrapped if item else None)

    @enforce_parameter_types
    def add_history_item(self: Self, user_name: "str", comment: "str"):
        """Method does not return.

        Args:
            user_name (str)
            comment (str)
        """
        user_name = str(user_name)
        comment = str(comment)
        self.wrapped.AddHistoryItem(
            user_name if user_name else "", comment if comment else ""
        )

    @enforce_parameter_types
    def create_history_item(
        self: Self, user_name: "str", comment: "str"
    ) -> "_1590.FileHistoryItem":
        """mastapy.utility.FileHistoryItem

        Args:
            user_name (str)
            comment (str)
        """
        user_name = str(user_name)
        comment = str(comment)
        method_result = self.wrapped.CreateHistoryItem(
            user_name if user_name else "", comment if comment else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

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
    def cast_to(self: Self) -> "FileHistory._Cast_FileHistory":
        return self._Cast_FileHistory(self)
