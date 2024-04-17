"""FESubstructureExportOptions"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.nodal_analysis.fe_export_utility import _170
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.utility.units_and_measurements import _1617
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_EXPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureExportOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureExportOptions",)


Self = TypeVar("Self", bound="FESubstructureExportOptions")


class FESubstructureExportOptions(_0.APIBase):
    """FESubstructureExportOptions

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_EXPORT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FESubstructureExportOptions")

    class _Cast_FESubstructureExportOptions:
        """Special nested class for casting FESubstructureExportOptions to subclasses."""

        def __init__(
            self: "FESubstructureExportOptions._Cast_FESubstructureExportOptions",
            parent: "FESubstructureExportOptions",
        ):
            self._parent = parent

        @property
        def fe_substructure_export_options(
            self: "FESubstructureExportOptions._Cast_FESubstructureExportOptions",
        ) -> "FESubstructureExportOptions":
            return self._parent

        def __getattr__(
            self: "FESubstructureExportOptions._Cast_FESubstructureExportOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FESubstructureExportOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_package(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_FESubstructuringFileFormat":
        """EnumWithSelectedValue[mastapy.nodal_analysis.fe_export_utility.FESubstructuringFileFormat]"""
        temp = self.wrapped.FEPackage

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_FESubstructuringFileFormat.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @fe_package.setter
    @enforce_parameter_types
    def fe_package(self: Self, value: "_170.FESubstructuringFileFormat"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_FESubstructuringFileFormat.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FEPackage = value

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
    def include_condensation_node_displacement_expansion(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeCondensationNodeDisplacementExpansion

        if temp is None:
            return False

        return temp

    @include_condensation_node_displacement_expansion.setter
    @enforce_parameter_types
    def include_condensation_node_displacement_expansion(self: Self, value: "bool"):
        self.wrapped.IncludeCondensationNodeDisplacementExpansion = (
            bool(value) if value is not None else False
        )

    @property
    def include_fe_mesh_definition(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeFEMeshDefinition

        if temp is None:
            return False

        return temp

    @include_fe_mesh_definition.setter
    @enforce_parameter_types
    def include_fe_mesh_definition(self: Self, value: "bool"):
        self.wrapped.IncludeFEMeshDefinition = (
            bool(value) if value is not None else False
        )

    @property
    def include_reduced_gravity_load(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeReducedGravityLoad

        if temp is None:
            return False

        return temp

    @include_reduced_gravity_load.setter
    @enforce_parameter_types
    def include_reduced_gravity_load(self: Self, value: "bool"):
        self.wrapped.IncludeReducedGravityLoad = (
            bool(value) if value is not None else False
        )

    @property
    def include_reduced_thermal_expansion_force(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeReducedThermalExpansionForce

        if temp is None:
            return False

        return temp

    @include_reduced_thermal_expansion_force.setter
    @enforce_parameter_types
    def include_reduced_thermal_expansion_force(self: Self, value: "bool"):
        self.wrapped.IncludeReducedThermalExpansionForce = (
            bool(value) if value is not None else False
        )

    @property
    def include_reduction_commands(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeReductionCommands

        if temp is None:
            return False

        return temp

    @include_reduction_commands.setter
    @enforce_parameter_types
    def include_reduction_commands(self: Self, value: "bool"):
        self.wrapped.IncludeReductionCommands = (
            bool(value) if value is not None else False
        )

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
    ) -> "FESubstructureExportOptions._Cast_FESubstructureExportOptions":
        return self._Cast_FESubstructureExportOptions(self)
