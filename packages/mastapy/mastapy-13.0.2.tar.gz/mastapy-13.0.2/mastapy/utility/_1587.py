"""EnvironmentSummary"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENVIRONMENT_SUMMARY = python_net_import("SMT.MastaAPI.Utility", "EnvironmentSummary")

if TYPE_CHECKING:
    from mastapy.utility import _1600, _1586


__docformat__ = "restructuredtext en"
__all__ = ("EnvironmentSummary",)


Self = TypeVar("Self", bound="EnvironmentSummary")


class EnvironmentSummary(_0.APIBase):
    """EnvironmentSummary

    This is a mastapy class.
    """

    TYPE = _ENVIRONMENT_SUMMARY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EnvironmentSummary")

    class _Cast_EnvironmentSummary:
        """Special nested class for casting EnvironmentSummary to subclasses."""

        def __init__(
            self: "EnvironmentSummary._Cast_EnvironmentSummary",
            parent: "EnvironmentSummary",
        ):
            self._parent = parent

        @property
        def environment_summary(
            self: "EnvironmentSummary._Cast_EnvironmentSummary",
        ) -> "EnvironmentSummary":
            return self._parent

        def __getattr__(self: "EnvironmentSummary._Cast_EnvironmentSummary", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EnvironmentSummary.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def build_date(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BuildDate

        if temp is None:
            return ""

        return temp

    @property
    def build_date_and_age(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BuildDateAndAge

        if temp is None:
            return ""

        return temp

    @property
    def command_line(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CommandLine

        if temp is None:
            return ""

        return temp

    @property
    def core_feature_code_in_use(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoreFeatureCodeInUse

        if temp is None:
            return ""

        return temp

    @property
    def core_feature_expiry(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoreFeatureExpiry

        if temp is None:
            return ""

        return temp

    @property
    def current_net_version(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentNETVersion

        if temp is None:
            return ""

        return temp

    @property
    def current_culture_system_locale(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentCultureSystemLocale

        if temp is None:
            return ""

        return temp

    @property
    def current_ui_culture_system_locale(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentUICultureSystemLocale

        if temp is None:
            return ""

        return temp

    @property
    def date_time_iso8601(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DateTimeISO8601

        if temp is None:
            return ""

        return temp

    @property
    def date_time_local_format(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DateTimeLocalFormat

        if temp is None:
            return ""

        return temp

    @property
    def dispatcher_information(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DispatcherInformation

        if temp is None:
            return ""

        return temp

    @property
    def entry_assembly(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EntryAssembly

        if temp is None:
            return ""

        return temp

    @property
    def executable_directory(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExecutableDirectory

        if temp is None:
            return ""

        return temp

    @property
    def executable_directory_is_network_path(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExecutableDirectoryIsNetworkPath

        if temp is None:
            return False

        return temp

    @property
    def installed_video_controllers(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InstalledVideoControllers

        if temp is None:
            return ""

        return temp

    @property
    def is_64_bit_operating_system(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Is64BitOperatingSystem

        if temp is None:
            return False

        return temp

    @property
    def licence_key(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LicenceKey

        if temp is None:
            return ""

        return temp

    @property
    def masta_version(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MASTAVersion

        if temp is None:
            return ""

        return temp

    @property
    def machine_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MachineName

        if temp is None:
            return ""

        return temp

    @property
    def open_gl_renderer(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OpenGLRenderer

        if temp is None:
            return ""

        return temp

    @property
    def open_gl_vendor(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OpenGLVendor

        if temp is None:
            return ""

        return temp

    @property
    def open_gl_version(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OpenGLVersion

        if temp is None:
            return ""

        return temp

    @property
    def operating_system(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingSystem

        if temp is None:
            return ""

        return temp

    @property
    def prerequisites(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Prerequisites

        if temp is None:
            return ""

        return temp

    @property
    def process_render_mode(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProcessRenderMode

        if temp is None:
            return ""

        return temp

    @property
    def processor(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Processor

        if temp is None:
            return ""

        return temp

    @property
    def ram(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RAM

        if temp is None:
            return ""

        return temp

    @property
    def remote_desktop_information(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RemoteDesktopInformation

        if temp is None:
            return ""

        return temp

    @property
    def start_date_time_and_age(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StartDateTimeAndAge

        if temp is None:
            return ""

        return temp

    @property
    def user_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserName

        if temp is None:
            return ""

        return temp

    @property
    def video_controller_in_use(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VideoControllerInUse

        if temp is None:
            return ""

        return temp

    @property
    def current_culture(self: Self) -> "_1600.NumberFormatInfoSummary":
        """mastapy.utility.NumberFormatInfoSummary

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentCulture

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def dispatchers(self: Self) -> "List[_1586.DispatcherHelper]":
        """List[mastapy.utility.DispatcherHelper]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Dispatchers

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

    def __copy__(self: Self):
        """Method does not return."""
        self.wrapped.Copy()

    def __deepcopy__(self: Self, memo):
        """Method does not return."""
        self.wrapped.Copy()

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
    def cast_to(self: Self) -> "EnvironmentSummary._Cast_EnvironmentSummary":
        return self._Cast_EnvironmentSummary(self)
