"""UserSpecifiedData"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_USER_SPECIFIED_DATA = python_net_import(
    "SMT.MastaAPI.Utility.Scripting", "UserSpecifiedData"
)


__docformat__ = "restructuredtext en"
__all__ = ("UserSpecifiedData",)


Self = TypeVar("Self", bound="UserSpecifiedData")


class UserSpecifiedData(_0.APIBase):
    """UserSpecifiedData

    This is a mastapy class.
    """

    TYPE = _USER_SPECIFIED_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UserSpecifiedData")

    class _Cast_UserSpecifiedData:
        """Special nested class for casting UserSpecifiedData to subclasses."""

        def __init__(
            self: "UserSpecifiedData._Cast_UserSpecifiedData",
            parent: "UserSpecifiedData",
        ):
            self._parent = parent

        @property
        def user_specified_data(
            self: "UserSpecifiedData._Cast_UserSpecifiedData",
        ) -> "UserSpecifiedData":
            return self._parent

        def __getattr__(self: "UserSpecifiedData._Cast_UserSpecifiedData", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UserSpecifiedData.TYPE"):
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

    def clear(self: Self):
        """Method does not return."""
        self.wrapped.Clear()

    @enforce_parameter_types
    def get_bool(self: Self, key: "str") -> "bool":
        """bool

        Args:
            key (str)
        """
        key = str(key)
        method_result = self.wrapped.GetBool(key if key else "")
        return method_result

    @enforce_parameter_types
    def get_double(self: Self, key: "str") -> "float":
        """float

        Args:
            key (str)
        """
        key = str(key)
        method_result = self.wrapped.GetDouble(key if key else "")
        return method_result

    @enforce_parameter_types
    def get_string(self: Self, key: "str") -> "str":
        """str

        Args:
            key (str)
        """
        key = str(key)
        method_result = self.wrapped.GetString(key if key else "")
        return method_result

    @enforce_parameter_types
    def has_bool(self: Self, key: "str") -> "bool":
        """bool

        Args:
            key (str)
        """
        key = str(key)
        method_result = self.wrapped.HasBool(key if key else "")
        return method_result

    @enforce_parameter_types
    def has_double(self: Self, key: "str") -> "bool":
        """bool

        Args:
            key (str)
        """
        key = str(key)
        method_result = self.wrapped.HasDouble(key if key else "")
        return method_result

    @enforce_parameter_types
    def has_string(self: Self, key: "str") -> "bool":
        """bool

        Args:
            key (str)
        """
        key = str(key)
        method_result = self.wrapped.HasString(key if key else "")
        return method_result

    @enforce_parameter_types
    def set_bool(self: Self, key: "str", value: "bool"):
        """Method does not return.

        Args:
            key (str)
            value (bool)
        """
        key = str(key)
        value = bool(value)
        self.wrapped.SetBool(key if key else "", value if value else False)

    @enforce_parameter_types
    def set_double(self: Self, key: "str", value: "float"):
        """Method does not return.

        Args:
            key (str)
            value (float)
        """
        key = str(key)
        value = float(value)
        self.wrapped.SetDouble(key if key else "", value if value else 0.0)

    @enforce_parameter_types
    def set_string(self: Self, key: "str", value: "str"):
        """Method does not return.

        Args:
            key (str)
            value (str)
        """
        key = str(key)
        value = str(value)
        self.wrapped.SetString(key if key else "", value if value else "")

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
    def cast_to(self: Self) -> "UserSpecifiedData._Cast_UserSpecifiedData":
        return self._Cast_UserSpecifiedData(self)
