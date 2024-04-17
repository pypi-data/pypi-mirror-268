"""OptionsWhenExternalFEFileAlreadyExists"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIONS_WHEN_EXTERNAL_FE_FILE_ALREADY_EXISTS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "OptionsWhenExternalFEFileAlreadyExists"
)


__docformat__ = "restructuredtext en"
__all__ = ("OptionsWhenExternalFEFileAlreadyExists",)


Self = TypeVar("Self", bound="OptionsWhenExternalFEFileAlreadyExists")


class OptionsWhenExternalFEFileAlreadyExists(_0.APIBase):
    """OptionsWhenExternalFEFileAlreadyExists

    This is a mastapy class.
    """

    TYPE = _OPTIONS_WHEN_EXTERNAL_FE_FILE_ALREADY_EXISTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_OptionsWhenExternalFEFileAlreadyExists"
    )

    class _Cast_OptionsWhenExternalFEFileAlreadyExists:
        """Special nested class for casting OptionsWhenExternalFEFileAlreadyExists to subclasses."""

        def __init__(
            self: "OptionsWhenExternalFEFileAlreadyExists._Cast_OptionsWhenExternalFEFileAlreadyExists",
            parent: "OptionsWhenExternalFEFileAlreadyExists",
        ):
            self._parent = parent

        @property
        def options_when_external_fe_file_already_exists(
            self: "OptionsWhenExternalFEFileAlreadyExists._Cast_OptionsWhenExternalFEFileAlreadyExists",
        ) -> "OptionsWhenExternalFEFileAlreadyExists":
            return self._parent

        def __getattr__(
            self: "OptionsWhenExternalFEFileAlreadyExists._Cast_OptionsWhenExternalFEFileAlreadyExists",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "OptionsWhenExternalFEFileAlreadyExists.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def append_current_date_and_time_to_new_file_names(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.AppendCurrentDateAndTimeToNewFileNames

        if temp is None:
            return False

        return temp

    @append_current_date_and_time_to_new_file_names.setter
    @enforce_parameter_types
    def append_current_date_and_time_to_new_file_names(self: Self, value: "bool"):
        self.wrapped.AppendCurrentDateAndTimeToNewFileNames = (
            bool(value) if value is not None else False
        )

    @property
    def output_mesh_file_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OutputMeshFilePath

        if temp is None:
            return ""

        return temp

    @property
    def output_vectors_file_path(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OutputVectorsFilePath

        if temp is None:
            return ""

        return temp

    @property
    def overwrite_existing_mesh_file(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverwriteExistingMeshFile

        if temp is None:
            return False

        return temp

    @overwrite_existing_mesh_file.setter
    @enforce_parameter_types
    def overwrite_existing_mesh_file(self: Self, value: "bool"):
        self.wrapped.OverwriteExistingMeshFile = (
            bool(value) if value is not None else False
        )

    @property
    def overwrite_existing_vectors_file(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverwriteExistingVectorsFile

        if temp is None:
            return False

        return temp

    @overwrite_existing_vectors_file.setter
    @enforce_parameter_types
    def overwrite_existing_vectors_file(self: Self, value: "bool"):
        self.wrapped.OverwriteExistingVectorsFile = (
            bool(value) if value is not None else False
        )

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
    ) -> "OptionsWhenExternalFEFileAlreadyExists._Cast_OptionsWhenExternalFEFileAlreadyExists":
        return self._Cast_OptionsWhenExternalFEFileAlreadyExists(self)
