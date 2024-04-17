"""BatchOperations"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Optional, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BATCH_OPERATIONS = python_net_import("SMT.MastaAPI.SystemModel.FE", "BatchOperations")

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2387


__docformat__ = "restructuredtext en"
__all__ = ("BatchOperations",)


Self = TypeVar("Self", bound="BatchOperations")


class BatchOperations(_0.APIBase):
    """BatchOperations

    This is a mastapy class.
    """

    TYPE = _BATCH_OPERATIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BatchOperations")

    class _Cast_BatchOperations:
        """Special nested class for casting BatchOperations to subclasses."""

        def __init__(
            self: "BatchOperations._Cast_BatchOperations", parent: "BatchOperations"
        ):
            self._parent = parent

        @property
        def batch_operations(
            self: "BatchOperations._Cast_BatchOperations",
        ) -> "BatchOperations":
            return self._parent

        def __getattr__(self: "BatchOperations._Cast_BatchOperations", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BatchOperations.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def all_selected(self: Self) -> "Optional[bool]":
        """Optional[bool]"""
        temp = self.wrapped.AllSelected

        if temp is None:
            return None

        return temp

    @all_selected.setter
    @enforce_parameter_types
    def all_selected(self: Self, value: "Optional[bool]"):
        self.wrapped.AllSelected = value

    @property
    def select_all_to_be_unloaded(self: Self) -> "Optional[bool]":
        """Optional[bool]"""
        temp = self.wrapped.SelectAllToBeUnloaded

        if temp is None:
            return None

        return temp

    @select_all_to_be_unloaded.setter
    @enforce_parameter_types
    def select_all_to_be_unloaded(self: Self, value: "Optional[bool]"):
        self.wrapped.SelectAllToBeUnloaded = value

    @property
    def total_memory_for_all_files_selected_to_unload(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalMemoryForAllFilesSelectedToUnload

        if temp is None:
            return ""

        return temp

    @property
    def total_memory_for_all_loaded_external_f_es(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalMemoryForAllLoadedExternalFEs

        if temp is None:
            return ""

        return temp

    @property
    def fe_parts(self: Self) -> "List[_2387.FEPartWithBatchOptions]":
        """List[mastapy.system_model.fe.FEPartWithBatchOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def fe_parts_with_external_files(
        self: Self,
    ) -> "List[_2387.FEPartWithBatchOptions]":
        """List[mastapy.system_model.fe.FEPartWithBatchOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEPartsWithExternalFiles

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

    def load_all_selected_external_files(self: Self):
        """Method does not return."""
        self.wrapped.LoadAllSelectedExternalFiles()

    def perform_reduction_for_selected(self: Self):
        """Method does not return."""
        self.wrapped.PerformReductionForSelected()

    def remove_all_full_fe_meshes_in_design(self: Self):
        """Method does not return."""
        self.wrapped.RemoveAllFullFEMeshesInDesign()

    def unload_all_selected_external_files(self: Self):
        """Method does not return."""
        self.wrapped.UnloadAllSelectedExternalFiles()

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
    def cast_to(self: Self) -> "BatchOperations._Cast_BatchOperations":
        return self._Cast_BatchOperations(self)
