"""Status"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATUS = python_net_import("SMT.MastaAPI.Utility.ModelValidation", "Status")

if TYPE_CHECKING:
    from mastapy.utility.model_validation import _1801


__docformat__ = "restructuredtext en"
__all__ = ("Status",)


Self = TypeVar("Self", bound="Status")


class Status(_0.APIBase):
    """Status

    This is a mastapy class.
    """

    TYPE = _STATUS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Status")

    class _Cast_Status:
        """Special nested class for casting Status to subclasses."""

        def __init__(self: "Status._Cast_Status", parent: "Status"):
            self._parent = parent

        @property
        def status(self: "Status._Cast_Status") -> "Status":
            return self._parent

        def __getattr__(self: "Status._Cast_Status", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Status.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def error_count(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ErrorCount

        if temp is None:
            return 0

        return temp

    @property
    def has_errors_or_warnings(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasErrorsOrWarnings

        if temp is None:
            return False

        return temp

    @property
    def has_errors(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasErrors

        if temp is None:
            return False

        return temp

    @property
    def has_information(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasInformation

        if temp is None:
            return False

        return temp

    @property
    def has_warnings(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasWarnings

        if temp is None:
            return False

        return temp

    @property
    def information_count(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InformationCount

        if temp is None:
            return 0

        return temp

    @property
    def warning_count(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WarningCount

        if temp is None:
            return 0

        return temp

    @property
    def errors(self: Self) -> "List[_1801.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Errors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def warnings(self: Self) -> "List[_1801.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Warnings

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
    def cast_to(self: Self) -> "Status._Cast_Status":
        return self._Cast_Status(self)
