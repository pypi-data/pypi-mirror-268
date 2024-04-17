"""RollingBearingImporter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_IMPORTER = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.XmlImport", "RollingBearingImporter"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling.xml_import import _2186


__docformat__ = "restructuredtext en"
__all__ = ("RollingBearingImporter",)


Self = TypeVar("Self", bound="RollingBearingImporter")


class RollingBearingImporter(_0.APIBase):
    """RollingBearingImporter

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_IMPORTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingBearingImporter")

    class _Cast_RollingBearingImporter:
        """Special nested class for casting RollingBearingImporter to subclasses."""

        def __init__(
            self: "RollingBearingImporter._Cast_RollingBearingImporter",
            parent: "RollingBearingImporter",
        ):
            self._parent = parent

        @property
        def rolling_bearing_importer(
            self: "RollingBearingImporter._Cast_RollingBearingImporter",
        ) -> "RollingBearingImporter":
            return self._parent

        def __getattr__(
            self: "RollingBearingImporter._Cast_RollingBearingImporter", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingBearingImporter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_bearings_ready_to_import(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfBearingsReadyToImport

        if temp is None:
            return 0

        return temp

    @property
    def replace_existing_bearings(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ReplaceExistingBearings

        if temp is None:
            return False

        return temp

    @replace_existing_bearings.setter
    @enforce_parameter_types
    def replace_existing_bearings(self: Self, value: "bool"):
        self.wrapped.ReplaceExistingBearings = (
            bool(value) if value is not None else False
        )

    @property
    def mappings(self: Self) -> "List[_2186.XmlBearingTypeMapping]":
        """List[mastapy.bearings.bearing_designs.rolling.xml_import.XmlBearingTypeMapping]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mappings

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

    def import_all(self: Self):
        """Method does not return."""
        self.wrapped.ImportAll()

    def load_setup(self: Self):
        """Method does not return."""
        self.wrapped.LoadSetup()

    def open_files_in_directory(self: Self):
        """Method does not return."""
        self.wrapped.OpenFilesInDirectory()

    def reset_to_defaults(self: Self):
        """Method does not return."""
        self.wrapped.ResetToDefaults()

    def save_setup(self: Self):
        """Method does not return."""
        self.wrapped.SaveSetup()

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
    def cast_to(self: Self) -> "RollingBearingImporter._Cast_RollingBearingImporter":
        return self._Cast_RollingBearingImporter(self)
