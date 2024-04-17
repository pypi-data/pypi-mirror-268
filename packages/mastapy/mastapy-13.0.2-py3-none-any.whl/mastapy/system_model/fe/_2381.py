"""ElectricMachineDynamicLoadData"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Optional

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.electric_machines import _1302
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_DYNAMIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "ElectricMachineDynamicLoadData"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2380
    from mastapy.electric_machines.load_cases_and_analyses import _1354, _1363


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineDynamicLoadData",)


Self = TypeVar("Self", bound="ElectricMachineDynamicLoadData")


class ElectricMachineDynamicLoadData(_0.APIBase):
    """ElectricMachineDynamicLoadData

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_DYNAMIC_LOAD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineDynamicLoadData")

    class _Cast_ElectricMachineDynamicLoadData:
        """Special nested class for casting ElectricMachineDynamicLoadData to subclasses."""

        def __init__(
            self: "ElectricMachineDynamicLoadData._Cast_ElectricMachineDynamicLoadData",
            parent: "ElectricMachineDynamicLoadData",
        ):
            self._parent = parent

        @property
        def electric_machine_dynamic_load_data(
            self: "ElectricMachineDynamicLoadData._Cast_ElectricMachineDynamicLoadData",
        ) -> "ElectricMachineDynamicLoadData":
            return self._parent

        def __getattr__(
            self: "ElectricMachineDynamicLoadData._Cast_ElectricMachineDynamicLoadData",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineDynamicLoadData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def slice(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_RotorSkewSlice":
        """ListWithSelectedItem[mastapy.electric_machines.RotorSkewSlice]"""
        temp = self.wrapped.Slice

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_RotorSkewSlice",
        )(temp)

    @slice.setter
    @enforce_parameter_types
    def slice(self: Self, value: "_1302.RotorSkewSlice"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Slice = value

    @property
    def electric_machine_data_sets(self: Self) -> "List[_2380.ElectricMachineDataSet]":
        """List[mastapy.system_model.fe.ElectricMachineDataSet]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineDataSets

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
    def add_electric_machine_data_set(
        self: Self, name: "str"
    ) -> "_2380.ElectricMachineDataSet":
        """mastapy.system_model.fe.ElectricMachineDataSet

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.AddElectricMachineDataSet(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def add_electric_machine_data_set_from_masta_dynamic_force_analysis(
        self: Self, analysis: "_1354.DynamicForceAnalysis", slice_index: "Optional[int]"
    ) -> "_2380.ElectricMachineDataSet":
        """mastapy.system_model.fe.ElectricMachineDataSet

        Args:
            analysis (mastapy.electric_machines.load_cases_and_analyses.DynamicForceAnalysis)
            slice_index (Optional[int])
        """
        method_result = (
            self.wrapped.AddElectricMachineDataSetFromMASTADynamicForceAnalysis(
                analysis.wrapped if analysis else None, slice_index
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def add_electric_machine_data_set_from_masta_electric_machine_fe_analysis(
        self: Self,
        analysis: "_1363.ElectricMachineFEAnalysis",
        slice_index: "Optional[int]",
    ) -> "_2380.ElectricMachineDataSet":
        """mastapy.system_model.fe.ElectricMachineDataSet

        Args:
            analysis (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineFEAnalysis)
            slice_index (Optional[int])
        """
        method_result = (
            self.wrapped.AddElectricMachineDataSetFromMASTAElectricMachineFEAnalysis(
                analysis.wrapped if analysis else None, slice_index
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def delete_all_data_sets(self: Self):
        """Method does not return."""
        self.wrapped.DeleteAllDataSets()

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
    ) -> "ElectricMachineDynamicLoadData._Cast_ElectricMachineDynamicLoadData":
        return self._Cast_ElectricMachineDynamicLoadData(self)
