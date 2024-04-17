"""SystemDeflectionFEExportOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, List
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.nodal_analysis.fe_export_utility import _168, _169
from mastapy.utility.units_and_measurements import _1617
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_DEFLECTION_FE_EXPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "SystemDeflectionFEExportOptions"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2411, _2412


__docformat__ = "restructuredtext en"
__all__ = ("SystemDeflectionFEExportOptions",)


Self = TypeVar("Self", bound="SystemDeflectionFEExportOptions")


class SystemDeflectionFEExportOptions(_0.APIBase):
    """SystemDeflectionFEExportOptions

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DEFLECTION_FE_EXPORT_OPTIONS

    class ExportType(Enum):
        """ExportType is a nested enum."""

        @classmethod
        def type_(cls):
            return _SYSTEM_DEFLECTION_FE_EXPORT_OPTIONS.ExportType

        BOUNDARY_CONDITIONS_FOR_FE_SOLVER = 0
        FULL_MESH_RESULTS_AS_OP2_FILE = 1

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    ExportType.__setattr__ = __enum_setattr
    ExportType.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SystemDeflectionFEExportOptions")

    class _Cast_SystemDeflectionFEExportOptions:
        """Special nested class for casting SystemDeflectionFEExportOptions to subclasses."""

        def __init__(
            self: "SystemDeflectionFEExportOptions._Cast_SystemDeflectionFEExportOptions",
            parent: "SystemDeflectionFEExportOptions",
        ):
            self._parent = parent

        @property
        def system_deflection_fe_export_options(
            self: "SystemDeflectionFEExportOptions._Cast_SystemDeflectionFEExportOptions",
        ) -> "SystemDeflectionFEExportOptions":
            return self._parent

        def __getattr__(
            self: "SystemDeflectionFEExportOptions._Cast_SystemDeflectionFEExportOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SystemDeflectionFEExportOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def alternative_fe_mesh_file(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AlternativeFEMeshFile

        if temp is None:
            return ""

        return temp

    @property
    def base_couplings_on_alternative_fe_mesh(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.BaseCouplingsOnAlternativeFEMesh

        if temp is None:
            return False

        return temp

    @base_couplings_on_alternative_fe_mesh.setter
    @enforce_parameter_types
    def base_couplings_on_alternative_fe_mesh(self: Self, value: "bool"):
        self.wrapped.BaseCouplingsOnAlternativeFEMesh = (
            bool(value) if value is not None else False
        )

    @property
    def default_type_of_result_to_export(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BoundaryConditionType":
        """EnumWithSelectedValue[mastapy.nodal_analysis.fe_export_utility.BoundaryConditionType]"""
        temp = self.wrapped.DefaultTypeOfResultToExport

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BoundaryConditionType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @default_type_of_result_to_export.setter
    @enforce_parameter_types
    def default_type_of_result_to_export(
        self: Self, value: "_168.BoundaryConditionType"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BoundaryConditionType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultTypeOfResultToExport = value

    @property
    def fe_export_format(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_FEExportFormat":
        """EnumWithSelectedValue[mastapy.nodal_analysis.fe_export_utility.FEExportFormat]"""
        temp = self.wrapped.FEExportFormat

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_FEExportFormat.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @fe_export_format.setter
    @enforce_parameter_types
    def fe_export_format(self: Self, value: "_169.FEExportFormat"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_FEExportFormat.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FEExportFormat = value

    @property
    def file_type(self: Self) -> "SystemDeflectionFEExportOptions.ExportType":
        """mastapy.system_model.fe.SystemDeflectionFEExportOptions.ExportType"""
        temp = self.wrapped.FileType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.FE.SystemDeflectionFEExportOptions+ExportType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.fe.SystemDeflectionFEExportOptions.SystemDeflectionFEExportOptions",
            "ExportType",
        )(value)

    @file_type.setter
    @enforce_parameter_types
    def file_type(self: Self, value: "SystemDeflectionFEExportOptions.ExportType"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.FE.SystemDeflectionFEExportOptions+ExportType",
        )
        self.wrapped.FileType = value

    @property
    def force_unit(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.ForceUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @force_unit.setter
    @enforce_parameter_types
    def force_unit(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ForceUnit = value

    @property
    def include_rigid_coupling_nodes_and_constraints_added_by_masta(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeRigidCouplingNodesAndConstraintsAddedByMASTA

        if temp is None:
            return False

        return temp

    @include_rigid_coupling_nodes_and_constraints_added_by_masta.setter
    @enforce_parameter_types
    def include_rigid_coupling_nodes_and_constraints_added_by_masta(
        self: Self, value: "bool"
    ):
        self.wrapped.IncludeRigidCouplingNodesAndConstraintsAddedByMASTA = (
            bool(value) if value is not None else False
        )

    @property
    def include_an_fe_mesh(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeAnFEMesh

        if temp is None:
            return False

        return temp

    @include_an_fe_mesh.setter
    @enforce_parameter_types
    def include_an_fe_mesh(self: Self, value: "bool"):
        self.wrapped.IncludeAnFEMesh = bool(value) if value is not None else False

    @property
    def length_unit(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.LengthUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @length_unit.setter
    @enforce_parameter_types
    def length_unit(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.LengthUnit = value

    @property
    def path_of_fe_mesh_file_to_be_included(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PathOfFEMeshFileToBeIncluded

        if temp is None:
            return ""

        return temp

    @property
    def use_rigid_coupling_types_from_fe_substructure_for_exported_couplings(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.UseRigidCouplingTypesFromFESubstructureForExportedCouplings

        if temp is None:
            return False

        return temp

    @use_rigid_coupling_types_from_fe_substructure_for_exported_couplings.setter
    @enforce_parameter_types
    def use_rigid_coupling_types_from_fe_substructure_for_exported_couplings(
        self: Self, value: "bool"
    ):
        self.wrapped.UseRigidCouplingTypesFromFESubstructureForExportedCouplings = (
            bool(value) if value is not None else False
        )

    @property
    def links(self: Self) -> "List[_2411.PerLinkExportOptions]":
        """List[mastapy.system_model.fe.PerLinkExportOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Links

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def nodes(self: Self) -> "List[_2412.PerNodeExportOptions]":
        """List[mastapy.system_model.fe.PerNodeExportOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Nodes

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
    def export_to_file(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.ExportToFile(file_path if file_path else "")

    @enforce_parameter_types
    def export_to_op2_file(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.ExportToOP2File(file_path if file_path else "")

    @enforce_parameter_types
    def set_alternative_fe_mesh_file(
        self: Self,
        file_path: "str",
        format_: "_169.FEExportFormat",
        length_scale: "float" = 1.0,
        force_scale: "float" = 1.0,
    ):
        """Method does not return.

        Args:
            file_path (str)
            format_ (mastapy.nodal_analysis.fe_export_utility.FEExportFormat)
            length_scale (float, optional)
            force_scale (float, optional)
        """
        file_path = str(file_path)
        format_ = conversion.mp_to_pn_enum(
            format_, "SMT.MastaAPI.NodalAnalysis.FeExportUtility.FEExportFormat"
        )
        length_scale = float(length_scale)
        force_scale = float(force_scale)
        self.wrapped.SetAlternativeFEMeshFile(
            file_path if file_path else "",
            format_,
            length_scale if length_scale else 0.0,
            force_scale if force_scale else 0.0,
        )

    @enforce_parameter_types
    def set_fe_mesh_file_to_include(
        self: Self,
        file_path: "str",
        format_: "_169.FEExportFormat",
        length_scale: "float" = 1.0,
        force_scale: "float" = 1.0,
    ):
        """Method does not return.

        Args:
            file_path (str)
            format_ (mastapy.nodal_analysis.fe_export_utility.FEExportFormat)
            length_scale (float, optional)
            force_scale (float, optional)
        """
        file_path = str(file_path)
        format_ = conversion.mp_to_pn_enum(
            format_, "SMT.MastaAPI.NodalAnalysis.FeExportUtility.FEExportFormat"
        )
        length_scale = float(length_scale)
        force_scale = float(force_scale)
        self.wrapped.SetFEMeshFileToInclude(
            file_path if file_path else "",
            format_,
            length_scale if length_scale else 0.0,
            force_scale if force_scale else 0.0,
        )

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
    ) -> "SystemDeflectionFEExportOptions._Cast_SystemDeflectionFEExportOptions":
        return self._Cast_SystemDeflectionFEExportOptions(self)
