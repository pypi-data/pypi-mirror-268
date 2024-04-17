"""SKFAuthentication"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SKF_AUTHENTICATION = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "SKFAuthentication"
)


__docformat__ = "restructuredtext en"
__all__ = ("SKFAuthentication",)


Self = TypeVar("Self", bound="SKFAuthentication")


class SKFAuthentication(_0.APIBase):
    """SKFAuthentication

    This is a mastapy class.
    """

    TYPE = _SKF_AUTHENTICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SKFAuthentication")

    class _Cast_SKFAuthentication:
        """Special nested class for casting SKFAuthentication to subclasses."""

        def __init__(
            self: "SKFAuthentication._Cast_SKFAuthentication",
            parent: "SKFAuthentication",
        ):
            self._parent = parent

        @property
        def skf_authentication(
            self: "SKFAuthentication._Cast_SKFAuthentication",
        ) -> "SKFAuthentication":
            return self._parent

        def __getattr__(self: "SKFAuthentication._Cast_SKFAuthentication", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SKFAuthentication.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def authentication_expiry_date(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuthenticationExpiryDate

        if temp is None:
            return ""

        return temp

    @property
    def authentication_state(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuthenticationState

        if temp is None:
            return ""

        return temp

    @property
    def error(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Error

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
    def cast_to(self: Self) -> "SKFAuthentication._Cast_SKFAuthentication":
        return self._Cast_SKFAuthentication(self)
