"""FESubstructureVersionComparer"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_VERSION_COMPARER = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.VersionComparer", "FESubstructureVersionComparer"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.version_comparer import _2423, _2419


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureVersionComparer",)


Self = TypeVar("Self", bound="FESubstructureVersionComparer")


class FESubstructureVersionComparer(_0.APIBase):
    """FESubstructureVersionComparer

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_VERSION_COMPARER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FESubstructureVersionComparer")

    class _Cast_FESubstructureVersionComparer:
        """Special nested class for casting FESubstructureVersionComparer to subclasses."""

        def __init__(
            self: "FESubstructureVersionComparer._Cast_FESubstructureVersionComparer",
            parent: "FESubstructureVersionComparer",
        ):
            self._parent = parent

        @property
        def fe_substructure_version_comparer(
            self: "FESubstructureVersionComparer._Cast_FESubstructureVersionComparer",
        ) -> "FESubstructureVersionComparer":
            return self._parent

        def __getattr__(
            self: "FESubstructureVersionComparer._Cast_FESubstructureVersionComparer",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FESubstructureVersionComparer.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def check_all_files_in_directory(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CheckAllFilesInDirectory

        if temp is None:
            return False

        return temp

    @check_all_files_in_directory.setter
    @enforce_parameter_types
    def check_all_files_in_directory(self: Self, value: "bool"):
        self.wrapped.CheckAllFilesInDirectory = (
            bool(value) if value is not None else False
        )

    @property
    def file(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.File

        if temp is None:
            return ""

        return temp

    @property
    def folder_path_for_saved_files(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FolderPathForSavedFiles

        if temp is None:
            return ""

        return temp

    @property
    def load_cases_to_run(self: Self) -> "_2423.LoadCasesToRun":
        """mastapy.system_model.fe.version_comparer.LoadCasesToRun"""
        temp = self.wrapped.LoadCasesToRun

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.FE.VersionComparer.LoadCasesToRun"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.fe.version_comparer._2423", "LoadCasesToRun"
        )(value)

    @load_cases_to_run.setter
    @enforce_parameter_types
    def load_cases_to_run(self: Self, value: "_2423.LoadCasesToRun"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.FE.VersionComparer.LoadCasesToRun"
        )
        self.wrapped.LoadCasesToRun = value

    @property
    def save_new_design_files(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SaveNewDesignFiles

        if temp is None:
            return False

        return temp

    @save_new_design_files.setter
    @enforce_parameter_types
    def save_new_design_files(self: Self, value: "bool"):
        self.wrapped.SaveNewDesignFiles = bool(value) if value is not None else False

    @property
    def status(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return ""

        return temp

    @property
    def design_results(self: Self) -> "List[_2419.DesignResults]":
        """List[mastapy.system_model.fe.version_comparer.DesignResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignResults

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

    def edit_folder_path(self: Self):
        """Method does not return."""
        self.wrapped.EditFolderPath()

    def run(self: Self):
        """Method does not return."""
        self.wrapped.Run()

    def select_file(self: Self):
        """Method does not return."""
        self.wrapped.SelectFile()

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
    ) -> "FESubstructureVersionComparer._Cast_FESubstructureVersionComparer":
        return self._Cast_FESubstructureVersionComparer(self)
