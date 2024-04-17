"""HarmonicAnalysisExportOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value
from mastapy.utility.units_and_measurements import _1617
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
from mastapy.system_model.analyses_and_results.modal_analyses import _4635
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_EXPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HarmonicAnalysisExportOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5774,
        _5772,
        _5775,
        _5776,
    )
    from mastapy.system_model.part_model import _2475


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisExportOptions",)


Self = TypeVar("Self", bound="HarmonicAnalysisExportOptions")
TPartAnalysis = TypeVar("TPartAnalysis")
TPart = TypeVar("TPart", bound="_2475.Part")


class HarmonicAnalysisExportOptions(_0.APIBase, Generic[TPartAnalysis, TPart]):
    """HarmonicAnalysisExportOptions

    This is a mastapy class.

    Generic Types:
        TPartAnalysis
        TPart
    """

    TYPE = _HARMONIC_ANALYSIS_EXPORT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicAnalysisExportOptions")

    class _Cast_HarmonicAnalysisExportOptions:
        """Special nested class for casting HarmonicAnalysisExportOptions to subclasses."""

        def __init__(
            self: "HarmonicAnalysisExportOptions._Cast_HarmonicAnalysisExportOptions",
            parent: "HarmonicAnalysisExportOptions",
        ):
            self._parent = parent

        @property
        def harmonic_analysis_fe_export_options(
            self: "HarmonicAnalysisExportOptions._Cast_HarmonicAnalysisExportOptions",
        ) -> "_5772.HarmonicAnalysisFEExportOptions":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5772,
            )

            return self._parent._cast(_5772.HarmonicAnalysisFEExportOptions)

        @property
        def harmonic_analysis_root_assembly_export_options(
            self: "HarmonicAnalysisExportOptions._Cast_HarmonicAnalysisExportOptions",
        ) -> "_5775.HarmonicAnalysisRootAssemblyExportOptions":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5775,
            )

            return self._parent._cast(_5775.HarmonicAnalysisRootAssemblyExportOptions)

        @property
        def harmonic_analysis_shaft_export_options(
            self: "HarmonicAnalysisExportOptions._Cast_HarmonicAnalysisExportOptions",
        ) -> "_5776.HarmonicAnalysisShaftExportOptions":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(_5776.HarmonicAnalysisShaftExportOptions)

        @property
        def harmonic_analysis_export_options(
            self: "HarmonicAnalysisExportOptions._Cast_HarmonicAnalysisExportOptions",
        ) -> "HarmonicAnalysisExportOptions":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisExportOptions._Cast_HarmonicAnalysisExportOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicAnalysisExportOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_units_for_export(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.DistanceUnitsForExport

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @distance_units_for_export.setter
    @enforce_parameter_types
    def distance_units_for_export(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.DistanceUnitsForExport = value

    @property
    def export_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ExportOutputType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.harmonic_analyses.ExportOutputType]"""
        temp = self.wrapped.ExportType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ExportOutputType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @export_type.setter
    @enforce_parameter_types
    def export_type(self: Self, value: "_5753.ExportOutputType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ExportOutputType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ExportType = value

    @property
    def planetary_duplicate_to_export(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_TPartAnalysis":
        """ListWithSelectedItem[TPartAnalysis]"""
        temp = self.wrapped.PlanetaryDuplicateToExport

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_TPartAnalysis",
        )(temp)

    @planetary_duplicate_to_export.setter
    @enforce_parameter_types
    def planetary_duplicate_to_export(self: Self, value: "TPartAnalysis"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_TPartAnalysis.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_TPartAnalysis.implicit_type()
        )
        value = wrapper_type[enclosed_type](value if value is not None else None)
        self.wrapped.PlanetaryDuplicateToExport = value

    @property
    def status_message_for_export(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatusMessageForExport

        if temp is None:
            return ""

        return temp

    @property
    def type_of_result_to_export(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.modal_analyses.DynamicsResponseType]"""
        temp = self.wrapped.TypeOfResultToExport

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @type_of_result_to_export.setter
    @enforce_parameter_types
    def type_of_result_to_export(self: Self, value: "_4635.DynamicsResponseType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TypeOfResultToExport = value

    @property
    def analysis_options(self: Self) -> "_5774.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisOptions

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

    def export_results(self: Self):
        """Method does not return."""
        self.wrapped.ExportResults()

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
    ) -> "HarmonicAnalysisExportOptions._Cast_HarmonicAnalysisExportOptions":
        return self._Cast_HarmonicAnalysisExportOptions(self)
