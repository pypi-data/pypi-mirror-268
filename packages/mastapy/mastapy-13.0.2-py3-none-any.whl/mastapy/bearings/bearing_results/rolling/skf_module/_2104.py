"""SKFCredentials"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SKF_CREDENTIALS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "SKFCredentials"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import _2102


__docformat__ = "restructuredtext en"
__all__ = ("SKFCredentials",)


Self = TypeVar("Self", bound="SKFCredentials")


class SKFCredentials(_0.APIBase):
    """SKFCredentials

    This is a mastapy class.
    """

    TYPE = _SKF_CREDENTIALS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SKFCredentials")

    class _Cast_SKFCredentials:
        """Special nested class for casting SKFCredentials to subclasses."""

        def __init__(
            self: "SKFCredentials._Cast_SKFCredentials", parent: "SKFCredentials"
        ):
            self._parent = parent

        @property
        def skf_credentials(
            self: "SKFCredentials._Cast_SKFCredentials",
        ) -> "SKFCredentials":
            return self._parent

        def __getattr__(self: "SKFCredentials._Cast_SKFCredentials", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SKFCredentials.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def email_address(self: Self) -> "str":
        """str"""
        temp = self.wrapped.EmailAddress

        if temp is None:
            return ""

        return temp

    @email_address.setter
    @enforce_parameter_types
    def email_address(self: Self, value: "str"):
        self.wrapped.EmailAddress = str(value) if value is not None else ""

    @property
    def password(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Password

        if temp is None:
            return ""

        return temp

    @password.setter
    @enforce_parameter_types
    def password(self: Self, value: "str"):
        self.wrapped.Password = str(value) if value is not None else ""

    @property
    def read_ampersand_accept_terms_of_use(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ReadAmpersandAcceptTermsOfUse

        if temp is None:
            return False

        return temp

    @read_ampersand_accept_terms_of_use.setter
    @enforce_parameter_types
    def read_ampersand_accept_terms_of_use(self: Self, value: "bool"):
        self.wrapped.ReadAmpersandAcceptTermsOfUse = (
            bool(value) if value is not None else False
        )

    @property
    def skf_authentication(self: Self) -> "_2102.SKFAuthentication":
        """mastapy.bearings.bearing_results.rolling.skf_module.SKFAuthentication

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFAuthentication

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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

    def authenticate(self: Self):
        """Method does not return."""
        self.wrapped.Authenticate()

    def create_skf_account(self: Self):
        """Method does not return."""
        self.wrapped.CreateSKFAccount()

    def skf_privacy_notice(self: Self):
        """Method does not return."""
        self.wrapped.SKFPrivacyNotice()

    def skf_terms_of_use(self: Self):
        """Method does not return."""
        self.wrapped.SKFTermsOfUse()

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
    def cast_to(self: Self) -> "SKFCredentials._Cast_SKFCredentials":
        return self._Cast_SKFCredentials(self)
