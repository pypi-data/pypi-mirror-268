"""ModalAnalysisBarModelFEExportOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value
from mastapy.system_model.part_model import _2460
from mastapy.nodal_analysis.fe_export_utility import _169
from mastapy.utility.units_and_measurements import _1617
from mastapy.nodal_analysis import _53
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_BAR_MODEL_FE_EXPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ModalAnalysisBarModelFEExportOptions",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _52
    from mastapy.nodal_analysis.dev_tools_analyses import _182


__docformat__ = "restructuredtext en"
__all__ = ("ModalAnalysisBarModelFEExportOptions",)


Self = TypeVar("Self", bound="ModalAnalysisBarModelFEExportOptions")


class ModalAnalysisBarModelFEExportOptions(_0.APIBase):
    """ModalAnalysisBarModelFEExportOptions

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_BAR_MODEL_FE_EXPORT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalAnalysisBarModelFEExportOptions")

    class _Cast_ModalAnalysisBarModelFEExportOptions:
        """Special nested class for casting ModalAnalysisBarModelFEExportOptions to subclasses."""

        def __init__(
            self: "ModalAnalysisBarModelFEExportOptions._Cast_ModalAnalysisBarModelFEExportOptions",
            parent: "ModalAnalysisBarModelFEExportOptions",
        ):
            self._parent = parent

        @property
        def modal_analysis_bar_model_fe_export_options(
            self: "ModalAnalysisBarModelFEExportOptions._Cast_ModalAnalysisBarModelFEExportOptions",
        ) -> "ModalAnalysisBarModelFEExportOptions":
            return self._parent

        def __getattr__(
            self: "ModalAnalysisBarModelFEExportOptions._Cast_ModalAnalysisBarModelFEExportOptions",
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
        self: Self, instance_to_wrap: "ModalAnalysisBarModelFEExportOptions.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_type(self: Self) -> "_52.BarModelAnalysisType":
        """mastapy.nodal_analysis.BarModelAnalysisType"""
        temp = self.wrapped.AnalysisType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.BarModelAnalysisType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._52", "BarModelAnalysisType"
        )(value)

    @analysis_type.setter
    @enforce_parameter_types
    def analysis_type(self: Self, value: "_52.BarModelAnalysisType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.BarModelAnalysisType"
        )
        self.wrapped.AnalysisType = value

    @property
    def connect_to_full_fe_mesh(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ConnectToFullFEMesh

        if temp is None:
            return False

        return temp

    @connect_to_full_fe_mesh.setter
    @enforce_parameter_types
    def connect_to_full_fe_mesh(self: Self, value: "bool"):
        self.wrapped.ConnectToFullFEMesh = bool(value) if value is not None else False

    @property
    def coordinate_system(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_FEPart":
        """ListWithSelectedItem[mastapy.system_model.part_model.FEPart]"""
        temp = self.wrapped.CoordinateSystem

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_FEPart",
        )(temp)

    @coordinate_system.setter
    @enforce_parameter_types
    def coordinate_system(self: Self, value: "_2460.FEPart"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_FEPart.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_FEPart.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.CoordinateSystem = value

    @property
    def error_message(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ErrorMessage

        if temp is None:
            return ""

        return temp

    @property
    def fe_file_to_include(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEFileToInclude

        if temp is None:
            return ""

        return temp

    @property
    def fe_package(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_FEExportFormat":
        """EnumWithSelectedValue[mastapy.nodal_analysis.fe_export_utility.FEExportFormat]"""
        temp = self.wrapped.FEPackage

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_FEExportFormat.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @fe_package.setter
    @enforce_parameter_types
    def fe_package(self: Self, value: "_169.FEExportFormat"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_FEExportFormat.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FEPackage = value

    @property
    def fe_part(self: Self) -> "list_with_selected_item.ListWithSelectedItem_FEPart":
        """ListWithSelectedItem[mastapy.system_model.part_model.FEPart]"""
        temp = self.wrapped.FEPart

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_FEPart",
        )(temp)

    @fe_part.setter
    @enforce_parameter_types
    def fe_part(self: Self, value: "_2460.FEPart"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_FEPart.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_FEPart.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.FEPart = value

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
    def shaft_export_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BarModelExportType":
        """EnumWithSelectedValue[mastapy.nodal_analysis.BarModelExportType]"""
        temp = self.wrapped.ShaftExportType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BarModelExportType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @shaft_export_type.setter
    @enforce_parameter_types
    def shaft_export_type(self: Self, value: "_53.BarModelExportType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BarModelExportType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ShaftExportType = value

    @property
    def use_fe_file_from_fe_substructure(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseFEFileFromFESubstructure

        if temp is None:
            return False

        return temp

    @use_fe_file_from_fe_substructure.setter
    @enforce_parameter_types
    def use_fe_file_from_fe_substructure(self: Self, value: "bool"):
        self.wrapped.UseFEFileFromFESubstructure = (
            bool(value) if value is not None else False
        )

    @property
    def mode_options(self: Self) -> "_182.EigenvalueOptions":
        """mastapy.nodal_analysis.dev_tools_analyses.EigenvalueOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModeOptions

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

    @enforce_parameter_types
    def export_to_file(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.ExportToFile(file_path if file_path else "")

    @enforce_parameter_types
    def set_fe_file_to_include(
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
        self.wrapped.SetFEFileToInclude(
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
    ) -> "ModalAnalysisBarModelFEExportOptions._Cast_ModalAnalysisBarModelFEExportOptions":
        return self._Cast_ModalAnalysisBarModelFEExportOptions(self)
